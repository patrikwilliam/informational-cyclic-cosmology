# Finite-Time Scrambling: Local Certificate and Operational Limits

This supplement consolidates the completed finite-dimensional analysis.
It establishes one entangled quotient-strict local minimum, excludes that
candidate from near-global selection at tolerance at most 0.3, and states
the assumptions of its operational interpretation. It is not a physical
selection law or a no-go theorem for all selectors.

## Functional and Domain

Fix $\mathcal H=\mathbb C^{d_A}\otimes\mathbb C^{d_B}$, $d=d_Ad_B$,
$\hbar=1$, a non-scalar Hermitian $H$, and a rank-one nondegenerate energy
projector $\rho$. All full factor algebras
$\mathcal A_U=U(M_{d_A}\otimes I_B)U^\dagger$ are admissible.
Identify local basis changes, simultaneous symmetries preserving $H,\rho$,
and factor exchange if equal-sized factors are declared unlabelled.
The state entropy $S(\operatorname{Tr}_B U^\dagger\rho U)$ is a diagnostic,
not part of the cost or a tie-breaker.

With normalized Haar measures, unnormalized Hilbert-Schmidt norm and a fixed
candidate-independent $T>0$, put

$$
G_U(t)=\frac1{2d}\int da\,db\,\|[a,e^{-itH}be^{itH}]\|_2^2,\qquad
F_T([U])=\frac1T\int_0^T G_U(t)\,dt,
$$

