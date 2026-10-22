# Arithmetic Operations as Inputs to Algebra Reconstruction

Date: 10 October 2026.

Status: bounded internal AI-assisted literature review and elementary derivation,
reviewed for v0.1.7. Not independent expert review and not a novelty claim.
No result from the OpenAI mathematics collection is required below.

## Question and Verdict

Can independently motivated physical or relational data determine multiplication
operations, or equivalent structure, without first specifying subsystems?

**Conditional mathematical answer: yes. Physical answer for ICC: not yet.** A
specified coherent probe/reference can reconstruct multiplication isometries in
an exactly logarithmic, simple-spectrum model. This exposes the required input;
it does not derive that input from ICC. In this construction:

- The logarithmic Hamiltonian and equilibrium states do not fix coherent shifts.
- A general probe need not yield mutually compatible prime operations.
- A full-support pure reference supplies compatible shifts, but all such choices
  are related by unitaries commuting with the Hamiltonian. For a fixed stationary
  state they cannot produce different restricted-state entropies at a fixed prime.
- Ordinary evolution of that reference under the same Hamiltonian leaves each
  reconstructed algebra unchanged.
- Full operator-norm algebra stability fails under arbitrarily small reference
  errors in the infinite model. This is not a statement about every operational,
  energy-constrained, or state-weighted error metric.

Thus the minimal reference-phase route is not a successful ICC transition
selector. It returns to the centralizer issue already present in earlier work.
This is a bounded obstruction for the construction below, not a no-go for ICC,
all arithmetic models, or all relational reconstruction schemes.

## Established Literature and Its Actual Inputs

| Route | Supplied inputs | Established output | What it does not supply for ICC |
| --- | --- | --- | --- |
| Bost-Connes representation | An arithmetic algebra, multiplication isometries, and time evolution | Arithmetic quantum statistical mechanics and equilibrium-state structure | A derivation of this arithmetic structure from cosmology |
| Bost-Connes reconstruction | A C*-algebra already in the number-field Bost-Connes class | Reconstruction of its semigroup action up to conjugacy; classification of the underlying number field | Reconstruction from an arbitrary Hamiltonian or from an unstructured global state |
| Reference-frame/asymmetry methods | A symmetry representation plus specified states, operations, or reference resources | Analysis of coherent operations and relational information | A physical choice of ICC's reference, access algebra, or clock decomposition |
| Observable-induced subsystems | Operationally specified observable/interactions algebras | Subsystem structure under suitable algebraic conditions | The independent origin of those operational inputs |
| Half-sided modular inclusions | An inclusion of von Neumann algebras and suitable common vector/weight | Translation/dilation structure under modular hypotheses | The original inclusion, a prime arithmetic structure, or an ICC algebra selector |

The source statements are [S1]-[S5] below. In particular, the reconstruction
theorem [S2] is stronger than a mere analogy, but its premise is a rich algebra
in a specified arithmetic class. It is not a theorem that an energy spectrum
alone determines that class. The formulae below are our explicit conditional
derivation, not claims attributed to these sources.

## 1. Fix the Input Data and Their Symmetries

Assume the represented ambient algebra is B(Hilbert space), with

$$
\mathcal H=\ell^2(\mathbb N_{>0}),\qquad
H|n\rangle=(\log n)|n\rangle,\qquad P_n=|n\rangle\langle n|.
$$

The zero of energy and energy/time units have been fixed. Both the exact
logarithmic spectrum and its multiplicity one are assumptions, not consequences
of ICC. The prime-count observables N_p = sum_n v_p(n) P_n are defined by spectral
calculus; their spectral projections generate commutative algebras.

Every diagonal unitary $D=\sum_n e^{i\theta_n}P_n$ preserves $H$ and any normal
stationary density operator $\rho$, where stationarity means
$e^{-itH}\rho e^{itH}=\rho$ for every real $t$. This avoids an implicit domain
assumption in the commutator with unbounded $H$.
Nondegeneracy implies that such $\rho$ is diagonal. Equilibrium
or stationarity therefore does not remove the independent eigenvector phases.
A coordinate-covariant construction must respect the symmetries of all its
inputs. An embedding chosen by a convention for those phases is not an
independently measured physical distinction. Quotienting these symmetries is
allowed, but does not turn equivalent descriptions into different aeons.

Suppose isometries T_m have the exact covariance and semigroup properties

$$
e^{itH}T_m e^{-itH}=m^{it}T_m,\qquad
T_mT_n=T_{mn},\qquad T_1=I.
$$

Simple spectrum forces T_m|n> = alpha_m(n)|mn>, with |alpha_m(n)| = 1.
Acting with T_m T_n on |1> yields

