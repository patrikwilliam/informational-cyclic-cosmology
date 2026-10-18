# Operational Stability of the Conditional Arithmetic Reconstruction

Version 0.1.7, 10 October 2026. Bounded, AI-assisted supplement for Appendix B.4.
No physical selector or cosmological transition is obtained.

## Result in Brief

A fixed spectral access window removes the previous high-index phase-flip
counterexample. It does **not** make the reference-to-algebra reconstruction
uniformly continuous over all full-support references with a fixed mean-energy
budget. An arbitrarily small amplitude at an accessible energy level suffices
for a new counterexample, detected by two fixed, finite-energy preparations.

Conversely, for each fixed full-support reference and fixed finite window,
the reconstruction is locally continuous. A certified amplitude floor gives
an explicit conditioning bound. These are compatible statements, not a
contradiction and not a no-go theorem for ICC.

The exact effect-set distance and reference sequence below are analytic
results. Lean checks the infinite-dimensional measurement witness, its
validity, the two-probe lower bound, and the scalar phase estimate; it does
**not** yet check the entire reference-to-effect-set theorem end to end.

## 1. Inputs and Operational Meaning

Use the conditional reconstruction in
[arithmetic-reconstruction.md](./arithmetic-reconstruction.md):

\[
\mathcal H=\ell^2(\mathbb N_{>0}),\qquad
H|n\rangle=\log n\,|n\rangle,\qquad S|n\rangle=|2n\rangle.
\]

Write \(n=2^k(2r+1)\), with \(k,r\ge0\). For the doubling algebra,

\[
\mathcal A=W^*(S)=\mathcal B(\ell^2(\mathbb N_0))\otimes I.
\]

For a normalized reference \(c\) with every \(c_n\ne0\), put

\[
D_c|n\rangle=\frac{c_n}{|c_n|}|n\rangle,\qquad
\mathcal A_c=D_c\mathcal A D_c^*.
\]

The polar reconstruction establishing this formula is an analytic dependency
from the existing note, not a new Lean-verified theorem. The Hamiltonian,
reference preparation, and compatible multiplication structure remain
supplied model inputs. Studying their conditioning does not independently
motivate them physically.

Fix \(P_N=\sum_{n=1}^N|n\rangle\langle n|\), independently of reference phases.
The primary diagnostic uses \(N=6\); \(N=12\) is a boundary control, not a fit.
The integer labels and this illustrative cutoff are features of the supplied
model, not an experimentally derived ICC access prescription.

Allow all test-state preparations supported on \(P_N\mathcal H\). A calibrated
external phase standard and coherent preparation control are assumed.
The candidate measurement sets are exactly the compressed effects defined
below; external preparation/calibration resources do not enlarge those sets.
This is an external testing convention, not the full accessible algebra of a
laboratory with unrestricted control. Freely adding arbitrary binary
measurements to both candidate sets would make them identical.
Preparation control need not conserve \(H\); time, work, and precision costs
are not bounded here. Reference preparation is separate from test-state
preparation: references may have infinite support but must satisfy
\(\langle H\rangle\le2\). No measurement back-action or leakage guarantee is
implied by compression. This metric compares ideal effects, not a procedure
turning an unknown supplied quantum reference into implemented measurements.

Define

\[
\mathcal E_N(\mathcal A_c)=
\{P_NaP_N:a\in\mathcal A_c,\ 0\le a\le I\},\qquad
d_N(\mathcal A_c,\mathcal A_d)=
d_{\mathrm H}^{\|\cdot\|}(\mathcal E_N(\mathcal A_c),\mathcal E_N(\mathcal A_d)).
\]

For self-adjoint compressed effects, their operator-norm difference is the
largest absolute probability difference over the permitted test states.
Hausdorff distance asks whether **each measurement** can be approximated by a
measurement in the other set. It is not the success probability or resource
cost of identifying an unknown algebra, and not a channel/diamond norm.
The compressed effect set need not be an algebra. This defines a pseudometric
on full represented algebras: different algebras can have identical compressed
effect sets.

Every effect set contains \(P_N/2\), and every compressed effect is at distance
at most \(1/2\) from that midpoint. Consequently

\[
0\le d_N\le\tfrac12.
\]

This normalization differs from the previous unit-ball algebra metric, whose
counterexample had distance 1.

## 2. What the Cutoff Removes

Let \(D_j=I-2|j\rangle\langle j|\). If \(j>N\), then \(P_ND_j=P_N\), so

\[
P_ND_jaD_jP_N=P_NaP_N,\qquad
d_N(\mathcal A,D_j\mathcal A D_j)=0.
\]

