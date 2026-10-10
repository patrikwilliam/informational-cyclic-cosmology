# Zanardi Transport: Bounded ICC Applicability Review

Date: 8 October 2026.

Release supplement: v0.1.6 (9 October 2026). The original review date and
source-version boundary are retained; no new physical selector is proposed.

Source: Paolo Zanardi, *Universal holonomic control of algebras of observables*,
[arXiv:2609.28662v1](https://arxiv.org/html/2609.28662v1), submitted 23 September
2026. The live record lists v1 only at this review date.

Status: internal AI-assisted applicability analysis. Source hypotheses and
selected constructions were inspected; the complete source theorems were not
independently certified. The deductions below are limited to declared finite
matrix factors. No claim of novelty is made.

## Verdict and Review Boundary

The framework is compatible with a geometric description of a supplied path of
ICC candidate embeddings. It does not supply an independently motivated path,
physical access changes, an entropy functional for cosmology, or an aeonic
selector. Retain it as conditional geometric prior art, not as a new postulate
or evidence for cyclic cosmology.

The question reviewed is whether prescribed-algebra transport can be formulated
without assuming a fundamental external clock, and whether its physical
interpretation closes ICC's missing-input problem. No lattice search,
optimization campaign or new cosmological dynamics was attempted.

## Source Basis

For finite unital matrix algebras of fixed block structure, the paper studies
unitary orbits and a canonical invariant connection. Equations (2)-(3),
Appendix B and Theorem 2 separate normalizer directions from directions that
move a tensor factor. The connection fixes transport along a specified curve,
not the curve itself. A tensor-factor loop returns the algebra while its lift
may acquire logical holonomy.

Physical implementation is conditional on compatible gapped Hamiltonians and
accessible control paths. The adiabatic construction uses a band refinement;
Appendix G distinguishes its transport from intrinsic tensor-factor transport.
Generic attainment within the specified class of smooth isospectral families
remains conjectural in Appendix F; additional control restrictions may reduce
the attainable holonomy. The fixed finite orbit does not cover changes of
algebra type or a continuum gravitational transition.
These are source claims, not newly proved results of this review.
[Primary text](https://arxiv.org/html/2609.28662v1).

## Dictionary for the Present ICC Ansatz

Use the finite factor

$$
\mathcal A_0=\operatorname{Mat}_2(\mathbb C)\otimes I_2
\subset\operatorname{Mat}_4(\mathbb C),
\qquad
\mathcal A(s)=V(s)\mathcal A_0V(s)^\dagger.
$$

This is a special case of ICC's candidate embedding family, not a derived
physical family. Its normalizer Lie algebra consists of local generators;
its Hilbert-Schmidt orthogonal complement consists of interaction generators.
With $\Omega=V^\dagger dV/ds$ and $P_{\mathfrak n}$ the normalizer projection,
the horizontal representative is obtained from

$$
\frac{dh}{ds}=-P_{\mathfrak n}(\Omega)h,
\qquad h(0)=I,
\qquad \widetilde V=Vh.
$$

Transport of an observable is then
$a\mapsto\widetilde V(s)a\widetilde V(s)^\dagger$ once the path and initial
frame are given. This could augment the description of an already justified
ICC pair. It does not replace ICC's $T_n$, which currently labels a candidate
pair, or its unspecified relation $\mathcal R$.

## Independent Bounded Deductions

### 1. A Path Parameter Need Not Be Fundamental Time

For an orientation-preserving reparameterization $s=f(r)$, the chain rule gives
$\Omega_r=f'(r)\Omega_s$ and
$dh/dr=-P_{\mathfrak n}(\Omega_r)h$. Thus the same oriented curve has the same
horizontal transport and endpoint after reparameterization. This is a
geometric statement, not a construction of a physical clock.
An actual adiabatic implementation still depends on physical duration, rates
and spectral gaps; geometric reparameterization invariance does not remove
those requirements.

An intrinsic observable could in principle label such a curve. Neither this
calculation nor the source identifies that observable in ICC or derives the
curve from $\rho$, $H$ and relational boundary data. Relabeling a hand-chosen
control schedule as a clock reading would not supply the missing derivation.
Path reversal also does not select a thermodynamic arrow.

### 2. A Fixed-State Entropy Contrast Fits the Geometry

Keep $\rho=|\Phi^+\rangle\langle\Phi^+|$, where
$|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$, and choose

$$
G=X\otimes Y,\qquad
V(s)=e^{-i\theta(s)G},\qquad \theta(s)=\frac\pi4s,\quad 0\le s\le1.
$$

Both Pauli factors are traceless. Therefore $G$ is orthogonal to all local
generators and $V^\dagger dV/ds=-i(\pi/4)G$ is horizontal. This needs no gauge
correction. Since $G^2=I$ and $G|\Phi^+\rangle=-i|\Phi^-\rangle$,

$$
V^\dagger|\Phi^+\rangle
=\cos\theta|\Phi^+\rangle+\sin\theta|\Phi^-\rangle.
$$

The density matrix representing the fixed state's restriction to the moving
first factor is consequently

$$
\rho_A(s)=\operatorname{Tr}_B(V^\dagger\rho V)
=\operatorname{diag}\!\left(
\frac{1+\sin2\theta}{2},\frac{1-\sin2\theta}{2}\right).
$$

Its entanglement entropy is
$h_2((1+\sin2\theta)/2)$ bits: one bit at $s=0$ and zero at $s=1$.
This is a direct algebraic derivation. The accompanying small matrix checks
corroborate it; they are not its proof for all parameters.

This is an alternative smooth interpolation of a known kinematic possibility,
not the specific endpoint unitary or POVM in the released measurement example.
The generator and stopping angle were chosen to make this Bell state product
in the new factor. No independently motivated, non-circular physical reason
for that choice has been supplied. A physical selector may depend on the state;
the problem is choosing its inputs solely to obtain the desired entropy.
Horizontality does not remove this circularity risk.

### 3. Co-Transport Is a Different Operation

If the state is instead actively carried by the same unitary,
$\rho(s)=V(s)\rho V(s)^\dagger$, then

$$
V(s)^\dagger\rho(s)V(s)=\rho.
$$

Its restriction relative to the co-transported factor remains $I_2/2$ and has
one bit of entropy. Changing both the state and algebra together must therefore
not be counted as the fixed-state entropy contrast above.

For this example $[G,\rho]\ne0$. If $G$ were the actual global Hamiltonian,
the chosen Bell state would not be stationary. As a geometric path generator,
$G$ need not be that Hamiltonian. A proposed physical or relational realization
must explain the distinction and its compatibility with ICC's assumed
stationary global state. The source's conditional implementation claim does
not by itself supply that explanation. This is not a no-go for all relational
realizations or a claim that every control must co-transport state and algebra.

### 4. A Returned Factor Does Not Retain This Entropy Drop

If a factor path closes as a set, $\mathcal A(1)=\mathcal A(0)$, and the
ambient state is fixed, its restricted state on that concrete algebra is
identical at the endpoints. Under a transported matrix-factor identification,
the endpoint normalizer acts by an inner automorphism; eigenvalues and
restricted von Neumann entropy are unchanged.

In the same explicit example, extending $\theta$ from zero to $\pi/2$ returns
the factor, since $V=-iX\otimes Y$ is a local product up to phase. The entropy
goes from one bit to zero and back to one. Nontrivial holonomy does not make the
intermediate low entropy persist at the returned factor.

This conclusion concerns fixed-state factor entropy and a returned concrete
algebra. It is not a no-go for ICC, whose aeonic pair need not form such a loop,
or for histories with changing conditional states, resources or measurements.
Rotating a stipulated POVM can change measurement entropy even within one
algebra; that is a separate protocol comparison.

## Applicability Gates

| Gate | Outcome | Reason |
|---|---|---|
| Transport on a supplied finite-factor path | Pass | Explicit horizontal construction above |
| Geometry without a fundamental external time | Pass, mathematical only | Reparameterization does not change the oriented path transport |
| Derive an intrinsic physical path with no added input | Not supplied | Endpoints, curve and access still require a physical derivation |
| Preserve ICC stationarity in a physical realization | Open | The geometric generator is not automatically the global constraint |
| Produce a persistent reset from a returned factor at fixed state | Fails in this domain | Same concrete algebra and state at both endpoints |
| Extend to continuum QFT or gravitational algebras | Outside scope | Finite fixed-block geometry does not establish that extension |

## Disposition and Stop Condition

Keep the framework as conditional prior art for transporting observables after
an independently motivated embedding family is available. Do not add a new
selector, search for a conveniently low-entropy path, or restart EC/CAR or
minimal-scrambling optimizations on the strength of this connection.

The bounded question is settled: geometric compatibility passes; a physical
selector without additional inputs does not follow. Further transport work is
justified only when independent relational data determines an admissible path
and operational access, with a consistent global constraint and entropy
comparison. Supplying that input remains a separate research problem.

## Verification and Limits

[transport_checks.py](./transport_checks.py) uses NumPy for six small diagnostics: horizontal-generator
orthogonality, the fixed-state pullback formula and endpoint entropies,
co-transport invariance, returned-algebra behavior, reparameterized
horizontality, and the nonzero Bell-state commutator. All six passed with
absolute tolerance $10^{-12}$ and zero relative tolerance.

Run with the configured Python runtime, for example:

```sh
python3 research/v016/transport_checks.py
```

These checks do not validate arbitrary algebra types, the complete holonomy or
uniqueness theorems, adiabatic errors, finite-control reachability, continuum
limits, or cosmology. No source numerical campaign was rerun. Release
integration checks are recorded [separately](../../feedback/v0.1.6-integration-verification.md).
The completed finite investigations remain closed.