$$
\alpha_m(n)=\frac{\eta_{mn}}{\eta_n},\qquad
\eta_n=\alpha_n(1),\qquad \eta_1=1.
$$

Consequently every such coherent family is D S_m D*, where
S_m|n> = |mn> and D|n> = eta_n |n>. This proves conditional uniqueness up to
the diagonal symmetry, not uniqueness of a physically distinguished embedding.
The semigroup/isometry assumptions themselves are substantive extra inputs.

## 2. A Probe Can Fix the Missing Phases

Let B be a specified bounded operator, for example a measured coupling or a
prepared rank-one projector. Its exact frequency-log(m) component is

$$
B_m=\sum_{n\ge1}P_{mn}BP_n
   =\sum_{n\ge1}b_m(n)|mn\rangle\langle n|.
$$

This orthogonal weighted-shift sum is strongly convergent and bounded. It is a
mathematical frequency projection, not an assertion that infinite-time frequency
resolution or unrestricted operator access is physically available.

If b_m(n) is nonzero for every n, the polar decomposition gives an isometry

$$
V_m|n\rangle=\frac{b_m(n)}{|b_m(n)|}|mn\rangle.
$$

Zeros give only a partial isometry and leave missing transitions. There is no
bounded-inverse assumption: the positive polar factor can have singular values
approaching zero. That is important for the stability issue below.

A polar factor is not automatically an implementable physical operation. For
the exact isometries, V_m* H V_m = H + log(m) on the energy domain. An
implementation therefore needs specified driving or compensating internal
energy exchange. Neither that access nor its resource cost follows from the
polar decomposition.

For a general probe, correct energy differences are not enough. Writing
alpha_m(n) = b_m(n)/|b_m(n)|, the two paths to pqn agree only if

$$
\alpha_q(n)\alpha_p(qn)=\alpha_p(n)\alpha_q(pn).
$$

The ratio of these two expressions is a phase around a multiplication square.
It is unchanged by diagonal basis rephasing. A probe with a nontrivial square
phase is an explicit obstruction to commuting prime shifts. For independently
extracted composite shifts one must also check V_m V_n = V_mn. Prime-square
compatibility alone does not check those independently supplied composites.

### An exactly compatible reference

Choose B = |r><r|, with r = sum_n c_n |n> a normalized vector and all c_n nonzero.
Then b_m(n) = c_mn conjugate(c_n), so

$$
V_m^{(r)}|n\rangle
=e^{i(\arg c_{mn}-\arg c_n)}|mn\rangle,
\qquad V_m^{(r)}V_n^{(r)}=V_{mn}^{(r)}.
$$

This definition is independent of the arbitrary phases used to write the
eigenvectors: it can be expressed entirely through P_n, B, and polar
decomposition. Define $\mathcal A_p^{(r)}=W^*(V_p^{(r)})$ and
$D_r|n\rangle=e^{i\arg c_n}|n\rangle$. Under the coordinate identification
$n=p^k m$, $p\nmid m$, the untwisted algebra
$\mathcal A_p^0=W^*(S_p)$ is
$\mathcal B(\ell^2(\mathbb N_0))\otimes I$, whereas
$\mathcal A_p^{(r)}=D_r\mathcal A_p^0D_r^*$.
The phase conjugation must not be omitted from the embedded-algebra statement.
To see the full first factor, the unilateral shift S
gives matrix units S^i (I - S S*) (S*)^j. Distinct primes give commuting factors.
These are type-I factors in this representation, not a continuum QFT net.

No entropy minimization enters this construction. A generic reference has
nonfactorizing coefficient magnitudes and need not become a product state.
Nevertheless, the reference phases encode the relative identifications between
energy lines. Whether that is an independently available physical resource is
exactly the question, not something the formula settles.

## 3. The Stationary-State and Clock Gates

All reconstructed families above are related by diagonal D commuting with H.
For a fixed normal stationary density operator rho, Ad(D) transports the algebra and its
restricted state without changing the latter's isomorphism class. Thus, for the
ordinary type-I reduced-state entropy at any fixed prime p,

$$
S_\rho(A_p^{(r)})=S_\rho(A_p^{(s)}).
$$

This statement includes equality when the common entropy is infinite; it does
not subtract divergent quantities. It does not compare different primes or
claim a gravitational entropy definition. Gibbs states at beta > 1 provide
normal examples. A pure stationary state of this simple H is an energy
eigenvector and is a product across the reconstructed prime factors.

If the reference changes only by r(t) = exp(-itH)r, then

$$
V_m^{(r(t))}=e^{-it\log m}V_m^{(r)},\qquad
A_p^{(r(t))}=A_p^{(r)}.
$$

