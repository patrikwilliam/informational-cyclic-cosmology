# Four-Cell Boundary-Phase Robustness Gate

Date specified and completed: 7 August 2026

Status: completed internal numerical follow-up; not externally preregistered
and not independently peer reviewed. A deep mathematical review found and
corrected a branch-switching error in the first implementation. The correction
does not change the small-twist pass or the full-path failure, but it changes
the branch definition and the first failed grid point.

The phase grid, tolerances, and original primary rule were fixed locally before
the first scan. The original conditional coupling rule was specified after the
primary values were known. The explicit transported branch and analytic
residual reduction were introduced retrospectively during this review, after
the numerical outputs had been inspected. The corrected calculation is
therefore an exploratory internal result, not a prospective confirmation test.

Reproducible calculation:
[`ec_four_cell_boundary_phase.py`](./ec_four_cell_boundary_phase.py)

## 1. Question

The four-cell periodic ring passes the restricted finite selector gate, whereas
the open chain fails. Is the periodic result confined to the exact degeneracy at
zero boundary phase, or does the same periodic stationary branch remain a strict
local minimum after that degeneracy is split by a boundary twist?

This tests one finite selector. It is not a test of ICC, a continuum limit, or a
cosmological mechanism.

## 2. Twisted kinetic operator

The three interior links are unchanged and the closing link is

$$
K_{3,0}=-i e^{i\phi},\qquad K_{0,3}=i e^{-i\phi}.
$$

For $v_x=e^{ikx}$, the boundary condition is
$v_{x+4}=e^{i\phi}v_x$. Therefore

$$
k_m=\frac{\phi+2\pi m}{4},\qquad
\lambda_m(\phi)=2\sin k_m,\qquad m=0,1,2,3.
$$

The diagonal gauge

$$
G(\phi)=\operatorname{diag}
\left(1,e^{i\phi/4},e^{i\phi/2},e^{3i\phi/4}\right)
$$

distributes the closing-link phase uniformly:

$$
G(\phi)^\dagger K(\phi)G(\phi)
$$

has forward links $-i e^{i\phi/4}$ and their Hermitian conjugates.

The fixed scan is

$$
\phi_j=\frac{j\pi}{16},\qquad j=0,1,\ldots,16.
$$

The script rejects any other subdivision count for the declared gate.

## 3. Fixed ingredients

The calculation retains:

- four cells, four Dirac modes per cell, and the half-filled $N=8$ sector;
- the onsite normal-ordered axial-current contact interaction;
- the centered fixed-sector Hilbert-Schmidt interaction projection;
- the number-preserving $U(4)/(U(1)^4\rtimes S_4)$ candidate family;
- all 12 physical off-diagonal tangent directions;
- stationarity tolerance $10^{-7}$ and strict-curvature threshold
  $2\times10^{-5}$; and
- fixed periodic coupling $g_0=0.4298279138553384$ in the primary scan.

The global Hamiltonian is not retuned while $\phi$ changes.

## 4. Branch definition and review correction

Let $U_0$ be the resolved strict periodic representative selected within the
two-dimensional zero eigenspace at $\phi=0$. The branch tested here is now
defined explicitly by

$$
U_\phi=G(\phi)U_0.
$$

This supplies one smooth, gauge-covariant representative for every $\phi$ and
removes ambiguity about which optimization basin is being followed. Consecutive
grid representatives have phase/permutation-matched overlap
$0.9972919524$; their overlap with the site decomposition is $0.375$.

The first implementation instead minimized from the preceding point and from
an exact kinetic seed, then preferred any strict candidate before comparing
overlap. At $\phi=\pi/2$, minimization from the preceding branch moved away from
the now-unstable stationary point, while the selection rule substituted a
different strict kinetic-basis minimum with overlap only $0.7479$ to the
preceding representative. That output was not a continuation of the periodic
branch. It caused the first failed point to be reported incorrectly as
$11\pi/16$.

The corrected calculation evaluates stationarity and curvature directly at
$U_\phi$. It never substitutes another minimum when this branch becomes a
saddle.

