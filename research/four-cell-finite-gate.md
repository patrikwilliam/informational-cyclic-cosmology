# Four-Cell Finite Selector Gate

Date: 7 August 2026

Status: completed exploratory follow-up; numerical and not independently peer
reviewed. This is a finite-size stress test of the restricted
Einstein-Cartan-inspired CAR selector, not a test of the main ICC proposal.

Reproducible calculation:
[`ec_four_cell_selector.py`](./ec_four_cell_selector.py)

## 1. Question

Does the boundary-sensitive branch found at three cells survive at four cells
without choosing a successful filling, boundary condition, kinetic basis, or
factorization after inspecting the selector landscape?

The four-cell gate uses:

- four cells and four Dirac modes per cell;
- the half-filled sector $N=8$;
- open and periodic nearest-neighbour kinetic terms;
- all number-preserving cell transformations $W\in U(4)$ that preserve the
  common internal Dirac factor, modulo column phases and permutations;
- the same centered fixed-sector Hilbert-Schmidt projection onto sums of
  one-cell, local-number-preserving Hamiltonians;
- the same onsite axial-current contact interaction as the two- and three-cell
  calculations;
- equal selector cost at the site and kinetic branches, with the coupling fixed
  before searches away from those branches;
- all 12 physical off-diagonal tangent directions on
  $U(4)/(U(1)^4\rtimes S_4)$;
- phase/permutation invariance, random sampling, and multi-start descent if the
  endpoint tests pass.

The calculation proceeds in gates. A failed implementation audit stops the
calculation. A nonstationary or non-minimal endpoint, an unremoved continuous
degeneracy, a negative Hessian direction at a stationary endpoint, or a lower
mixed factorization fails that boundary condition. Endpoint stationarity is
tested at gradient-norm tolerance $10^{-7}$. Failure for either open or
periodic geometry is a
boundary-independent robustness failure for this finite selector. Passing both
would justify further finite controls, not a continuum or cosmological claim.

This gate was fixed locally before evaluating the four-cell selector but was
not externally preregistered.

## 2. Periodic zero-mode rule

For four periodic cells, the one-particle cell kinetic spectrum is

$$
(-2,0,0,2).
$$

Consequently, diagonalizing the kinetic matrix does not define a unique
factorization. Its zero eigenspace carries an exact $U(2)$ freedom. The periodic
kinetic branch is therefore defined in two stages:

1. minimize the contact residual over the full zero-eigenspace $U(2)$ family,
   modulo phases and permutations, using a deterministic sphere scan followed
   by local refinement;
2. test the selected representative in all 12 physical tangent directions of
   the full $U(4)$ candidate manifold.

The equal-endpoint coupling is then computed from that selected kinetic-family
minimum. If the contact residual remains continuously degenerate, the minimum
depends on an arbitrary basis convention, or no strict representative exists,
the periodic branch fails the strict-selector gate. An arbitrary basis returned
by numerical diagonalization is not admissible evidence.

## 3. Memory-efficient formulation

At half filling,

$$
\mathcal H_{4,8}=\bigwedge^8\mathbb C^{16},
\qquad
\dim\mathcal H_{4,8}=\binom{16}{8}=12{,}870.
$$

Dense fixed-sector matrices are therefore excluded. The implementation
represents the Hamiltonian by its one-body matrix $h$ and a matrix $V$ acting on
the antisymmetric two-particle space $\bigwedge^2\mathbb C^{16}$. Under
$U=W\otimes I_4$,

$$
h\mapsto U^\dagger hU,
\qquad
V\mapsto \Gamma_2(U)^\dagger V\Gamma_2(U).
$$

The overlaps with the 280 labelled one-cell matrix units are evaluated by
fixed-number partial-trace identities. Their $280\times280$ Gram matrix is the
same exact combinatorial Gram construction used at three cells. Full-sector
Hilbert-Schmidt norms are computed once from sparse one- and two-body actions
and are invariant under $W$.