So merely using successive readings along this free reference evolution does
not even change the algebra. A nonstationary target state can evade the first
entropy equality, but it changes the premise of this stationary arithmetic
model. ICC's unspecified global constraint need not have this simple spectrum.
Calling r a relational reference also requires a derivation of its
preparation or conditioning data. Page-Wootters does not supply those data
without clock/access assumptions; the existing clock-ambiguity literature [S6]
is relevant to that caution, not a universal prohibition on relational time.

The resource theory in [S3] gives independent physical meaning to coherence and
reference access. It does not select the full-support r used here. In particular,
such r cannot itself be the globally stationary pure state of this simple H.

## 4. A Specific Infinite-Dimensional Stability Failure

Take c_n = sqrt(6)/(pi n), all positive. This normalized reference has finite
mean energy for H. For odd integers r tending to infinity, flip just its r-th
coefficient with D_r = I - 2 P_r. Both references have identical energy
probabilities, while their trace distance is

$$
T(|c\rangle\langle c|,D_r|c\rangle\langle c|D_r^*)
=2|c_r|\sqrt{1-|c_r|^2}\longrightarrow0.
$$

But V_2 changes sign on the edge r -> 2r, giving operator-norm difference 2.
There is also a full algebra statement in the fixed ambient representation.
Here $d_{\rm KK}$ is the maximum of the two directed Hausdorff distances between
the closed operator-norm unit balls $A_1$ and $B_1$:

$$
d_{\rm KK}(A,B)=\max\left\{
\sup_{a\in A_1}\inf_{b\in B_1}\|a-b\|,
\sup_{b\in B_1}\inf_{a\in A_1}\|a-b\|\right\}.
$$

It lies in $[0,1]$, since zero belongs to both unit balls. In this convention:

$$
d_{\rm KK}(A_2,D_r A_2D_r^*)=1.
$$

Here is a direct witness. A_2 is B(ell^2(N_0)) tensor I on the decomposition
n = 2^k m with m odd. Any a in A_2 has the same matrix element from k=0 to k=1
in every m-fiber. The unit-ball element D_r S_2 D_r* has that element -1 in the
r-fiber and +1 in any other odd fiber. Hence its distance to every a is at least
max(|z-1|,|z+1|) >= 1. Zero is in the unit ball, so the distance and the full
Kadison-Kastler distance are exactly 1.

This defeats continuity from reference-state trace distance to full
operator-norm algebra distance for this infinite reconstruction, even at the
fixed reference c above. It does not defeat an energy-restricted or
state-weighted notion of operational agreement. Treating simultaneously
conjugated inputs/outputs as gauge equivalent is also a different comparison.
On a fixed finite access window, a nonzero lower bound on measured transition
amplitudes permits local phase stability; it does not by itself ensure a
uniform continuum limit. Exact frequency matching is an additional fragile
assumption if the logarithmic spectrum is perturbed.

The separate [fixed-access follow-up](./operational-stability.md) now treats
one such metric: operator-norm Hausdorff distance between compressed effect
sets with coherent external test preparation. The old beyond-window flip is
invisible, but a small accessible reference amplitude prevents uniform
continuity over the fixed mean-energy class. Local continuity at each fixed
full-support reference survives, with bound min(1/2, 2 delta/mu_N).
This concerns reference amplitudes, not a general transition-calibration error
model. The [Lean supplement](./lean/README.md) checks selected mathematical
components without formalizing the entire reference-to-algebra argument.

## 5. Physical Assessment and Bounded Next Gate

There are established ways for additional data to carry genuine structure:
measured couplings, reference resources, symmetry representations, and algebra
inclusions. None of the sources inspected derives the particular logarithmic
spectrum and compatible multiplication operations from ICC's current premises.
That is a bounded literature finding, not a claim that no relevant theorem can
exist anywhere.

Prime labels alone are weak evidence of a specifically arithmetic physical
mechanism. An occupation vector for countably many modes can be encoded by
n = product_p p^(k_p); arbitrary additive mode energies then give
E_n = sum_p epsilon_p k_p. The special choice epsilon_p = log p is further
structure, not a consequence of this encoding or of quantum mechanics.

Do not promote the present construction to the paper as a working selector.
Do not enlarge the previous lattice searches to investigate it. A meaningful
follow-up would first have to supply a probe/coupling/reference from a specified
physical or relational model, independently of candidate algebras and entropy.
Then fix a finite-access error metric and check, in this order:

1. Nonzero accessible transition amplitudes and independently justified energy
   relations; specify what survives imperfect frequency resolution.
2. Multiplication-square phases and composite consistency, without imposing
   successful compatibility by hand.
