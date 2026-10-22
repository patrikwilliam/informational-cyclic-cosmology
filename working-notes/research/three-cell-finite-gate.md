# Three-Cell Finite Selector Gate

Date: 20 July 2026

Status: exploratory v0.1.3 finite-size stress test; numerical and not
independently peer reviewed.

Release-status note (14 September 2026, ICC v0.1.4): the dated three-cell
calculation below is retained as a historical gate. Subsequent
[four-cell](./four-cell-finite-gate.md),
[boundary-phase](./four-cell-boundary-phase-gate.md),
[matched-control](./four-cell-matched-control-gate.md), and
[onsite-closure](./four-cell-onsite-closure.md) work is now included in the
package. It does not establish boundary-independent robustness or a continuum
selector, and the matched-control and closure results remove EC specificity
from the declared residual law.

Reproducible calculation:
[`ec_three_cell_selector.py`](./ec_three_cell_selector.py)

## 1. Predeclared question

Does the restricted two-cell CAR selector survive the first nontrivial increase
in spatial cell count without narrowing the admissible factorization family?

The primary gate was fixed before inspecting the result, but was not externally
preregistered:

- three cells and four Dirac modes per cell;
- the half-filled sector $N=6$;
- both open and periodic nearest-neighbour kinetic terms;
- all number-preserving cell transformations $W\in U(3)$ that preserve the
  common internal Dirac factor, modulo column phases and permutations;
- the same centered fixed-sector Hilbert-Schmidt interaction projection used in
  the two-cell follow-up;
- site and kinetic-eigenmode endpoints placed at equal selector cost;
- all six physical off-diagonal tangent directions on
  $U(3)/(U(1)^3\rtimes S_3)$;
- phase/permutation invariance, random sampling, multi-start descent, an
  isolated ground state, and positive average one-cell mode, local-number-SSR,
  and local-parity-SSR entropy contrasts.

The decision rule was also fixed in advance. Failure under both boundary
conditions is a stop condition. If exactly one boundary condition passes, the
result is boundary-sensitive; a four-cell or analytic large-size calculation
would be required before making a boundary-independent claim. Neither was part
of this three-cell calculation; later four-cell work is linked above.

## 2. Model and projection

The fixed sector has

$$
\mathcal H_{3,6}=\bigwedge^6\mathbb C^{12},
\qquad
\dim\mathcal H_{3,6}=\binom{12}{6}=924.
$$

The Hamiltonian is the direct three-cell extension

$$
H(t,g)=tK+gQ,
$$

where $K$ is the sum of oriented nearest-neighbour massless Dirac links and
$Q$ is the sum of the same normal-ordered onsite axial-current contact terms
used in v0.1.3.

At fixed total number, the one-cell Hamiltonian space is the restriction of

$$
A_1\otimes I\otimes I
+I\otimes A_2\otimes I
+I\otimes I\otimes A_3,
$$

with each $A_x$ preserving its local particle number. Unlike the two-cell
case, the same local charge block occurs with several complementary charge
pairs. The script therefore constructs the complete matrix-unit Gram matrix
and its Moore-Penrose inverse rather than projecting each charge triple
independently. The resulting local subspace has dimension 207.

The number-preserving lift $\Gamma(W\otimes I_4)$ is evaluated blockwise in
the four conserved spinor-flavour occupations. No full $4096\times4096$ Fock
matrix is constructed.

There are $3\times70=210$ labelled one-cell matrix-unit generators. Two
relations identify the three copies of the fixed-sector identity, and a third
is $N_1+N_2+N_3=6I$. Exact row reduction of the integer Gram matrix modulo
$1{,}000{,}003$ gives rank 207. The nonzero modular minor and the three exact
relations together certify that the rank over $\mathbb Q$ is exactly 207.

## 3. Validation

The generalized implementation reproduces the existing $L=2,N=4$ calculation:

