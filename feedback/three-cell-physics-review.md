# Physicist Review of the Three-Cell Finite Selector Gate

Date: 18 July 2026

Scope: adversarial review of the physical model, interpretation, and claim
boundaries in [`three-cell-finite-gate.md`](../research/three-cell-finite-gate.md)
and [`ec_three_cell_selector.py`](../research/ec_three_cell_selector.py).
The numerical and algebraic implementation is reviewed separately.

## Verdict

The calculation is physically readable as a finite CAR toy-model stress test.
It is not a controlled lattice discretization of Einstein-Cartan-Dirac theory,
a thermodynamic limit, or evidence for a cosmological selector. The three-cell
result fails the relevant boundary-independent robustness test: the open chain
fails, while the periodic ring passes only the restricted numerical gate.

The periodic result may be reported as a numerical branch of the toy model, but
not as a rescue, confirmation, or EC-specific mechanism. With that limitation,
the result is worth including because it materially narrows the positive
two-cell finding and prevents selective reporting.

## Findings

### 1. Major: boundary sensitivity is inseparable from finite geometry

At three cells, changing from an open chain to a periodic ring changes two
bonds into three. The boundary contribution is therefore an order-one change
to the Hamiltonian, not a small boundary perturbation to a common bulk system.
The two calculations cannot establish a boundary-independent phase or a
thermodynamic selector.

The cell kinetic matrix is the nearest-neighbour central-difference operator.
For a periodic lattice its one-particle eigenvalues are

$$
\lambda_m=2\sin\left(\frac{2\pi m}{L}\right).
$$

Thus the three-cell ring has spectrum $\{-\sqrt3,0,+\sqrt3\}$, whereas a
four-cell ring would have $\{-2,0,0,+2\}$. The latter contains the additional
$k=\pi$ zero of the naive lattice derivative. The passing three-cell periodic
branch is consequently entangled with odd lattice size and the elementary
lattice-fermion doubling issue. No large-$L$ inference is available.

Required interpretation: the combined three-cell verdict is
**boundary-sensitive/inconclusive**, and therefore a failure of the proposed
boundary-independent robustness gate. The periodic branch is a finite
numerical observation only.

### 2. Major: the EC connection remains channel-level motivation

Eliminating non-propagating torsion can generate local four-fermion terms,
including an axial-axial channel. That supports using the onsite operator as an
EC-inspired interaction. It does not derive this one-dimensional lattice
Hamiltonian, the $U(3)$ candidate family, the Hilbert-Schmidt selector, the
equal-endpoint coupling, or an aeonic transition.

The model keeps one spatial kinetic direction while retaining all three spatial
components in the axial-current Lorentz contraction. It is deliberately not a
controlled dimensional reduction. The selected $g/t=O(1)$ regime is also where
a gravitational-strength dimension-six contact would generally require
Planckian lattice scales, outside a controlled low-energy EC expansion.

These caveats are already present in the two-cell companion note and must be
carried into every three-cell summary.

### 3. Major: equal-endpoint tuning is not a prediction

The coupling $g_c$ is chosen separately for each geometry and filling by
forcing the site and kinetic-eigenmode endpoint costs to agree. This is a valid
way to inspect whether competing branches can exist, but it builds endpoint
competition into the test. Neither $g_c$ nor the existence of an equal-cost
point is derived from EC dynamics.

The filling controls likewise compare filling-dependent tuned couplings. They
test a normalized selector identity and stationary-state behavior, not a single
Hamiltonian transported across different fillings.

### 4. Major: the finite geometry is not EC-specific

The non-EC onsite density contact also gives strict site and kinetic endpoints
under the same tuning procedure. Therefore the branch competition is evidence
for generic kinetic-versus-onsite locality competition, not for torsion or EC
dynamics. This control should appear beside the three-cell result, not only in
a limitations paragraph.

### 5. Moderate: the stationary state is a toy many-body state

The fixed-$N$ ground state is a state of twelve bare fermionic modes. It is not
a relativistic vacuum with a specified Dirac-sea prescription, a state of a
gravitating quantum field, or a cosmological state. Half filling is a finite
occupation-sector choice. The spectral gap and entropy contrasts are valid
within that model only.

The code correctly withholds entropy evidence when the numerical ground space
is degenerate. The isolated even-filling results may be reported, but they do
not repair the selector's boundary dependence.

### 6. Moderate: the entropy is not thermodynamic entropy

The reported quantities are average one-cell mode entropies, with additional
local-number and parity-superselection diagnostics. They establish
factorization dependence of a finite pure state's reduced entropy. They do not
model heat death, Boltzmann entropy, cosmological observational entropy, or an
entropy reset.

## Required claim boundary for v0.1.3

The defensible summary is:

> Extending the restricted CAR calculation from two to three cells does not
> produce boundary-independent robustness. The open-chain kinetic endpoint has
> a negative Hessian direction and a lower mixed factorization, whereas the
> periodic ring retains two strict sampled endpoints and an isolated
> positive-contrast state at even tested fillings. Because the finite graphs
> and naive-derivative spectra differ at order one, and because a non-EC onsite
> control produces analogous endpoint competition, this is a boundary-sensitive
> finite-size result rather than evidence for an EC-derived or cosmological
> selector.

## Publication recommendation

Include the result in unpublished v0.1.3 as an adverse finite-size stress test.
Do not make the periodic pass part of the abstract's positive claim. Link the
full script and technical report, state that four cells and the continuum limit
were not tested, and leave the EC/CAR mechanism classified as an exploratory
side branch.

## Resolution in v0.1.3

Resolved on 20 July 2026. The manuscript, README, companion note, and release
notes classify the combined result as a boundary-independent robustness
failure. The periodic branch is presented only as a restricted numerical
observation; the order-one graph/spectrum difference, tuned coupling, non-EC
control, entropy scope, and absence of a four-cell or continuum result are all
stated explicitly.

## Physical references used for scope

- D. Diakonov, A. G. Tumanov, and A. A. Vladimirov, [Low-energy general
  relativity with torsion: a systematic derivative
  expansion](https://arxiv.org/abs/1104.2432), *Physical Review D* 84,
  124042 (2011). Supports torsion-induced local four-fermion channels, not the
  selector.
- H. B. Nielsen and M. Ninomiya, [A no-go theorem for regularizing chiral
  fermions](https://doi.org/10.1016/0370-2693(81)91026-1), *Physics Letters B*
  105, 219-223 (1981). General lattice-fermion context; the finite spectra above
  are obtained directly from the model and do not rely on invoking the theorem.