## 5. Gate definitions

A branch passes a phase point only if:

1. its gradient norm is below $10^{-7}$ at every one of the four finite-
   difference steps;
2. its minimum Hessian eigenvalue exceeds $2\times10^{-5}$ at every step; and
3. it remains distinct from the other branch under the quotient-overlap test.

The **small-twist three-point gate** passes only if both branches pass at

$$
\phi=0,\quad \frac{\pi}{16},\quad \frac{\pi}{8}.
$$

This is a discrete numerical gate. By itself it is not an interval-arithmetic
proof for every phase between the tested points. The **full
periodic-to-antiperiodic gate** requires both branches to pass all 17 points.

## 6. Analytic residual reduction

For a fixed decomposition $U$, write the unnormalized residual polynomial as

$$
R_U(g)=A_U+2gC_U+g^2B_U.
$$

The normalized selector is $R_U(g)/D(g)$, where the invariant denominator
$D(g)$ is common to all decompositions. Direct evaluation on the two explicit
branches gives, up to a maximum raw numerical error below
$4.7\times10^{-10}$,

$$
(A_{\rm site},B_{\rm site},C_{\rm site})=(109824,0,0),
$$

and

$$
(A_\phi,B_\phi,C_\phi)=
\left(109824\sin^2\frac{\phi}{4},594440,0\right).
$$

Consequently, at fixed $g_0$,

$$
F_\phi(g_0)=F_0(g_0)
\left(1+\sin^2\frac{\phi}{4}\right),
$$

and equal branch costs occur at the positive root

$$
g_*(\phi)=g_0\cos\frac{\phi}{4}.
$$

This replaces the original optimizer-dependent coupling bisection. The two
reported roots are solutions of an explicit quadratic and have nonzero crossing
slopes.

## 7. Validation

| Check | Maximum error |
|---|---:|
| $\phi=0$ against the original periodic matrix | 0 |
| $\phi=2\pi$ closure against $\phi=0$ | $2.45\times10^{-16}$ |
| Exact spectrum formula at five phases | $1.03\times10^{-15}$ |
| Distributed-gauge identity at five phases | $1.57\times10^{-16}$ |
| Direct fixed-sector kinetic reconstruction | 0 |
| Direct fixed-sector contact reconstruction | 0 |
| Analytic residual and cost identities, full grid | $4.66\times10^{-10}$ |

An optional independent sparse audit at $L=4,N=8$ compares the combinatorial
partial-trace formula directly with occupation-mask actions for a seeded random
decomposition at $\phi=\pi/16$. It gives local-overlap error
$1.89\times10^{-11}$, zero displayed sector-norm discrepancy, and trace error
$2.91\times10^{-10}$ on a trace of magnitude approximately $4.13\times10^4$.
It does not construct the dense $12{,}870\times12{,}870$ matrix.

## 8. Primary fixed-coupling result

The site branch has constant cost $0.4586065963$, zero displayed gradient, and
minimum Hessian approximately $0.177740$ throughout. The transported periodic
branch is stationary at every grid point, with maximum audited gradient below
$1.17\times10^{-11}$.

| $\phi/\pi$ | Transported-branch cost | Minimum Hessian | Point gate |
|---:|---:|---:|:---:|
| 0 | 0.45860660 | 0.122137 | pass |
| 0.0625 | 0.45971075 | 0.119538 | pass |
| 0.1250 | 0.46301259 | 0.111885 | pass |
| 0.1875 | 0.46848032 | 0.099573 | pass |
| 0.2500 | 0.47606127 | 0.083172 | pass |
| 0.3125 | 0.48568244 | 0.063328 | pass |
| 0.3750 | 0.49725117 | 0.040700 | pass |
| 0.4375 | 0.51065605 | 0.015917 | pass |
| 0.5000 | 0.52576798 | **-0.010441** | **fail** |
| 0.5625 | 0.54244142 | -0.063502 | fail |
| 0.6250 | 0.56051581 | -0.135800 | fail |
| 0.6875 | 0.57981707 | -0.213005 | fail |
| 0.7500 | 0.60015932 | -0.294374 | fail |
| 0.8125 | 0.62134666 | -0.379123 | fail |
| 0.8750 | 0.64317504 | -0.466436 | fail |
| 0.9375 | 0.66543424 | -0.555473 | fail |
| 1.0000 | 0.68790989 | -0.645376 | fail |