where $a\in\mathrm U(\mathcal A_U)$ and $b\in\mathrm U(\mathcal A_U')$.
For $K=U^\dagger HU$, $W_t=e^{-itK}$, realignment
$(M_t)_{(i,j),(\alpha,\beta)}=(W_t)_{i\alpha,j\beta}$ and $Q_t=M_tM_t^\dagger$,

$$
G_U(t)=1-\frac{\operatorname{Tr}Q_t^2}{d^2}.
$$

This is established bipartite operator linear entropy, not an ICC invention;
see [Zanardi et al., section 4, equations (7)-(9)](https://arxiv.org/html/2212.14340v5#S4).
The full-factor quantity is invariant under inverse evolution and factor exchange.
Its short-time expansion, with $J_{\rm int}=(I-P_{\rm loc})K$, is
$F_T=2T^2\|J_{\rm int}\|_2^2/(3d)+O(T^4)$.
For $T>0$, $F_T=0$ iff $K$ is additive: nonnegativity and continuity force
$G$ to vanish throughout the interval, hence its quadratic coefficient
vanishes; conversely additive evolution factorizes. A nondegenerate
eigenstate of an additive Hamiltonian is product.

Finite time is nevertheless not a monotone rescaling of interaction cost.
For $H=2ZI+\tfrac12 IZ+ZZ$, $T=1$, compare identity with
$C|a,b\rangle=|a\mathbin\oplus b,b\rangle$. The normalized interaction costs
are $4/21<16/21$, but
$F_1(1)=1/4-\sin4/16>F_1(2)=1/4-\sin8/32$.
Here $G_j(t)=\tfrac12\sin^2(2jt)$ and both selected $|00\rangle$ entropies
are zero. This ranking check proves neither candidate is a strict minimum.

## Variations and Complete Normal Slice

For $U(s)=Ue^{sX}$, $X^\dagger=-X$, define
$A_t=\mathcal R([W_t,X])$, $B_t=\mathcal R([[W_t,X],X])$.
Then

$$
\dot Q_t=A_tM_t^\dagger+M_tA_t^\dagger,\quad
\ddot Q_t=B_tM_t^\dagger+M_tB_t^\dagger+2A_tA_t^\dagger,
$$
$$
\delta_XF_T=-\frac4{Td^2}\operatorname{Re}\int_0^T
\operatorname{Tr}(M_t^\dagger Q_t A_t)\,dt,\qquad
\delta_X^2F_T=-\frac2{Td^2}\int_0^T
\operatorname{Tr}(\dot Q_t^2+Q_t\ddot Q_t)\,dt.
$$

For mixed entries use
$B_{ij,t}=\tfrac12\mathcal R([[W_t,X_i],X_j]+[[W_t,X_j],X_i])$ and
$Q_{ij,t}=B_{ij,t}M_t^\dagger+M_tB_{ij,t}^\dagger+
A_{i,t}A_{j,t}^\dagger+A_{j,t}A_{i,t}^\dagger$:
$\operatorname{Hess}_{ij}F_T=-2(Td^2)^{-1}\int
\operatorname{Re}\operatorname{Tr}(Q_{i,t}Q_{j,t}+Q_tQ_{ij,t})dt$.
A Hessian is a minimum test only at a critical point.

Take the fixed candidate

$$
H=\frac{XX+2YY+3ZZ}{\sqrt{14}},\quad T=8,\quad
\rho=|\Psi^-\rangle\langle\Psi^-|,\quad
|\Psi^-\rangle=(|01\rangle-|10\rangle)/\sqrt2,\quad U=I.
$$

Equivalently use $H_0=XX+2YY+3ZZ$ and $L=8/\sqrt{14}$.
The energies of $H_0$ are $-6,0,2,4$; the singlet is the unique ground state.
Every energy eigenstate is Bell-entangled with one-bit reduced entropy.
After removing overall phase, $\dim SU(4)=15$. The orbit tangent at $I$
has six local Pauli directions and the three centralizer directions
$XX,YY,ZZ$. They are independent, so its full normal space has dimension six:

$$
E_{PQ}^{\pm}=\frac{PQ\pm QP}{2\sqrt2},\qquad
PQ\in\{XY,XZ,YZ\},\qquad U(s)=e^{-isE_{PQ}^{\pm}}.
$$

The displayed Hermitian generators are Hilbert-Schmidt orthonormal.
Conjugation by $XX,YY,ZZ$ fixes the candidate, $H,\rho$ and the functional;
each normal generator reverses sign under at least one such symmetry.
Every normal first derivative therefore vanishes exactly, while invariance
annuls vertical derivatives. Distinct unordered Pauli pairs have distinct
sign characters, eliminating cross-pair Hessian entries. Factor exchange
diagonalizes each remaining $2\times2$ block into the $+$ and $-$ directions.
These facts cover the full normal space, not a restricted path family.

The compact symmetry action admits a normal slice to its orbit even when the
quotient has singular strata. Positive Hessian on that complete slice gives
a strict local minimum modulo the orbit. Finite stabilizers and the optional
swap add identifications, not missing tangent directions.

## Exact Curvatures and Certificate

For the Bell family $H_0=aXX+bYY+cZZ$, set $d_t=(a-b)t$ and $p_t=(a+b)t$.
The parity-block calculation gives

$$
\kappa_{XY}^+=-\frac1L\int_0^L\sin^2d_t
[\cos2d_t+(2+\cos4ct)\cos2p_t]\,dt.
$$

Exchange $d_t,p_t$ for $\kappa_{XY}^-$; permute axes for the other pairs.
At $(a,b,c)=(1,2,3)$, put $s_k=\operatorname{sinc}(kL)$,
$\operatorname{sinc}x=\sin x/x$, $\operatorname{sinc}0=1$. Exactly,

$$
\begin{aligned}
8\kappa_{XY}^+&=2-4s_2+7s_4-10s_6+5s_8+s_{16}-2s_{18}+s_{20},\\
8\kappa_{XY}^-&=2-8s_2+5s_4-4s_6+5s_8-2s_{10}+2s_{12}-2s_{14}+s_{16}+s_{20},\\
8\kappa_{XZ}^+&=2s_4-6s_8+5s_{12}-2s_{16}+s_{20},\\
8\kappa_{XZ}^-&=2-4s_4-4s_8+3s_{12}+2s_{16}+s_{20},\\
8\kappa_{YZ}^+&=2-4s_2+3s_4-2s_6+5s_8-8s_{10}+5s_{12}-2s_{14}+s_{16},\\
8\kappa_{YZ}^-&=2-10s_2+s_4-2s_6+5s_8-4s_{10}+5s_{12}+s_{16}+2s_{20}.
\end{aligned}
$$

[The certificate](finite_time_bell_certificate.py) reconstructs these
coefficients with Gaussian-integer matrix Laurent polynomials, represented
by real block matrices of arbitrary-precision integers. It does not import
the six displayed formulas. Denominators account for the normalized generators;
JSON direction labels are combinations of the base generators $-iPQ/2$.
The program verifies exact zero gradients, block structure and eigenvalues.

For frequency $k$, $(kL)^2=32k^2/7$ is rational. The sinc Taylor sum includes
indices $m=0,\ldots,192$ (degree 384); the next term bounds the decreasing
alternating tail. Signed rational interval arithmetic encloses each
integrated curvature with width below $10^{-80}$ and proves
$\kappa_i>7/100$ for all six directions. Their decimal displays, in the
order $XY+,XY-,XZ+,XZ-,YZ+,YZ-$, are
$(0.3669970823,0.4768343477,0.07253043194,0.2410781221,0.3434799134,0.4796490816)$.

The [record](finite_time_bell_certificate_results.json) stores exact Fourier
coefficients and verified thresholds; rational interval endpoints are
recomputed, not inferred from those rounded displays. Combined with the
normal-slice argument, this proves a quotient-strict local minimum with
entangled selected eigenstate. It refutes the proposed universal
finite-time strict-local-minimum extension, not the original interaction-cost
result. This is executable, internally reviewed evidence, not a formal
proof-assistant certificate or external peer review.

## Explicit Lower-Cost Competitor

For the same $H_0,\rho,L$, take

$$
U_{\rm prod}=\frac1{\sqrt2}
\begin{pmatrix}0&0&1&1\\1&1&0&0\\-1&1&0&0\\0&0&1&-1\end{pmatrix},
\quad U_{\rm prod}^\dagger H_0U_{\rm prod}=\operatorname{diag}(-6,0,2,4),
\quad U_{\rm prod}^\dagger\rho U_{\rm prod}=|00\rangle\langle00|.
$$

Its determinant is $-1$; $e^{i\pi/4}U_{\rm prod}$ is an equivalent $SU(4)$
representative. Integer identities in the certificate verify this basis map.
The exact costs are

$$
F_{\rm Bell}=\frac9{16}-\frac3{16}s_4-\frac5{32}(s_8+s_{12})
-\frac1{32}(s_{16}+s_{20}),\qquad F_{\rm prod}=\frac{1-s_4}{4}.
$$

They are approximately $0.55203175395687$ and $0.22761185052885$.
Rational bounds prove $F_{\rm Bell}-F_{\rm prod}>3/10$, hence
$F_{\rm Bell}-\min F_T>3/10$. No claim that the competitor itself is a
minimum is required. The Bell class fails every near-global tolerance
$\varepsilon\leq0.3$; neither the global minimizer nor its uniqueness is known.
The finite continuous cost has a nonempty compact argmin on the compact
quotient, but existence supplies no physical preference.

Simple energies here have repeated gaps. The
[infinite-time global product-minimizer result, Proposition 2(ii)](https://arxiv.org/html/2312.13386v2#S4)
uses nonresonance assumptions and does not classify these finite-time local
minima. Smoothness gives qualitative persistence of positivity and the cost
deficit under sufficiently small Bell-family/horizon changes retaining simple
energies; gap resonances can be detuned there. No quantitative perturbation
radius, arbitrary-model robustness, lifetime, or uniform long-time result is
certified. The cost gap is not a dynamical escape barrier.

## Conditional Recovery and Physical Failure

With an independently reset maximally mixed environment define

$$
\mathcal E_{U,t}(X)=\operatorname{Tr}_B[W_t(X\otimes I_B/d_B)W_t^\dagger].
$$

Its normalized Choi state in output/reference order is $J_t=Q_t/d$:
the Kraus operators $L_{\alpha\beta}=\langle\alpha|W_t|\beta\rangle/\sqrt{d_B}$
give $J_t=d_A^{-1}\sum_{\alpha\beta}|L_{\alpha\beta}\rangle\rangle
\langle\langle L_{\alpha\beta}|$. Unitarity makes $\mathcal E$ TP and unital.
This channel interpretation is established in
[Styliaris et al., Proposition 7 and Theorem 8](https://arxiv.org/html/2007.08570v3).

Let $P=\operatorname{Tr}J^2$ and $f_*$ be optimal single-use entanglement
fidelity for input $I_A/d_A$, an untouched reference and an A-only CPTP
decoder, without postselection. The Kraus Gram sum gives
$f_e(\mathcal E^\dagger\mathcal E)=P$. The adjoint is an allowed decoder
because $\mathcal E$ is unital, the maximally-mixed specialization of
[Barnum and Knill's transpose recovery, equation (12)](https://arxiv.org/html/quant-ph/0004088v2).
For any decoder $\mathcal D$,
$f_e(\mathcal D\mathcal E)=\operatorname{Tr}(J_{\mathcal E}J_{\mathcal D^\dagger})$;
$J_{\mathcal D^\dagger}$ is a positive trace-one matrix since $\mathcal D$ is TP.
Consequently

$$
P\le f_*\le\lambda_{\max}(J)\le\sqrt P,\qquad
1-F_T\le f_{\rm known}:=\frac1T\int_0^T f_*(\mathcal E_t)dt
\le\sqrt{1-F_T}.
$$

The last bounds require recorded time and a time-dependent decoder; Jensen's
inequality gives the upper bound. At the already fixed $T=8$, the exact
coefficient bounds imply $f_{\rm known}({\rm Bell})<0.670$ and
$f_{\rm known}({\rm prod})>0.772$. Thus the explicit competitor also wins
under optimal recovery in this particular task, not all possible tasks.
The operational checker imports the rational integrator and recorded Bell
coefficients; [run_checks.py](run_checks.py) first regenerates and matches them.

Equal purity is not equal optimal recovery. The additional fixed check uses
$\theta=\arccos(3^{-1/4})$, $c=\pi/4-\theta/2$,
$H=\theta\,{\rm SWAP}+c(ZI+IZ)$ and its unique singlet ground state.
At $t=1$, compare $I$ with the basis $(\Psi^-,\Psi^+,00,11)$.
The channels are a rotated depolarizing channel with shrinkage $1/\sqrt3$
and complete Z dephasing. Both have $P=1/2$, but
$f_*=(1+\sqrt3)/4$ and $1/2$, attained by explicit unitary decoders and
bounded above by their largest Choi eigenvalues. Ground-state entropies are
one and zero bits. This is an instantaneous example, not equal integrated
costs or an additional minimum.

For a fixed time law, $\bar J=\int w(t)J_tdt$ satisfies

$$
1-\operatorname{Tr}\bar J^2=
\int w(t)[1-\operatorname{Tr}J_t^2]dt+
\int w(t)\|J_t-\bar J\|_2^2dt.
$$

Discarding time therefore changes the task. For $H=ZI$ and equally likely
$t=0,\pi/2$, each known-time channel is unitary with $G=0$; the averaged
channel is $(X+ZXZ)/2$ with Choi purity $1/2$.
This two-point control is not the original uniform window.

Spectral prescriptions $T=c/s(H)$ can fix units without determining $c$,
time weighting, a preparation event, or an actual clock. A phase-resolution
window can diverge near split resonances; an externally timed probe requires
apparatus and an independent deadline. Neither supplies a physical ICC window.
The recovery task also assumes encoded probes, reset B, a usable time record,
and all A-only decoders. Candidate Choi inputs have equal AB marginal $I/d$
but different reference correlations: equal marginals do not prove equal access.

Finally, $V_s=e^{-isH}$ preserves the ground projector and lies in the
Hamiltonian centralizer. Hence $[V_s\mathcal A V_s^\dagger]=[\mathcal A]$
and the cost is constant: existing unitary transport is not motion between
inequivalent classes. A static preference postulate needs independent
justification; a relaxation/transition claim additionally needs dynamics,
initialization and a clock. None is provided here. No trapping, entropy reset,
thermodynamic arrow or cosmological applicability follows.

## Verification Scope

The second-variation diagnostic covers six fixed centered-RMS-normalized
Hamiltonians at $\tau=0.25,0.5,1,2,4,8$, using all 15 Pauli directions and
rank-computed orbit complements. It compares 64/128-node quadrature and
finite differences at $10^{-3},5\times10^{-4}$; positive floating-point
curvature alone is not its certificate. The separate exact program supplies
that certificate only for the fixed Bell example above.
Operational checks include identity/CNOT/SWAP and nine seeded controls in
$2\times2,2\times3,3\times2$; unequal dimensions test conventions, not scaling.
See the [reproduction guide](README.md) for recorded data, reruns, dependencies,
and internal AI-review limits. No optimizer or lattice campaign is involved.