| Check | Largest error |
|---|---:|
| Hamiltonian matrices | $0$ |
| Endpoint residual components | $4.55\times10^{-13}$ |
| Published gap and three entropy contrasts | $0$ at displayed precision |
| Projection audit | $3.69\times10^{-14}$ |

For $L=3,N=6$:

| Check | Error |
|---|---:|
| Lift representation $\Gamma(W_1W_2)=\Gamma(W_1)\Gamma(W_2)$ | $6.5\times10^{-16}$ |
| One-body covariance | $2.8\times10^{-15}$ |
| Lift unitarity | $4.6\times10^{-15}$ |
| Projection idempotence | $2.4\times10^{-15}$ |
| Residual orthogonality | $1.1\times10^{-13}$ |
| Generic phase/permutation invariance of the selector | $7.7\times10^{-14}$ |

All endpoint Hessians were recomputed at chart steps $2\times10^{-3}$,
$10^{-3}$, $5\times10^{-4}$, and $2.5\times10^{-4}$. The smallest eigenvalues
remained in the following ranges:

| Boundary | Endpoint | Smallest-eigenvalue range |
|---|---|---:|
| Open | site | 0.1222236 to 0.1222249 |
| Open | kinetic | -0.0465285 to -0.0465275 |
| Periodic | site | 0.4866789 to 0.4866815 |
| Periodic | kinetic | 0.2433372 to 0.2433405 |

## 4. Primary half-filled result

At each boundary condition, $g_c$ is chosen before optimization by equating
the site and kinetic-eigenmode endpoint costs.

| Quantity | Open chain | Periodic ring |
|---|---:|---:|
| $g_c$ | 0.3501691221 | 0.4129483210 |
| Normalized endpoint cost | 0.4529794648 | 0.4717832957 |
| Minimum site Hessian eigenvalue | 0.1222247 | 0.4866812 |
| Minimum kinetic-basis Hessian eigenvalue | **-0.0465277** | 0.2433404 |
| Lowest optimized cost found | **0.4413803** | 0.4717832957 |
| Ground-space multiplicity | **3** | 1 |
| Spectral gap above ground space | 0.5688714 | 0.2033920 |
| Site-minus-momentum mode entropy | not evidential | 1.7508546 bits |
| Local-number-SSR contrast | not evidential | 0.6380137 bits |
| Local-parity-SSR contrast | not evidential | 0.9787055 bits |

The open-chain kinetic endpoint is not a local minimum on the full restricted
$U(3)$ candidate manifold. A multi-start descent also finds a lower mixed
factorization. Its selected stationary ground space is degenerate, so the
entropy of an arbitrary numerical eigenvector in that space is not used as
evidence.

For the periodic ring, both endpoints are numerically strict in all six tangent
directions.
An expanded search used 32 independent Haar samples and optimized eight random
starts for up to 80 iterations, in addition to the two exact endpoints. Across
7,187 selector evaluations, no lower factorization was found; the optimized
runs approached either the site or kinetic-eigenmode decomposition. This is
strong numerical evidence on the sampled landscape, not a proof of global
minimality.

## 5. Filling controls

The periodic selector landscape at its filling-dependent equal-endpoint
coupling was compared at eight identical Haar-random $W$ values for
$N=4,5,6,7,8$. Its normalized values agreed across all five fillings to
$7.0\times10^{-14}$. Endpoint Hessians show the same open-fail/periodic-pass
pattern at every tested filling.

| $N$ | Open site min. | Open kinetic min. | Periodic site min. | Periodic kinetic min. |
|---:|---:|---:|---:|---:|
| 4 | 0.1222246 | -0.0465275 | 0.4866810 | 0.2433405 |
| 5 | 0.1222246 | -0.0465274 | 0.4866810 | 0.2433404 |
| 6 | 0.1222246 | -0.0465275 | 0.4866810 | 0.2433403 |
| 7 | 0.1222245 | -0.0465276 | 0.4866810 | 0.2433404 |
| 8 | 0.1222246 | -0.0465274 | 0.4866810 | 0.2433405 |

