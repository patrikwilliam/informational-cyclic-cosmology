# Measurement Capability After Reference Redistribution

Study: 15 October 2026. Integrated into v0.1.8 on 16 October 2026.

## Answer

**Yes, the attainable measurement set genuinely changes in the declared finite
access model; the earlier decrease is not solely a poor choice of readout.**
Part of that decrease IS recoverable by improving the protocol. But the
original readout's before-priming success, 0.7197744539, exceeds even the
after-priming ceiling for ALL charge-symmetric measurements on the fresh input
plus retained detector and memory, 0.6813596618.

This is conditional on having one copy of the retained apparatus, no accessible
old input or extra phase reference, and the stated symmetry constraint. If the
old input remains coherently accessible, the full symmetry-allowed measurement
set is unchanged by the global unitary. The result concerns physical access,
not information destruction, a changing global algebra, or an ICC transition.

This extends the [existing three-qubit model](../three-qubit-memory/README.md)
without changing its Hamiltonian or priming state. It adds an analytic
operational bound, not more dynamical qubits or an ontology. Appendix C in the
main paper summarizes this result. The separate [Lean scope](../lean/README.md)
identifies the formally checked components and the remaining analytic bridges.

## 1. Fix the Operational Assumptions

Use the same S (fresh test input), D (finite reference/detector) and charge-neutral
M (memory). Set n = (I-Z)/2 and

$$
H=\frac12(X_SX_D+Y_SY_D)+n_DX_M,\quad Q=n_S+n_D,\quad T=\frac\pi4.
$$

Let R = DM, Q_R = n_D tensor I_M, tau_0 = |+><+|_D tensor |0><0|_M and

$$
\tau_1=\Phi(\tau_0),\qquad
\Phi(\tau)=\operatorname{Tr}_{S_{\rm old}}
\left[U_T\left(\frac{I_{S_{\rm old}}}{2}\otimes\tau\right)U_T^\dagger\right].
$$

Priming remains UNREAD: no intermediate population readout, reset, pulse, or
postselection is added. DM correlations are retained. A new uncorrelated input
is supplied after the old input ceases to be accessible. This restriction is
supplied, not dynamically derived. The mixed priming input has no accessible
preparation label or purification. No coherent training probes, repeated copies
of the unknown test input, fresh asymmetric ancillas, or refreshed reference
states are granted. Each trial uses one apparatus state and one unknown input.

For the broad benchmark, allow every joint binary effect E satisfying

$$
0\le E\le I,\qquad [E,n_S+Q_R]=0.
$$

The induced effect F_tau(E) is defined by

$$
\operatorname{Tr}[\rho_S F_\tau(E)]
=\operatorname{Tr}[(\rho_S\otimes\tau_R)E],\qquad
\mathcal C_{\rm sym}(\tau)=\{F_\tau(E):0\le E\le I,\ [E,n_S+Q_R]=0\}.
$$

**Exactly the same class is used before and after.** It is a generous
symmetry-allowed upper envelope, not a claim that the fixed hardware can
implement every member. Symmetric processing with invariant ancillary states
and invariant outcome readout is covered at the effective-POVM level. Arbitrary
external phase references are not. Classical processing and all outcomes of a
protocol are included; success conditional on discarded failures is not the
figure of merit.

The original measurement U_t^dagger n_D U_t belongs to this class. Therefore
an upper bound on this broader class bounds every original-hardware protocol
that stays within the same resource and symmetry restrictions.

## 2. An Exact Optimum, Not a Parameter Search

Use the equal-prior inputs rho_+ = (I+Y)/2 and rho_- = (I-Y)/2. Their label is
unknown to the detector; the phase convention is calibrated relative to the
initial reference. The preparator is not an additional accessible resource.

Let G be the twirl over the total charge, equivalently deletion of matrix
elements connecting distinct charge sectors. Symmetric measurements cannot
distinguish an operator from its twirl. Helstrom optimization therefore gives

$$
p_{\rm sym}^{\star}(\tau)
=\frac12+\frac14\left\|\mathcal G(Y\otimes\tau)\right\|_1.
$$

Write the apparatus state in D-charge blocks, with each entry an operator on M:

$$
\tau=\begin{pmatrix}A&B\\B^\dagger&C\end{pmatrix}.
$$

Only the total-charge-one sector contributes to the twirled difference. In
the order (|0>_S|1>_D, |1>_S|0>_D), its nonzero block is

