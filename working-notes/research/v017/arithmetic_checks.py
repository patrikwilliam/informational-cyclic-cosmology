"""Small diagnostics for the conditional arithmetic reconstruction.

No test is a proof of an infinite-dimensional or physical statement. Finite
shifts are partial isometries at the specified boundary, not full isometries.
"""

import argparse
import json
from pathlib import Path

import numpy as np


def opnorm(matrix):
    return float(np.linalg.norm(matrix, ord=2))


def require_small(value, name, tolerance=1e-10):
    if not np.isfinite(value) or value > tolerance:
        raise AssertionError(f"{name}: {value} exceeds {tolerance}")


def shift(labels, multiplier, phases=None):
    indices = {label: i for i, label in enumerate(labels)}
    result = np.zeros((len(labels), len(labels)), dtype=complex)
    if phases is None:
        phases = np.ones(len(labels), dtype=complex)
    for n, source in indices.items():
        target = indices.get(multiplier * n)
        if target is not None:
            result[target, source] = phases[target] * phases[source].conjugate()
    return result


def frequency_component(probe, labels, multiplier):
    return probe * (np.abs(shift(labels, multiplier)) > 0)


def polar_partial(matrix):
    left, singular, right = np.linalg.svd(matrix)
    # Discard numerical zeros from the finite boundary, not small true weights.
    active = singular > 1e-12
    return (left[:, active] @ right[active, :], singular[active])


def entropy(density):
    eigenvalues = np.linalg.eigvalsh(density)
    if eigenvalues.min() < -1e-10:
        raise AssertionError("Density matrix is not positive")
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-np.sum(eigenvalues * np.log2(eigenvalues)))