Thus the previous fixed-reference counterexample obtained by moving the flip
to arbitrarily large odd labels is invisible in this fixed-window metric.
It cannot simply be reused as an operational obstruction here.

## 3. An Accessible-Amplitude Counterexample

Keep the flipped level fixed at \(j=3\). Define

\[
u_3=0,\quad u_n=\sqrt{\frac{192}{61}}\,2^{-n}\ (n\ne3),\qquad
c_\epsilon^{\pm}=\sqrt{1-\epsilon^2}\,u\pm\epsilon|3\rangle,
\quad0<\epsilon<\tfrac12.
\]

Since \(\sum_{n\ne3}4^{-n}=61/192\), these references are normalized and
have full support. Their norm difference is \(2\epsilon\). Their pure-state
trace distance, using the convention \(T(\rho,\sigma)=\|\rho-\sigma\|_1/2\), is

\[
T_\epsilon=2\epsilon\sqrt{1-\epsilon^2}\longrightarrow0.
\]

They satisfy the fixed reference energy budget. Indeed,

\[
\langle u,Hu\rangle
\le\sum_n n|u_n|^2
=\frac{192}{61}\left(\frac49-\frac3{64}\right)
=\frac{229}{183}<2,
\]

and \(\log3<2\); the energy of either reference is the convex combination
\((1-\epsilon^2)\langle u,Hu\rangle+\epsilon^2\log3<2\).
Yet \(\mathcal A_{c_\epsilon^+}=\mathcal A\) and
\(\mathcal A_{c_\epsilon^-}=D_3\mathcal A D_3\) for every \(\epsilon\).

### Fixed Effect and Two Fixed Preparations

Put \(P_0=I-SS^*\), the projection onto odd labels, and define

\[
L=SP_0+P_0S^*+I-P_0-SP_0S^*,\qquad Q=(I+L)/2.
\]