Before any four-cell result is accepted, this low-body implementation must
reproduce dense $L=2$ and $L=3$ residual components at endpoints and seeded
Haar-random factorizations to numerical tolerance. Failure of that comparison
invalidates the implementation rather than the physical selector.

## 4. Validation

The low-body implementation was compared with separately evaluated dense
fixed-sector matrices before the half-filled result was evaluated.

| Case | Hamiltonian reconstruction | Exterior lift | Local overlaps | Residual components | Sector norms |
|---|---:|---:|---:|---:|---:|
| $L=2,N=4$, open | 0 | $1.14\times10^{-16}$ | $1.43\times10^{-14}$ | $9.10\times10^{-13}$ | 0 |
| $L=3,N=6$, open | 0 | $1.24\times10^{-16}$ | $2.27\times10^{-13}$ | $1.82\times10^{-10}$ | 0 |
| $L=3,N=6$, periodic | 0 | $1.24\times10^{-16}$ | $9.10\times10^{-13}$ | $1.66\times10^{-9}$ | 0 |
| $L=4,N=3$, open | 0 | $2.33\times10^{-16}$ | $8.53\times10^{-14}$ | $1.93\times10^{-11}$ | 0 |
| $L=4,N=3$, periodic | 0 | $1.39\times10^{-16}$ | $5.69\times10^{-14}$ | $1.46\times10^{-11}$ | 0 |

A separate generic random Hermitian one-plus-two-body operator on $L=4,N=3$
gives local-overlap error $2.84\times10^{-14}$, zero trace discrepancy, zero
Hermiticity discrepancy, and absolute sector-norm discrepancy
$1.54\times10^{-9}$. This checks coefficient patterns beyond the structured
kinetic/contact orbit.

There are 280 labelled one-cell matrix-unit generators. Three exact relations
identify the four copies of the sector identity, and
$N_1+N_2+N_3+N_4=8I$ supplies a fourth. The integer Gram matrix annihilates all
four relations exactly. Row reduction modulo $1{,}000{,}003$ gives rank 276;
the modular lower bound and four rational relations certify that the rank over
$\mathbb Q$ is exactly 276.

Generic right multiplication by column phases or permutations changes the
normalized selector by no more than $3.4\times10^{-16}$ in the reported runs.

## 5. Four-cell result

| Quantity | Open chain | Periodic ring |
|---|---:|---:|
| Kinetic spectrum | $(-1.618,-0.618,0.618,1.618)$ | $(-2,0,0,2)$ |
| Equal-endpoint coupling $g_c$ | 0.3584858648 | 0.4298279139 |
| Normalized endpoint cost | 0.4773544741 | 0.4586065963 |
| Site gradient norm | 0 | 0 |
| Kinetic-branch gradient norm | **0.06136680** | $4.93\times10^{-12}$ |
| Minimum site Hessian eigenvalue | **-0.02949084** | 0.17773973 |
| Minimum kinetic chart-curvature eigenvalue | -0.00352795 | 0.12213664 |
| Lowest cost found | **0.47318959** | 0.45860660 |
| Endpoint gate | fail | pass |
| Sampled landscape gate | fail | pass |

For the open chain, the site branch is stationary and has a negative Hessian
direction on the full restricted $U(4)$ candidate manifold. At chart steps
$2\times10^{-3}$, $10^{-3}$, $5\times10^{-4}$, and $2.5\times10^{-4}$, its
minimum eigenvalue remains between -0.02949085 and -0.02949084. A direct step
along the negative eigenvector lowers the selector, and subsequent descent
reaches 0.47621311.

The open kinetic branch is not stationary. Its gradient norm remains between
0.06136674 and 0.06136681 over the same four steps. A normalized negative-
gradient step lowers the cost directly to 0.47452009. An additional search
initialized along a negative chart-curvature direction reaches 0.47318959.
Because the gradient is nonzero, the reported -0.00352795 chart-curvature
eigenvalue is not interpreted as an intrinsic Hessian or used to call this
endpoint a saddle. Nonstationarity alone certifies failure.