$$
\begin{pmatrix}0&-iB^\dagger\\iB&0\end{pmatrix}.
$$

Its eigenvalues are the positive and negative singular values of B. Hence

$$
\boxed{p_{\rm sym}^{\star}(\tau)=\frac12+\frac12\|B\|_1.}
$$

The positive spectral effect, with any valid choice on the kernel, attains
this optimum and commutes with total charge. It is an exact optimum within
the benchmark, not an upper bound guessed from a numerical search.
Equivalently every attainable system effect satisfies

$$
|[F_\tau(E)]_{01}|\le\frac12\|B\|_1,
$$

and this transverse bound is attainable. This does NOT characterize the entire
effect set from one scalar: longitudinal and bias constraints also matter.

## 3. Evaluate the Same Priming Interaction

For general real couplings g,k in the preceding model, define
Omega = sqrt(g^2+k^2/4), alpha = k/(2 Omega), beta = g/Omega,
s = sin(Omega T), c = cos(Omega T), delta = kT/2, and u = beta^2 s^2.
The primary values are still g = k = 1 and T = pi/4; zero couplings are
interpreted by continuity.

The initial charge-coherence block is B_0 = |0><0|_M/2, so ||B_0||_1 = 1/2.
For the primed apparatus, direct block evolution gives

$$
\|B_1\|_1=\frac12\sqrt{c^2+\alpha^2s^2}
=\frac12\sqrt{1-u},\qquad
p_{\rm sym}^{\star}(\tau_1)=\frac12+\frac14\sqrt{1-u}.
$$

For a short derivation, let P = |0><0|_M,
D = exp(-i delta X)(cI+i alpha sX), and W = exp(-2i delta X).
The actual off-diagonal charge block obeys

$$
B_1W=\frac14(PD+DP)
=\frac14\begin{pmatrix}2d_0&i d_1\\i d_1&0\end{pmatrix},
$$

where d_0 = c cos(delta)+alpha s sin(delta) and
d_1 = alpha s cos(delta)-c sin(delta). Unitary multiplication by W does not
change singular values. The identity ||K||_1^2 = Tr(K K^dagger)+2|det K| for a
2x2 matrix gives ||B_1||_1 = sqrt(d_0^2+d_1^2)/2, proving the formula.

Numerically ||B_1||_1 = 0.3627193236. The results are:

| Fixed access/control specification | Before priming | After priming |
| --- | ---: | ---: |
| Original H, n_D readout, duration T | 0.7197744539 | 0.5341235815 |
| Same H and n_D, best exposure duration permitted in both cases | 0.7236067977 | 0.6731277438 |
| All Q-symmetric measurements on fresh S plus DM | 0.7500000000 | 0.6813596618 |
| All Q-symmetric measurements on fresh S plus D only | 0.7500000000 | 0.6145758693 |
| Old input also retained; all Q-symmetric joint measurements | 0.7500000000 | 0.7500000000 |
| Unrestricted direct system measurement, abandoning Q restriction | 1.0000000000 | 1.0000000000 |

The D-only row excludes M from operations, not merely its marginal readout;
it is a different fixed access specification, applied equally before and after.
The difference from the DM row demonstrates useful retained correlations.
The maximally mixed-memory control has the SAME optimal phase-discrimination
score as the pure-memory case. This single-score equality does not assert
equality of their full measurement sets.

### Exact Duration Optimization

No new Hamiltonian pulses or pointer axes are granted. If arbitrary exposure
time t is allowed equally before and after, put
a = c cos(delta)-alpha s sin(delta), b = c sin(delta)+alpha s cos(delta),
and d = alpha b, using the fixed PRIMING time T in these quantities.
The subsequent-readout Y coefficient is

$$
y_{\rm after}(t)=\frac\beta4
\left[a\sin(2\Omega t)+d\cos(2\Omega t)-d\right].
$$

For the primary positive couplings,

$$
\max_t p_{\rm before}(t)=\frac12+\frac\beta4,\qquad
\max_t p_{\rm after}(t)=\frac12+\frac\beta4(\sqrt{a^2+d^2}+|d|).
$$

The maxima follow from the amplitude of one sinusoid and are attained. At the
primary setting one choice of optimal times is 0.7024814731 before and
1.8830035917 after. Relabeling the binary outcome is permitted in both cases.
Randomization over times cannot improve this linear discrimination objective.
This is an optional enlargement of the original fixed-duration menu, not an
autonomous clock construction or a search for favorable couplings.