In every odd-number fiber, \(L\) swaps levels \(k=0,1\) and fixes the rest.
It is a self-adjoint unitary in \(\mathcal A\), hence \(Q\) is a projection.
The conjugate \(Q'=D_3QD_3\) is a valid effect in the flipped algebra.
Use the preparations

\[
\psi_0=(|1\rangle+|2\rangle)/\sqrt2,\qquad
\psi_1=(|3\rangle+|6\rangle)/\sqrt2.
\]

They lie in the fixed window for every \(N\ge6\), do not depend on
\(\epsilon\), and give probabilities 1 and 0 respectively for \(Q'\).
Every \(a\in\mathcal A\) has the same expectation on the two preparations,
because swapping their odd fibers commutes with \(\mathcal A\). Calling the
common value \(z\),

\[
\max\{|1-z|,|z|\}\ge\tfrac12.
\]

Therefore no effect from \(\mathcal A\) can approximate the compressed
\(Q'\) with operator-norm error below \(1/2\). Together with the universal
midpoint upper bound, this proves analytically

\[
\boxed{d_N(\mathcal A_{c_\epsilon^+},\mathcal A_{c_\epsilon^-})
=\tfrac12\quad(N\ge6),\qquad T_\epsilon\to0.}
\]

This disproves **uniform continuity on the stated reference class**, even
with the fixed energy budget and fixed test preparations. It does not
disprove continuity at each individual full-support reference: both sequences
approach \(u\), which lacks support at level 3 and is outside that domain.

## 4. Conditional Local Stability

For nonzero complex numbers \(z,w\), normalization obeys

\[
\left|\frac z{|z|}-\frac w{|w|}\right|
\le\frac{2|z-w|}{|z|}.
\]

One proof multiplies the left-hand vector by \(|z|\), writes it as
\((z-w)+(|w|-|z|)w/|w|\), and uses the triangle and reverse-triangle
inequalities. Lean checks this scalar estimate directly.

Fix a full-support \(c\), a finite \(N\), and
\(\mu_N(c)=\min_{n\le N}|c_n|>0\). For another full-support normalized \(d\),
align its irrelevant global phase and set

\[
\delta=\min_{|\lambda|=1}\|c-\lambda d\|.
\]

The diagonal phase unitaries on the window differ in norm by at most
\(2\delta/\mu_N(c)\). For any compressed effect \(x\), center it at \(I_N/2\):
\(\|x-I_N/2\|\le1/2\). If \(U,V\) are the two phase unitaries, then

\[
\|UxU^*-VxV^*\|
\le2\|U-V\|\,\|x-I_N/2\|
\le\|U-V\|.
\]

Pairing corresponding effects in both directions therefore gives

\[
\boxed{d_N(\mathcal A_c,\mathcal A_d)
\le\min\left\{\tfrac12,\frac{2\delta}{\mu_N(c)}\right\}.}
\]

For normalized pure references, \(\delta\le\sqrt2\,T(c,d)\), so a
trace-distance version has numerator \(2\sqrt2\,T\). A common certified
floor \(\mu>0\) makes this a uniform bound on that restricted class.
The mean-energy constraint alone supplies no such floor, as Section 3 shows.
This is a reference-amplitude condition, not by itself a calibrated bound on
transition-measurement errors. Neither mixed reference noise, spectral errors,
finite frequency resolution nor an increasing-window limit is covered.
This is ordinary conditioning of phase extraction, not a proposed new
fundamental law. The passage from the scalar estimate to this full effect-set
bound is presently an analytic proof, not a complete Lean formalization.

## 5. Access Controls and Interpretation

- With only energy-diagonal test states, corresponding phase-conjugated
  effects have identical probabilities. The resulting restricted
  pseudometric is zero. This hides the phase information; it does not select
  an algebra or demonstrate an entropy transition.
- Co-transporting both states and measurements preserves all probabilities.
  That is a different comparison from the fixed-apparatus convention here.
- The witness requires coherent superpositions at specified energies and a
  fixed phase standard. Such resources do not follow from an autonomous,
  stationary ICC model. A hard cutoff alone is not a laboratory implementation
  or a bound on reconstruction cost.
- All algebras remain type I in this construction. There is no continuum AQFT,
  Type III extension, gravitational dynamics, or cosmological prediction.
- Nothing here repairs the previously established invariance under the
  reference's free evolution. Stability is only one prerequisite, not a
  mechanism for changing observable algebras.

## 6. Verification and Dependencies

[IccOperational.lean](./lean/IccOperational.lean) is bundled with the
`IccArithmetic` project, on Lean/mathlib v4.24.0. Its seven audited
declarations cover:

1. The self-adjoint projection witness in the infinite shift algebra.
2. Normalization of the two probe rays.
3. Positivity of the flipped effect and its complement.
4. The probability range for arbitrary valid effects.
5. The two-fixed-probe lower bound for every member of the original algebra.
6. The scalar phase perturbation bound.

The audit allows only mathlib's standard `propext`, `Classical.choice`, and
`Quot.sound`; it rejects unfinished proofs and new axioms. A deliberately
incorrect upper-bound proof must fail. The exact reference normalization,
mean-energy sum, trace-distance expression, reconstruction formula, compressed
Hausdorff theorem, and combined local bound remain analytic dependencies.
No OpenAI manuscript or unverified external theorem is imported into Lean.

[operational_stability_checks.py](./operational_stability_checks.py) exercises
nine groups of small numerical
diagnostics, including the cutoff, diagonal-access and co-transport controls.
It compresses operators from the infinite model; it does **not** generate an
algebra from a truncated shift. Random checks do not prove a universal bound.
The 64-coordinate reference calculations are diagnostics of the explicitly
normalized infinite sequence, not substitutes for its analytic tail argument.

Run `python3 run_checks.py` here for the combined 24 finite diagnostic groups.
The [Lean project](./lean/README.md) has its own optional verification command
and a five-minute total proof-check timeout after dependency setup. Its
[release record](./lean/verification-record.json) stores source hashes, actual
exits, axiom inventories and timings. That project also includes the earlier
B.3 proofs; its combined audit covers 16 declarations, not 16 independent
cosmological results.

Separate bounded [mathematical](../../feedback/v0.1.7-mathematical-review.md) and
[physics/operational](../../feedback/v0.1.7-physics-review.md) reviews are recorded. These are
AI-assisted checks, not human peer review or validation of ICC.

## 7. Literature Boundary and Decision

[Shirokov, *Operator E-norms and their use* (v6)](https://arxiv.org/abs/1806.05668v6)
provides context for choosing energy-sensitive operator metrics. Its
operator E-norm results are not asserted to prove continuity of this
reference-to-algebra map; the hard-cutoff effect metric here is defined
separately.

[Li, *Relative Perturbation Bounds for the Unitary Polar Factor* (1994)](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1994/5480.html)
provides polar-factor perturbation background. That report treats structured
relative perturbations. Our scalar estimate is proved directly, not claimed
as an application of its relative-perturbation theorem or as a novel result.

**Decision:** close this bounded mathematical gate. A cutoff yields a useful
local statement but no reference-independent robustness guarantee. A future
physical application would need independently supplied access/control data
and a calibrated reference-amplitude condition, or a justified reconstruction
that does not require resolving arbitrarily small amplitudes. Neither choice
is made or derived here. Inclusion in the release does not change ICC's core
postulates or supply the missing physical input.