The stationary spectrum depends on filling:

| $N$ | Sector dimension | Periodic $g_c$ | Ground multiplicity | Gap if isolated | Evidential status |
|---:|---:|---:|---:|---:|---|
| 4 | 495 | 0.4505635569 | 1 | 0.7800054 | passes |
| 5 | 792 | 0.4214636152 | 4 | n/a | degenerate |
| 6 | 924 | 0.4129483210 | 1 | 0.2033920 | passes |
| 7 | 792 | 0.4214636152 | 4 | n/a | degenerate |
| 8 | 495 | 0.4505635569 | 1 | 0.7800054 | passes |

The origin of the fourfold odd-sector degeneracy has not been proved and no
symmetry label is assigned here. Entropies of arbitrary vectors selected from
those degenerate spaces are excluded. The even sectors $N=4,6,8$ all have
isolated ground states and positive mode, local-number-SSR, and local-parity-SSR
contrasts.

For the open chain, the selector already fails because of the negative
kinetic-endpoint Hessian direction. Ground multiplicities for $N=4,5,6,7,8$
are respectively $1,4,3,4,1$.

## 6. Non-EC control

Replacing the axial contact by

$$
Q_{\mathrm{dens}}=\sum_x N_x(N_x-1)
$$

produces strict site and kinetic-basis endpoints at equal cost for both open
and periodic three-cell geometries. At $N=6$, the smallest endpoint Hessian
eigenvalues are 0.06063 for the open chain and 0.42160 for the periodic ring.
Twenty-four direct Haar samples found no lower cost. This repeats the v0.1.3
warning that competing finite selector branches are not specific evidence for
Einstein-Cartan dynamics.

## 7. Timing

On a 12-core Apple M4 Pro with 48 GB memory:

- geometry construction: approximately 0.02 seconds;
- Hamiltonian construction: approximately 0.03 seconds;
- the default run, including 12 Haar samples, four optimized random starts,
  24 iterations, filling Hessians, and non-EC controls: 78.7 seconds measured
  inside the calculation;
- the strengthened periodic search with 7,187 objective evaluations: 138.3
  seconds;
- peak fixed-sector matrices are approximately 13 MB each.

The computation is inexpensive. Implementation, validation, and interpretation
take substantially longer than matrix construction or diagonalization.

## 8. Classification

The three-cell result is a **boundary-independent robustness failure**, while
remaining boundary-sensitive rather than a complete algebraic no-go result:

1. The open-chain axial selector fails decisively on the enlarged candidate
   manifold.
2. The periodic axial selector passes only the predeclared restricted numerical
   gate and retains isolated positive-contrast states in all tested even
   fillings.
3. Odd-sector stationary states are degenerate and do not pass the isolated-
   state gate.
4. A non-EC density interaction also produces strict competing branches.

A four-cell or analytic large-size calculation would be needed to adjudicate
the open-versus-periodic and odd-lattice dependence. That was beyond this
three-cell calculation. The later four-cell gates linked above do not establish
a boundary-independent or large-size result, so the finite selector is not
promoted beyond this side branch. No change to the main ICC hypothesis follows.

## 9. Remaining limits

This gate does not test a complete symmetry-allowed quartic perturbation basis,
alternative selector norms, Bogoliubov transformations, an interaction
ensemble, arbitrary cell count, a continuum limit, or a dynamical transition.
The Hessians, searches, spectra, entropies, and Moore-Penrose projection are
evaluated numerically. The projection formula and integer Gram-rank certificate
are exact algebraic statements; their floating-point realization and the
internal numerical identities are verified only to the reported tolerances.

## 10. Reproduction

From the repository root:

```bash
python3 research/ec_three_cell_selector.py
```

For the strengthened periodic run:

```bash
python3 -c "import sys; sys.path.insert(0, 'research'); import ec_three_cell_selector as m; r=m.evaluate_boundary(True, 6, 32, 8, 80, 20260719); m.print_boundary(r)"
```