def local_entropy(density, labels, side_a, side_b):
    order = [labels.index(2**a * 3**b) for a in range(side_a)
             for b in range(side_b)]
    tensor = density[np.ix_(order, order)].reshape(
        side_a, side_b, side_a, side_b
    )
    return entropy(np.einsum("abcb->ac", tensor))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Optional diagnostic output file")
    arguments = parser.parse_args()
    rng = np.random.default_rng(20261010)
    labels = sorted(2**a * 3**b for a in range(4) for b in range(3))
    size = len(labels)
    energies = np.log(labels)
    hamiltonian = np.diag(energies)
    magnitudes = rng.uniform(0.5, 1.5, size)
    phases = np.exp(1j * rng.uniform(-np.pi, np.pi, size))
    reference = magnitudes * phases
    reference /= np.linalg.norm(reference)
    probe = np.outer(reference, reference.conjugate())
    results = {}
    operators = {}

    max_polar_error = 0.0
    max_covariance_error = 0.0
    max_boundary_error = 0.0
    smallest_weight = 1.0
    for multiplier in (1, 2, 3, 4, 6):
        component = frequency_component(probe, labels, multiplier)
        operator, weights = polar_partial(component)
        expected = shift(labels, multiplier, phases)
        operators[multiplier] = operator
        max_polar_error = max(max_polar_error, opnorm(operator - expected))
        max_covariance_error = max(max_covariance_error, opnorm(
            hamiltonian @ operator - operator @ hamiltonian
            - np.log(multiplier) * operator
        ))
        allowed = np.diag([float(multiplier*n in labels) for n in labels])
        max_boundary_error = max(max_boundary_error, opnorm(
            operator.conj().T @ operator - allowed
        ))
        smallest_weight = min(smallest_weight, float(weights.min()))
    for name, error in [("polar_reconstruction", max_polar_error),
                        ("frequency_covariance", max_covariance_error),
                        ("boundary_partial_isometry", max_boundary_error)]:
        require_small(error, name)
        results[name] = error
    results["smallest_tested_nonzero_probe_weight"] = smallest_weight

    max_energy_error = 0.0
    for multiplier in (2, 3, 4, 6):
        operator = operators[multiplier]
        allowed = operator.conj().T @ operator
        max_energy_error = max(max_energy_error, opnorm(
            operator.conj().T @ hamiltonian @ operator
            - allowed @ (hamiltonian + np.log(multiplier)*np.eye(size))
        ))
    require_small(max_energy_error, "energy_on_allowed_finite_domain")
    results["energy_on_allowed_finite_domain"] = max_energy_error

    missing_probe = probe.copy()
    missing_probe[labels.index(2), labels.index(1)] = 0
    missing_probe[labels.index(1), labels.index(2)] = 0
    missing_shift, _ = polar_partial(frequency_component(missing_probe, labels, 2))
    missing_support = np.diag([float(2*n in labels and n != 1) for n in labels])
    missing_error = opnorm(missing_shift.conj().T @ missing_shift - missing_support)
    require_small(missing_error, "missing_transition_partial_isometry")
    results["missing_transition_partial_isometry"] = missing_error

    semigroup_error = max(
        opnorm(operators[2] @ operators[3] - operators[6]),
        opnorm(operators[3] @ operators[2] - operators[6]),
        opnorm(operators[2] @ operators[2] - operators[4]),
    )
    require_small(semigroup_error, "semigroup")
    results["semigroup"] = semigroup_error
    double_error = opnorm(operators[2] @ operators[3].conj().T
                         - operators[3].conj().T @ operators[2])
    require_small(double_error, "double_commutation_on_rectangular_window")
    results["double_commutation_on_rectangular_window"] = double_error

    # Reconstruct with spectral projectors after a generic basis rotation.
    random_matrix = rng.normal(size=(size, size)) + 1j*rng.normal(size=(size, size))
    unitary, _ = np.linalg.qr(random_matrix)
    rotated_h = unitary @ hamiltonian @ unitary.conj().T
    rotated_probe = unitary @ probe @ unitary.conj().T
    eigenvalues, eigenvectors = np.linalg.eigh(rotated_h)
    require_small(float(np.max(np.abs(eigenvalues - energies))), "eigenvalues")
    projectors = [np.outer(v, v.conjugate()) for v in eigenvectors.T]
    index = {n: i for i, n in enumerate(labels)}
    rotated_component = np.zeros_like(probe)
    for n in labels:
        if 2*n in index:
            rotated_component += projectors[index[2*n]] @ rotated_probe @ projectors[index[n]]
    rotated_shift, _ = polar_partial(rotated_component)
    basis_error = opnorm(rotated_shift - unitary @ operators[2] @ unitary.conj().T)
    require_small(basis_error, "generic_basis_covariance")
    results["generic_basis_covariance"] = basis_error

    # Perturb a Hermitian probe's edge phase, not the energy spectrum.
    bad_probe = probe.copy()
    i, j = index[6], index[2]
    bad_probe[i, j] *= np.exp(1j*np.pi/3)
    bad_probe[j, i] = bad_probe[i, j].conjugate()
    bad_2, _ = polar_partial(frequency_component(bad_probe, labels, 2))
    bad_3, _ = polar_partial(frequency_component(bad_probe, labels, 3))
    commutator = bad_2 @ bad_3 - bad_3 @ bad_2
    witness = float(abs(commutator[index[6], index[1]]))
    require_small(abs(witness - 1.0), "nonflat_probe_control")
    results["nonflat_probe_commutator_witness"] = witness

    time = 0.713
    evolved_reference = np.exp(-1j*time*energies) * reference
    evolved_probe = np.outer(evolved_reference, evolved_reference.conjugate())
    evolved_shift, _ = polar_partial(frequency_component(evolved_probe, labels, 2))
    evolution_error = opnorm(evolved_shift - np.exp(-1j*time*np.log(2))*operators[2])
    require_small(evolution_error, "free_reference_evolution")
    results["free_reference_evolution_scalar_only"] = evolution_error

    probabilities = rng.uniform(0.1, 1.0, size)
    stationary = np.diag(probabilities / probabilities.sum())
    diagonal = np.diag(phases)
    transported = diagonal.conj().T @ stationary @ diagonal
    state_error = opnorm(transported - stationary)
    entropy_error = abs(local_entropy(transported, labels, 4, 3)
                        - local_entropy(stationary, labels, 4, 3))
    require_small(state_error, "stationary_state")
    require_small(entropy_error, "stationary_entropy")
    results["stationary_state_invariance"] = state_error
    results["stationary_entropy_invariance_bits"] = entropy_error

    order = [labels.index(2**a * 3**b) for a in range(4) for b in range(3)]
    old_reduced = np.einsum("abcb->ac", stationary[np.ix_(order, order)].reshape(4, 3, 4, 3))
    new_reduced = np.einsum("abcb->ac", transported[np.ix_(order, order)].reshape(4, 3, 4, 3))
    spectrum_error = float(np.max(np.abs(np.linalg.eigvalsh(old_reduced)
                                        - np.linalg.eigvalsh(new_reduced))))
    require_small(spectrum_error, "stationary_restricted_spectrum")
    results["stationary_restricted_spectrum"] = spectrum_error

    small_labels = [1, 2, 3, 6]
    # Positive magnitudes do not force a product state in the recovered factors.
    generic_reference = np.array([1., 3., 2., 4.]) / np.sqrt(30.)
    generic_density = np.outer(generic_reference, generic_reference)
    nonproduct_entropy = local_entropy(generic_density, small_labels, 2, 2)
    if nonproduct_entropy <= 0.01:
        raise AssertionError("Generic reference unexpectedly became a product")
    results["nonproduct_reference_entropy_bits"] = nonproduct_entropy

    instability = []
    standard_2 = shift(small_labels, 2)
    for epsilon in (0.1, 0.001, 0.00001):
        ref = np.array([1., 1., 1., epsilon])
        ref /= np.linalg.norm(ref)
        changed = ref * np.array([1., 1., 1., -1.])
        changed_probe = np.outer(changed, changed)
        changed_shift, _ = polar_partial(frequency_component(changed_probe, small_labels, 2))
        distance = opnorm(changed_shift - standard_2)
        a = abs(ref[-1])
        trace_distance = 2*a*np.sqrt(1-a*a)
        require_small(abs(distance - 2.0), "phase_instability")
        # In the standard first-prime algebra these two entries must coincide.
        first = changed_shift[1, 0]
        second = changed_shift[3, 2]
        algebra_distance_lower_bound = float(abs(first - second)/2)
        require_small(abs(algebra_distance_lower_bound - 1), "algebra_witness")
        instability.append({"epsilon": epsilon, "reference_trace_distance": trace_distance,
                            "shift_operator_distance": distance,
                            "algebra_distance_lower_bound": algebra_distance_lower_bound})
    results["small_reference_error_control"] = instability
    results["diagnostic_names"] = [key for key in results
                                   if key != "smallest_tested_nonzero_probe_weight"]
    results["configuration"] = {"seed": 20261010, "absolute_tolerance": 1e-10,
                                "prime_occupation_window": [4, 3]}
    results["status"] = "All finite diagnostic assertions passed"
    results["scope"] = "No continuum, selector, or cosmological validation"
    output = json.dumps(results, indent=2) + "\n"
    if arguments.json:
        arguments.json.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