3. Whether the output contains a distinction outside the symmetry orbit of all
   supplied inputs, with stability in the chosen operational metric.
4. Only then, whether independently derived relational changes alter the algebra
   and produce the required entropy contrast. Free evolution under H fails this
   test in the exact construction above.

Until such input is identified, this branch has an explicit conditional
reconstruction and an explicit stationary-state obstruction, not a physical
selector. The conditional fixed-access follow-up examines conditioning only;
it does not satisfy this physical-input requirement. No cosmological,
continuum, or new Riemann-hypothesis claim follows.

## Checks and Source Audit

Run `python3 run_checks.py` in this directory with NumPy installed. Checks cover
truncated shift identities with boundaries accounted for, generic-basis
covariance, a nonflat probe control, stationary-state entropy invariance,
unchanged algebras under reference free evolution, a non-product reference,
and a finite witness for the instability. They are diagnostics, not proofs of
the infinite statements. The derivations above provide the arguments.

Local verification on 10 October 2026 used Python 3.12 and NumPy. All assertions
passed. The largest tested reconstruction/covariance residual was below
8e-15; the nonflat probe produced a commutator matrix element of magnitude 1.
The stationary entropy difference was 0 bits. A positive-amplitude reference
retained approximately 0.04128 bits of local entropy, confirming that the
construction does not force every input to be a product state. In the finite
instability control, a reference trace distance of approximately 1.15e-5
coexisted with shift-operator distance 2 and an algebra-distance lower bound 1.
The finite window is a chosen diagnostic domain, not an independently derived
physical factorization or an infinite-limit simulation.

Sources inspected on 10 October 2026:

- **[S1]** Marcolli, *Bost-Connes, F1, 3-manifolds* (2008), slides 1-2:
  [author-hosted PDF](https://www.its.caltech.edu/~matilde/BCF1slides.pdf).
  Verified generator relations, time evolution, and the multiplication-shift
  representation. This is a source for the concrete model, not an ICC theorem.
- **[S2]** Kubota and Takeishi, *Reconstructing the Bost-Connes semigroup actions
  from K-theory* (2018 revision, first submitted 2017):
  [arXiv:1709.03281v2](https://arxiv.org/abs/1709.03281v2).
  The release review checked Theorem 1.1 and Corollary 1.2 on page 2 of the
  [v2 PDF](https://arxiv.org/pdf/1709.03281v2): the input class and equivalence
  statements match the scope used here. No audit of the full proof or new
  application to ICC is claimed.
- **[S3]** Bartlett, Rudolph and Spekkens, *Reference frames, superselection
  rules, and quantum information*, Rev. Mod. Phys. 79, 555 (2007):
  [arXiv:quant-ph/0610030](https://arxiv.org/abs/quant-ph/0610030).
  Marvian and Spekkens, *Modes of asymmetry*:
  [arXiv:1312.0680](https://arxiv.org/abs/1312.0680).
  Checked scope of reference resources and harmonic-mode decomposition; these
  sources do not assert the specific polar reconstruction proposed here.
- **[S4]** Zanardi, Lidar and Lloyd, *Quantum tensor product structures are
  observable-induced*, Phys. Rev. Lett. 92, 060402 (2004):
  [arXiv:quant-ph/0308043](https://arxiv.org/abs/quant-ph/0308043).
  Operational observables/interactions are inputs, not outputs of empty data.
- **[S5]** Araki and Zsido, *Extension of the structure theorem of Borchers and
  its application to half-sided modular inclusions*, Rev. Math. Phys. 17,
  491-543 (2005): [arXiv:math/0412061](https://arxiv.org/abs/math/0412061).
  Checked abstract and the explicit inclusion hypotheses reproduced in
  [Tanimoto's author-hosted notes, section 2.3](https://www.mat.uniroma2.it/~tanimoto/smc18.pdf).
  A pre-existing inclusion/common vector or weight is essential to this route;
  its full theorem was not re-proved here.
- **[S6]** Albrecht and Iglesias, *The clock ambiguity and the emergence of
  physical laws*, Phys. Rev. D 77, 063506 (2008):
  [arXiv:0708.2743](https://arxiv.org/abs/0708.2743), together with
  [Albrecht's later clarification](https://albrecht.ucdavis.edu/special-topics/clock-ambiguity).
  The author's clarification separates the clock ambiguity from the proposal
  to draw physical laws randomly; the latter is not adopted here.

This reviewed note is included in v0.1.7; the historical v0.1.6 PDF and archive
are preserved. The paused family-290/282 applicability work is not part of this
release. See the separate [mathematical review](../../feedback/v0.1.7-mathematical-review.md)
and [physics review](../../feedback/v0.1.7-physics-review.md).