Thus the small-twist three-point gate passes and the full gate fails. The first
failed prescribed point is $\phi=\pi/2$. A post-review 12-step bisection of the
$5\times10^{-4}$ numerical Hessian brackets a sign-changing zero in

$$
0.4756011963 < \frac{\phi_c}{\pi} < 0.4756164551.
$$

The endpoint Hessian values of that bracket are approximately
$9.71\times10^{-7}$ and $-5.50\times10^{-6}$. This is a numerical location, not
an interval-certified theorem.

## 9. Conditional coexistence result

At the two nonzero phases in the small-twist gate, the analytic positive roots
are audited again on the full 12-dimensional quotient tangent space:

| $\phi/\pi$ | $g_*(\phi)$ | Common cost | Hessian minima | Matched overlap |
|---:|---:|---:|---:|---:|
| 0.0625 | 0.4293101673 | 0.4592051604 | 0.175332, 0.120501 | 0.375000 |
| 0.1250 | 0.4277581750 | 0.4610044470 | 0.168094, 0.115664 | 0.375000 |

The raw quadratic residuals are $-1.46\times10^{-11}$ and the crossing slopes
are approximately $-5.10\times10^5$ and $-5.09\times10^5$. Both pairs remain
stationary and strict at the roots.

For each phase, 24 seeded Haar samples and descents from the four lowest samples
find no value below the two branches. The lowest direct values are 0.73266013
and 0.65280473; the lowest optimized values equal the branch cost to printed
precision. This is finite search evidence, not a global-minimum proof.

## 10. Classification

The calculation supports this narrow statement:

> In the specified $L=4,N=8$ selector, the explicitly transported periodic
> branch remains a numerically strict local minimum at the first two nonzero
> twists, after the periodic zero pair has split. Its residual polynomial yields
> nearby analytic coexistence roots. The same branch loses positive curvature
> near $\phi/\pi\simeq0.4756$, so full periodic-to-antiperiodic robustness fails.

This disfavors the explanation that the periodic pass is solely an arbitrary
basis choice inside the exact zero eigenspace. It does not prove a continuous
interval by certified numerics, a global minimum, EC specificity, persistence
with lattice size, or a continuum/cosmological selector. The naive derivative,
fixed filling, imposed norm, and tuned coexistence remain unresolved modeling
choices.

Because the periodic representative is numerically nondegenerate and the
finite objective is smooth, some sufficiently small continuation is already
the expected implicit-function-theorem behavior. The scan measures a finite
stability range and its later failure; it is not independent evidence for a new
selection mechanism.

## 11. Reproduction

Complete corrected scan, approximately 2.2 minutes on the reported 12-core
Apple M4 Pro:

```bash
/Users/pwp/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 research/ec_four_cell_boundary_phase.py
```

Three-point gate, analytic coexistence roots, and finite landscape searches,
approximately 1.7 minutes:

```bash
/Users/pwp/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 research/ec_four_cell_boundary_phase.py --max-index 2 --conditional
```

Optional sparse $N=8$ audit:

```bash
/Users/pwp/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 research/ec_four_cell_boundary_phase.py --max-index 0 --deep-validation
```

Optional curvature-zero diagnostic:

```bash
/Users/pwp/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 research/ec_four_cell_boundary_phase.py --max-index 0 --curvature-root
```

Independent internal reviews:

- [`four-cell-boundary-phase-mathematical-review.md`](../feedback/four-cell-boundary-phase-mathematical-review.md)
- [`four-cell-boundary-phase-physics-review.md`](../feedback/four-cell-boundary-phase-physics-review.md)
