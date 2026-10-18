# Three-Qubit Fixed-Interaction Memory Gate

Study: 15 October 2026. Integrated into v0.1.8 on 16 October 2026.

## Bounded Protocol, Fixed Before Calculation

This model uses simultaneous detector exchange and memory coupling, rather
than a separately applied memory-copy gate.
It is not a search for an entropy contrast or an algebra selector.

The tensor factors S (input), D (detector/reference), and M (memory) are supplied.
Set n = (I-Z)/2, hbar = 1 and

$$
H=\omega Q+\frac g2(X_SX_D+Y_SY_D)+k n_D X_M,
\qquad Q=n_S+n_D.
$$

The memory's two logical states have the same Q charge; its bare Hamiltonian
is zero in this ideal model. A third ordinary charged qubit with Q including
n_M would NOT make the proposed interaction charge-conserving. Both couplings
are time independent. The controlled rotation is an explicit apparatus design,
not a derived cosmological interaction. No intermediate copying pulse,
dephasing channel, measurement, or detector/memory reset is inserted.

The primary settings are g = k = 1, omega = 0 and exposure T = pi/4. This keeps
the previous detector's nominal exposure and sets equal coupling strengths;
there is no parameter optimization. Initially D is |+> and M is |0>.
The operational terminal pointer is n_D. Memory-population readout n_M is
a separately declared diagnostic in otherwise identical trials, not feedback.

The three gates are:

1. Record: with S initially I/2, compare M's states for initially D = |0> and
   D = |1>. Report distinguishability using the fixed n_M readout as well as
   the trace distance. This is a record of an initial preparation label, not
   an assumption that D has an undisturbed classical trajectory.
2. Access: derive the all-input effect on S. Prime D,M using S = I/2 for T,
   trace out only the old S, and test a fresh uncorrelated S for the SAME T
   with the SAME H and pointer. Keep the full correlated D,M state. Fresh-input
   exchange remains an external operation; this is not an autonomous stream.
3. Controls: remove each coupling, remove the initial detector coherence,
   and replace the memory blank by I/2. The last control distinguishes
   record formation from dynamical backaction. Check finite nearby times,
   but do not tune parameters to rescue a failed witness.

Report mathematical validity and physical interpretation separately. Even a
positive finite gate does not supply a subsystem selector, an autonomous clock,
durable classical memory, or an ICC transition.

## Result: A Conditional Pass, With an Important Negative Control

The simultaneous model produces a partial readable memory record and changes
the next induced detector measurement at unchanged H, duration, and pointer.
It does NOT establish that recording causes the access change: a maximally
mixed memory has the same detector statistics and no local record of the input
or detector-preparation label. The bounded mathematical and operational gate
passes; the stronger claim that a locally readable record is necessary fails
for this example. This is not a no-go theorem for records in general or for ICC.

The full S,D,M tensor product is an eight-dimensional Hilbert space, not an
extra spatial dimension. M is an explicitly supplied two-state apparatus degree
of freedom in ordinary spacetime. Neither its existence in a cosmological
setting nor its coupling is derived. No infinite family of actual observers
is assumed. The model is not being adopted as an aeon-transition mechanism.

## Exact Finite Calculation

Since [H,X_M] = 0, resolve the memory into its X eigenvalues mu = +/-1.
Writing U(t) = sum_mu V_mu(t) tensor P_mu, P_mu = (I+mu X)/2, the S,D blocks
are particularly simple. The zero-excitation block is 1, the two-excitation
block is exp[-i(2 omega+mu k)t], and in the one-excitation basis (|01>,|10>)

$$
V_\mu^{(1)}(t)=e^{-i(\omega+\mu k/2)t}
\left[\cos(\Omega t)I-i\frac{\sin(\Omega t)}{\Omega}
\begin{pmatrix}\mu k/2&g\\g&-\mu k/2\end{pmatrix}\right],
\quad \Omega=\sqrt{g^2+k^2/4}.
$$