## 4. A Genuine Measurement-Set Separation

The before-priming hardware effect F_0 has |(F_0)_01| = 0.2197744539.
Every after-priming symmetric effect has |F_01| <= 0.1813596618. Thus

$$
F_0\notin\mathcal C_{\rm sym}(\tau_1),\qquad
\inf_{F\in\mathcal C_{\rm sym}(\tau_1)}\|F_0-F\|_{\rm op}
\ge 0.0384147921.
$$

F_0 is actually implemented by the original hardware before priming, not only
postulated available by the broad benchmark. Therefore any unchanged hardware
class containing that original protocol and lying inside the symmetric class
cannot have identical before/after attainable sets. This does not assert that
the smaller hardware sets are nested.

For the FULL symmetric benchmark, more can be established. Phi is a CPTP
covariant channel because the priming input I/2 is invariant and U conserves
total charge. For any allowed after effect E, define

$$
E'=(\operatorname{id}_S\otimes\Phi^*)(E).
$$

The adjoint is unital and completely positive, so E' is a valid effect;
covariance ensures it is invariant. Moreover
Tr[(rho tensor tau_0) E'] = Tr[(rho tensor tau_1) E] for every input rho.
The same construction preserves the sum of a finite POVM's effects. Hence

$$
\boxed{\mathcal C_{\rm sym}(\tau_1)\subsetneq\mathcal C_{\rm sym}(\tau_0)}
$$

at the primary setting. Inclusion is proved by the channel dual, not inferred
from random sampling. Strictness follows from the discrimination witness.

This is a QUANTITATIVE capability change, not a different underlying observable
algebra. Since B_0 and B_1 are both nonzero, each benchmark set contains
nontrivial transverse effects in both phase directions as well as sharp
diagonal effects. Each spans the same full qubit matrix algebra M_2. Taking
that linear span does not grant sharp measurements of all its elements.

## 5. What Makes the Conclusion Conditional

If the old input remains accessible, its initial and final joint apparatus
states are related by the charge-conserving unitary U, not the reduced channel
Phi. Conjugating ANY joint effect by I_fresh tensor U maps invariant effects
bijectively between the two descriptions. Thus the full symmetric measurement
sets are equal, not merely their scores on this one task. Physical access to
all such joint effects or inverse operations is still a benchmark assumption,
not a demonstrated feature of the fixed original hardware.

Similarly, without the Q restriction the direct Y measurement distinguishes
the test inputs perfectly before and after, independently of the reference.

The result therefore establishes a change of SINGLE-COPY accessible measurement
capability relative to fixed resources and symmetry. It does not establish
irreversible global loss, a different Hilbert-space factorization, an entropy
reset, new spacetime dimensions, or a cosmological aeon. The missing physical
input remains why particular degrees of freedom and controls are accessible
or inaccessible in an ICC application. Declaring the old input inaccessible
is not a derivation of that boundary.

## Reproduction and Sources

[checks.py](checks.py) imports the previous model read-only and records both
source hashes in [checks-results.json](checks-results.json). It checks exact
Helstrom attainment, arbitrary-input Born identities, the charge-block formula,
constructive effect-set inclusion, analytic duration optimization, and the
retained-resource control. Run `python3 -B checks.py` with NumPy, optionally
adding `--output PATH`. The [math review](mathematical-review.md) and
[physics review](physics-review.md) are separate internal AI-assisted passes,
not independent expert review. They predate the scoped Lean supplement;
the numerical checks themselves are not Lean proofs.

- [Marvian and Spekkens, arXiv:1212.3378](https://arxiv.org/abs/1212.3378):
  asymmetric reference resources and symmetric measurement processing.
- [Bartlett, Rudolph and Spekkens, arXiv:quant-ph/0610030](https://arxiv.org/abs/quant-ph/0610030):
  reference frames, operational symmetry restrictions, and relational encodings.
- [Bartlett et al., arXiv:quant-ph/0602069](https://arxiv.org/abs/quant-ph/0602069):
  finite-reference degradation and operational measurement quality.
- [Barnett and Croke, arXiv:0810.1970, Section 3.1](https://arxiv.org/abs/0810.1970):
  minimum-error discrimination and spectral optimization.

These sources were checked on 15 October 2026. The specific finite formulas
above are derived here for the existing illustrative model; no claim is made
that this calculation or its principles are novel, or that the sources support
ICC. No unverified AI-generated theorem is a dependency of this calculation.