For the periodic ring, the deterministic $25\times48$ zero-family scan gives
contact-selector values from 0.84717184 to 0.94013343. Local refinement followed
by one Newton correction reaches 0.8470856742, with zero-family gradient norm
$8.8\times10^{-12}$ and two-direction minimum Hessian eigenvalue 0.50210660.
This removes the arbitrary eigensolver basis before fixing $g_c$. The resulting
full 12-direction gradient norm is $4.9\times10^{-12}$. Both full-manifold
endpoints are stationary and strict in all tested tangent directions. Their
minimum Hessian eigenvalues remain in the ranges 0.17773917 to 0.17773976 and
0.12213594 to 0.12213669 over the four chart steps.

For the passing periodic boundary, the default 24 seeded Haar samples and four
descents from the lowest sampled starts find no lower point. The lowest direct
random value is 0.61315703, and all optimized values remain above the endpoint.
A post-review strengthened search uses 64 Haar samples and optimizes the eight
lowest starts for up to 100 iterations. Its lowest direct value is 0.58483497
and its lowest optimized value is 0.4586065991, compared with endpoint
0.4586065963. Several descents have not reached the gradient tolerance, so this
is sampled numerical evidence and not a global-minimum proof.

## 6. Classification

The result is a **failure of boundary-independent robustness for this finite
selector**, not a no-go theorem for ICC or for all periodic selectors:

1. The open-chain two-branch landscape fails more strongly than at three cells:
   the site endpoint is a saddle and the kinetic endpoint is not stationary.
2. The periodic selector passes its restricted $L=4,N=8$ endpoint and sampled
   landscape gates after the zero-mode ambiguity is removed.
3. The same open-fail/periodic-pass dependence now occurs at both three and four
   cells. Increasing the lattice once therefore does not remove the boundary
   sensitivity.
4. A periodic-only research branch remains logically possible if compact
   topology and this lattice discretization are justified independently and in
   advance. The present calculation supplies neither justification.

According to the predeclared rule, the boundary-independent finite selector is
not advanced to state diagnostics or promoted into the main ICC mechanism.
This does not modify the core ICC hypothesis.

## 7. Deferred diagnostics

Ground-state gaps, entropy contrasts, filling controls, non-EC controls, and
broader perturbation ensembles were deferred because both boundary selectors
did not survive. This ordering prevents an already-failed selector from
accumulating irrelevant positive diagnostics.

## 8. Remaining limits

The calculation does not test a complete symmetry-allowed quartic perturbation
basis, alternative selector norms, Bogoliubov transformations, arbitrary cell
count, a continuum limit, AQFT local algebras, a dynamical transition, or
cosmology. The periodic global minimum is not proved. The naive periodic
nearest-neighbour derivative also has two zero modes at even lattice size, so
its relation to a continuum fermion discretization requires separate analysis.

No four-cell outcome changes the main ICC hypothesis by itself. This failure
retires the boundary-independent version of this particular finite
Einstein-Cartan-inspired selector as presently defined. It does not establish a
general no-go theorem for factorization selectors.

## 9. Timing and reproduction

On a 12-core Apple M4 Pro with 48 GB memory, the complete default run takes
approximately 30 seconds and never constructs a dense $12{,}870\times12{,}870$
matrix. From the repository root:

```bash
/Users/pwp/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 research/ec_four_cell_selector.py
```

For the strengthened post-review periodic search:

```bash
/Users/pwp/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 research/ec_four_cell_selector.py --random-samples 64 --optimized-starts 8 --max-iterations 100 --seed 2026080712
```

The explicit interpreter path selects the bundled NumPy environment used for
the reported run. Any Python environment with a recent NumPy installation may
be used instead.