The zero-coupling expression is understood by continuity. Both interactions
are present throughout each exposure; their commutator is nonzero, so this U
cannot be replaced by the product of separate exchange and recording gates.

For any supplied apparatus state tau_DM the induced detector effect is defined
for ALL system inputs by

$$
\operatorname{Tr}(\rho_S F_\tau)
=\operatorname{Tr}\!\left[U(\rho_S\otimes\tau_{DM})U^\dagger n_D\right].
$$

For omega = 0, put s = sin(Omega T), c = cos(Omega T), alpha = k/(2 Omega),
beta = g/Omega, delta = kT/2 and u = beta^2 s^2. The initial apparatus is
tau_0 = |+><+|_D tensor |0><0|_M. Its effect and the effect after an UNREAD
priming exposure with S = I/2 are

$$
F_0=\frac I2+y_0Y-\frac u2Z,\qquad y_0=\frac{\beta sc}{2},
$$

$$
\tau_1=\operatorname{Tr}_S[U(I_S/2\otimes\tau_0)U^\dagger],
\qquad F_1=\frac I2+y_1Y-\frac u2Z,
$$

$$
y_1=\frac{\beta s}{2}\left[(c^2-\alpha^2s^2)\cos\delta
-2\alpha sc\sin\delta\right].
$$

One way to derive the second formula is to keep the two normalized diagonal
memory-X blocks of tau_1. Their detector populations are 1/2 and their detector
coherences are exp(i mu delta)(c+i mu alpha s)/2. Averaging each block's
induced effect gives F_1. Replacing tau_1 by tau_D tensor tau_M is incorrect.
The old S is discarded and a fresh, uncorrelated S supplied; there is NO
intermediate D or M readout. This is not the postmeasurement reuse protocol
of the previous study, which had an explicit intermediate population readout.

At g = k = 1 and T = pi/4:

| Quantity | Value |
| --- | ---: |
| y_0 | 0.2197744539 |
| y_1 | 0.0341235815 |
| u/2 | 0.2368693846 |
| Operator norm of [F_0,F_1] | 0.0879500158 |
| Success distinguishing fresh inputs (I +/- Y)/2 before priming | 0.7197744539 |
| Same success after unread priming | 0.5341235815 |
| Effect error if DM correlations are incorrectly discarded | 0.0665998149 |

Success refers to equal priors and optimal classical processing of the fixed
binary detector outcome. Since [F_0,F_1] = -iu(y_0-y_1)X is nonzero, neither
effect is a classical relabeling of the other. This is not a general statement
that noncommuting unsharp POVMs are incompatible or that all available effects
form a newly selected observable algebra.

## What the Memory Records

For S = I/2 and initially D = |d>, d = 0,1, let sigma_d be the final memory
state. With trace distance D_tr = ||sigma_0-sigma_1||_1/2 and the fixed
population-outcome distance D_pop = |Tr[n(sigma_0-sigma_1)]|,

$$
D_{\rm tr}=\frac12|\sin(kT)+2\alpha sc|,\qquad
D_{\rm pop}=D_{\rm tr}|\sin(kT)|.
$$

For example, in the memory-X basis the difference of the off-diagonal overlap
factors is i exp(-ikT)[sin(kT)+2 alpha sc]; the density-matrix off-diagonal
difference is half this quantity. This gives the two distances above.
At the primary setting D_tr = 0.5733278445 and D_pop = 0.4054040067. Thus the
fixed n_M readout distinguishes the initial D labels with success 0.7027020033.
The larger Helstrom success (1+D_tr)/2 would require a different memory
measurement, which is NOT granted as part of the fixed population protocol.

This is a partial record of a supplied initial preparation label, not a faithful
copy of a pre-existing detector trajectory: [H,n_D] is nonzero. In trials with
D initially |+>, memory population also carries system-input information. Its
induced system effect is approximately

$$
G_0=0.2400962917I+0.0837459741Y-0.0472979967Z.
$$

No terminal memory readout is actually inserted between the two exposures in
the priming test; G_0 is a diagnostic in separate trials. Unitary record
formation is not irreversible classical outcome production or stable storage.

## Exact Negative Control: No Local Record Is Needed Here

Replace the memory blank |0><0| by I/2. Both states have identical diagonal
blocks in the conserved memory-X basis. Since U and n_D are block diagonal in
that basis, every induced detector effect depends only on these blocks.
Tracing out a used S preserves that equivalence, including the DM correlations.
It therefore holds for subsequent supplied fresh inputs, not just one chosen
input or one numerical time.

In the mixed-memory control the memory marginal remains I/2 for every system
input and either initial detector label. Its fixed population readout and any
other local memory measurement carry no label information. Nevertheless the
detector effects F_0 and F_1 are exactly the same as with the pure memory blank.
There can still be information in joint correlations; this is not a claim that
all records or all correlations in the full system disappear.

For D-only measurements this model is operationally equivalent to a mixture
of two static conditional-detuning sectors. The extra coupling changes the
detector dynamics, but a locally readable memory record is not what selects
the changed detector measurement. This control prevents promoting the example
to a record-driven selector.

Further controls give:

- k = 0: no memory record, but unread priming still changes phase success from
  0.75 to 0.6767766953 through the original exchange interaction alone.
- g = 0: memory can record D, but n_D contains no information about S.
- Initially D = I/2: no transverse input sensitivity before or after priming.
- Global Q Fisher information remains 1 during the unitary priming exposure;
  total Q expectation and total-H energy expectation are conserved. This
  conservation does not cover the externally supplied input replacement or
  terminal readout operation. Q symmetry is not full energy autonomy.

## Checks, Reviews, and Stop Boundary

[checks.py](checks.py) and [checks-results.json](checks-results.json) provide:

- 80 propagator comparisons against the analytic sector solution;
- 640 Born-rule comparisons on all four system matrix units, using arbitrary
  apparatus density matrices and both terminal pointers;
- 60 analytic reuse/record comparisons and conserved-X equivalence checks;
- positivity, charge conservation, limiting models, and four consecutive
  unread priming updates for the mixed-memory equivalence;
- nearby exposures 0.9T, T, 1.1T and uniform +/-10% timing uncertainty, with
  independent timing errors on priming and test exposures.

Random couplings in the formula checks validate identities, not a physical
parameter search. The timing examples are limited diagnostics, not a generic
robustness theorem. The timing-averaged commutator norm is 0.0875334788 and the
population-record distance is 0.4043146334. No clock has thereby been derived.

The [mathematical review](mathematical-review.md) and
[physics review](physics-review.md) are separate internal AI-assisted passes,
not independent expert certification or Lean proofs. Run `python3 -B checks.py`
with NumPy; optionally add `--output PATH`. The results include the script hash.

**Stop here for this finite example.** It supplies a conditional operational
illustration and a useful limitation, not a reason to expand to more qubits.
The narrow unresolved ICC question remains which independently justified
physical inputs determine measurement access. Nothing here decides whether
aeons are successive physical regimes or observer-relative descriptions.
No new ontological interpretation or infinite-observer assumption is introduced.
The later [capability study](../measurement-capability/README.md) answers the
stronger question about all allowed measurements, not only a chosen readout.

## Literature Boundaries

- [Bose, arXiv:0802.1224](https://arxiv.org/abs/0802.1224) motivates exchange
  interactions and fixed-coupling quantum transport, not this particular
  memory Hamiltonian or an ICC interpretation.
- [Marvian and Spekkens, arXiv:1212.3378](https://arxiv.org/abs/1212.3378)
  supplies the asymmetry-resource perspective on conservation-constrained
  measurement. Our transverse effects are unsharp, not a violation of WAY.
- [Bartlett et al., arXiv:quant-ph/0602069](https://arxiv.org/abs/quant-ph/0602069)
  studies finite reference-frame degradation and operational measurement
  quality. It is prior context, not a derivation of the exact model here.

These primary sources were checked on 15 October 2026. The controlled rotation
is a declared finite apparatus construction; no source is cited as evidence
that this apparatus exists in cosmology. No novelty claim is made.
