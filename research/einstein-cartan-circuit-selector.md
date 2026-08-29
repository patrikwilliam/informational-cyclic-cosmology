# An Einstein-Cartan-Inspired Restricted CAR Selector

## A Bounded Finite-Dimensional Example and Robustness Test

Author: Patrik William Pustejovsky

ORCID: [0009-0008-1618-6619](https://orcid.org/0009-0008-1618-6619)

Version: 0.1

Date: 10 August 2026

Status: companion technical note to ICC v0.1.3; exploratory finite-dimensional
result, not peer reviewed. It develops one possible effective realization of
the algebra-selection problem and states its limitations.

## Abstract

This note asks whether a Hamiltonian interaction-projection selector that fails
on the unrestricted finite factorization space can acquire strict competing
minima after the admissible family is restricted by fermionic and internal
Dirac-algebra structure. For a two-cell, eight-mode CAR system with a massless
Dirac link and an Einstein-Cartan-inspired axial-current contact term, the
restricted selector has momentum- and site-factorization branches separated by a
finite barrier. At the tested positive-coupling co-global point it admits an
isolated stationary ground state with nonzero factorization-dependent mode
entanglement. The branch structure and stationary contrast survive replacement
of the full-Fock Hilbert-Schmidt trace by the fixed four-particle-sector trace.
A first three-cell extension does not pass a boundary-independent robustness
gate: the open-chain kinetic endpoint is unstable, whereas the periodic ring
passes only a restricted numerical test. A four-cell periodic branch survives
the prescribed small twists, but a matched non-axial density contact passes the
same gate and obeys the same residual law. A bounded classification extends
that law to every nonzero contact in the declared translation-invariant onsite
quartic class. The result is therefore a bounded Hamiltonian-relative example
of generic kinetic-versus-onsite competition, not evidence for a scalable or
EC-specific selector. It neither derives the
restricted candidate family from continuum Einstein-Cartan dynamics nor
establishes an aeonic transition, cosmological entropy reset, or observable
prediction.

Reproducible calculations:

- [`ec_axial_selector_analysis.py`](./ec_axial_selector_analysis.py)
- [`ec_ground_state_certificate.py`](./ec_ground_state_certificate.py)
- [`ec_fixed_sector_selector.py`](./ec_fixed_sector_selector.py)
- [`ec_three_cell_selector.py`](./ec_three_cell_selector.py)
- [`three-cell-finite-gate.md`](./three-cell-finite-gate.md)
- [`ec_four_cell_selector.py`](./ec_four_cell_selector.py)
- [`ec_four_cell_boundary_phase.py`](./ec_four_cell_boundary_phase.py)
- [`ec_four_cell_matched_control.py`](./ec_four_cell_matched_control.py)
- [`four-cell-matched-control-gate.md`](./four-cell-matched-control-gate.md)
- [`ec_four_cell_onsite_closure.py`](./ec_four_cell_onsite_closure.py)
- [`four-cell-onsite-closure.md`](./four-cell-onsite-closure.md)

## 1. Question

Can a structurally restricted family of fermionic factorizations acquire two
competing minima from a relativistic kinetic term and the axial-current contact
channel associated with eliminating Einstein-Cartan (EC) torsion, without
putting entropy in the selector?

The answer is positive in the finite two-cell model below. The result is
kinematic and Hamiltonian-relative. It does not yet establish a cosmological
cycle, a Page-Wootters embedding, or a continuum EC transition.

## 2. Finite relativistic model

Take two spatial cells and four Dirac components per cell. The one-particle
space and fermionic Fock space are

$$
\mathfrak h=\mathbb C^2_{\mathrm{cell}}\otimes\mathbb C^4_{\mathrm{Dirac}},
\qquad
\mathcal H=\mathcal F(\mathfrak h),
\qquad
\dim\mathcal H=2^8=256.
$$

Let $c_{x a}$ annihilate component $a$ in cell $x$. In units where the link
spacing has been absorbed into the coefficients, define

$$
H(t,g)=tK+gQ,
$$

with the massless one-link Dirac kinetic operator

$$
K=-i\left(\psi_1^\dagger\alpha^1\psi_2
-\psi_2^\dagger\alpha^1\psi_1\right)
$$

and the normal-ordered axial-current contact operator

$$
Q=\sum_{x=1}^{2}
\left[
:\!\left(\psi_x^\dagger\gamma^5\psi_x\right)^2\!:
-\sum_{i=1}^{3}
:\!\left(\psi_x^\dagger\alpha^i\gamma^5\psi_x\right)^2\!:
\right].
$$

Thus $Q$ is the finite-mode version of the Lorentz contraction
$J_5^\mu J^5_\mu$. Integrating out algebraic, non-propagating torsion in EC
theory produces local four-fermion terms that include this axial-axial channel.
The sign and coefficient depend on conventions and on whether non-minimal
couplings are admitted. The selector below depends on $g^2$, so the sign of $g$
does not affect this finite selector branch diagram.

This is not a controlled non-relativistic approximation. The leading
non-relativistic limit of the Einstein-Cartan-Dirac equations does not retain a
torsion correction of this form.

## 3. Physically restricted candidate algebras

A general factorization of the 256-dimensional Hilbert space would be far too
permissive. Here the admissible transformations are required to

1. preserve the canonical anticommutation relations and fermion number; and
2. normalize the internal Dirac matrix algebra.

Writing

$$
\mathfrak D=I_2\otimes M_4(\mathbb C),
$$

the second condition is the basis-invariant requirement

$$
V\mathfrak D V^\dagger=\mathfrak D.
$$

Every automorphism of $M_4(\mathbb C)$ is inner. Therefore a unitary satisfying
this condition has the form

$$
V=W\otimes S,
\qquad W\in U(2),\quad S\in U(4).
$$

Indeed, after removing the inner action $S$, the remaining unitary commutes
with $\mathfrak D$ and hence belongs to its commutant $M_2(\mathbb C)\otimes
I_4$. The common $S$ is an internal basis change within each candidate cell; it
does not change the subsystem split. Thus each induced cell decomposition has a
representative $W\otimes I_4$. Under the stated normalizer condition, the
unordered candidate decompositions form

$$
U(2)/\left((U(1)\times U(1))\rtimes S_2\right)
\simeq \mathbb{RP}^2.
$$

This is the complete image of the number-preserving one-particle normalizer in
the space of unordered cell decompositions, not an arbitrary one-parameter
ansatz. Equivalently, a candidate cell split is represented by an unoriented
Bloch axis

$$
\mathbf n=(n_x,n_y,n_z)\in S^2,
\qquad \mathbf n\sim-\mathbf n.
$$

This admissibility condition is a defining structural assumption. It is not
derived from the EC contact term. It excludes Bogoliubov transformations and
unitaries that do not preserve the internal matrix-algebra factor. A continuum
theory would have to derive the corresponding restriction independently, not
merely impose it.

Fermionic mode factors are properly combined with a graded tensor product,

$$
\mathcal F(\mathfrak h_+\oplus\mathfrak h_-)
\simeq
\mathcal F(\mathfrak h_+)\,\widehat\otimes\,
\mathcal F(\mathfrak h_-).
$$

The finite calculation fixes a Jordan-Wigner ordering to represent this as a
$16\times16$ matrix tensor product. All Hamiltonians and candidate unitaries in
the calculation are parity even. The one-factor projection of an even operator
has no odd local component, so the interaction cost agrees with projection onto
the even local Hamiltonian sectors in this setting. A continuum CAR-algebra
formulation should state this without choosing a Jordan-Wigner representation.

## 4. Exact interaction-projection cost on this family

For each $\mathbf n$, lift $W$ to Fock space and use the same
Hilbert-Schmidt projection onto Kronecker-sum Hamiltonians as in ICC v0.1.2.
The two factors have dimensions $16\times16$.

The finite CAR expansion makes the orientation dependence transparent. In cell
Pauli notation the kinetic term carries $\sigma_y$, so its nonlocal residual is
$512(1-n_y^2)$. For the contact term, the squared residual depends only on
$u=n_z^2$ and the CAR expansion is a polynomial of degree at most two in $u$.
Its values at $u=0,1/2,1$ are respectively $4608,2688,0$, fixing it uniquely as
$1536(1-u)(3+u)$. The same trace expansion makes the kinetic-contact residual
cross term vanish. The selector defined in ICC v0.1.2 removes the scalar part
of the Hamiltonian in its denominator. Here $\operatorname{Tr}K=0$ and
$\operatorname{Tr}Q/256=4$. Define $\widetilde Q=Q-4I$. Direct CAR traces give

$$
\lVert K\rVert_2^2=512,
\qquad
\lVert \widetilde Q\rVert_2^2=8192,
\qquad
\langle K,\widetilde Q\rangle_{\mathrm{HS}}=0,
$$

and, relative to the candidate split $\mathbf n$,

$$
\lVert K_{\mathrm{int}}(\mathbf n)\rVert_2^2
=512(1-n_y^2),
$$

$$
\lVert Q_{\mathrm{int}}(\mathbf n)\rVert_2^2
=1536(1-n_z^2)(3+n_z^2),
$$

$$
\langle K_{\mathrm{int}}(\mathbf n),
Q_{\mathrm{int}}(\mathbf n)\rangle_{\mathrm{HS}}=0.
$$

Consequently, with $r=g/t$ and $t\neq0$,

$$
\boxed{
C(\mathbf n;r)=
\frac{
(1-n_y^2)+3r^2(1-n_z^2)(3+n_z^2)
}{1+16r^2}
}.
$$

Entropy does not appear in this functional.

The Hilbert-Schmidt trace weights every vector in the full Fock space equally,
including all particle-number sectors. That is a convenient continuation of
the v0.1.2 test selector, not a consequence of EC dynamics. A fixed-charge,
thermal, or state-weighted inner product would require a new orthogonal
projection and may change every numerical coefficient below. In a fixed total
charge sector the subsystem structure also becomes a direct sum with a center,
not a simple $16\times16$ factorization.

## 5. Complete restricted branch diagram

For fixed $n_z$, the kinetic contribution is minimized by $n_x=0$ and
$n_y^2=1-n_z^2$. Setting $u=n_z^2\in[0,1]$, the numerator becomes

$$
N(u)=u+3r^2(3-2u-u^2).
$$

Since

$$
N''(u)=-6r^2\leq0,
$$

the global minimum is always at an endpoint. The endpoint costs are

$$
C_{\mathrm{site}}(r)=\frac{1}{1+16r^2},
\qquad
C_{\mathrm{mom}}(r)=\frac{9r^2}{1+16r^2}.
$$

Therefore

$$
\begin{array}{lll}
|r|<1/3 &\Longrightarrow& \mathbf n=\pm\hat{\mathbf y}
\quad\text{(phase-momentum split)},\\[2mm]
|r|>1/3 &\Longrightarrow& \mathbf n=\pm\hat{\mathbf z}
\quad\text{(site split)}.
\end{array}
$$

At $|r|=1/3$, both endpoint minima have

$$
C_{\min}=\frac{9}{25}.
$$

They are not joined by a flat direction. The intervening saddle on the
$yz$ great circle has $n_y^2=n_z^2=1/2$ and

$$
C_{\mathrm{barrier}}=\frac{39}{100},
\qquad
\Delta C=\frac{3}{100}.
$$

The local-stability thresholds differ from the equal-cost point:

$$
\begin{aligned}
\text{momentum split stable:}&\quad r^2<\frac16,\\
\text{site split stable:}&\quad r^2>\frac1{12}.
\end{aligned}
$$

For example, using tangent coordinates at the two endpoints, the unnormalized
numerator has the local expansions

$$
N_{\mathrm{mom}}=
9r^2+x^2+(1-6r^2)z^2+O(4),
$$

$$
N_{\mathrm{site}}=
1+12r^2x^2+(12r^2-1)y^2+O(4).
$$

At $r^2=1/9$, every displayed quadratic coefficient is positive, proving that
both co-global endpoints are strict minima on the restricted quotient.

Hence there is a bistability interval

$$
\boxed{
\frac1{\sqrt{12}}<|r|<\frac1{\sqrt6}
}.
$$

This finite barrier and the distinct spinodals permit hysteresis under a local
update law. Hysteresis is not implied if the system is assumed to jump
instantaneously to the global minimum.

## 6. CAR circuit geometry

On the $yz$ great circle, write

$$
\mathbf n(\alpha)=(0,\sin 2\alpha,\cos 2\alpha),
\qquad 0\leq\alpha\leq\frac\pi4.
$$

The change is generated by four parallel fermionic beam splitters,

$$
U(\alpha)=\exp\!\left[
i\alpha\sum_{a=1}^{4}
\left(c_{1a}^\dagger c_{2a}+c_{2a}^\dagger c_{1a}\right)
\right].
$$

The four principal angles between the corresponding one-particle subspaces are
all $|d\alpha|$. With the standard quadratic Grassmann/F2 convention,

$$
ds_{\mathrm{CAR}}^2=4\,d\alpha^2,
\qquad
d_{\mathrm{CAR}}(\mathrm{site},\mathrm{momentum})=\frac\pi2.
$$

Along this path the static cost and its derivative are

$$
C(\alpha;r)=
\frac{
\cos^2 2\alpha
+3r^2\sin^2 2\alpha\left(3+\cos^2 2\alpha\right)
}{1+16r^2},
$$

$$
\partial_\alpha C
=\frac{-2\sin 4\alpha
\left[1-6r^2\left(1+\cos^2 2\alpha\right)\right]
}{1+16r^2}.
$$

This suggests a dynamical extension rather than a new static entropy selector:

$$
I[\alpha]=\int d\tau\,
\left[
2\mu\dot\alpha^2
+\Lambda C\bigl(\alpha;r(\chi(\tau))\bigr)
\right],
$$

or an overdamped relational update law

$$
4\Gamma\dot\alpha
=-\Lambda\,\partial_\alpha C.
$$

Here $\chi$ must be an intrinsic clock variable, such as a relational density;
it cannot be an external aeon label. The circuit term penalizes rapid changes
of factorization and allows the finite barrier to carry branch memory. It does
not by itself determine $\mu$, $\Gamma$, $\Lambda$, quantum tunnelling rates, or
the correct complexity metric. Calling it a derived law would therefore be
premature.

## 7. EC scaling and the cutoff problem

In continuum EC theory, eliminating non-propagating torsion produces a
dimension-six four-fermion operator with a coefficient of gravitational
strength. For a cell scale $\ell$,

$$
t\sim\ell^{-1},
\qquad
g\sim\kappa\ell^{-3},
\qquad
r=\frac gt\sim\frac{\kappa}{\ell^2},
$$

up to discretization and convention-dependent constants. Thus the contact term
becomes relatively important as the relational density increases.

The same scaling is also the main warning. Reaching $r=O(1)$ generally means
approaching a Planckian regime, where a low-energy EC derivative expansion and
this two-cell truncation are not controlled. The value $r_c=1/3$ is exact for
the normalized toy Hamiltonian; it is not a prediction of a physical reset
density.

Microscopic EC calculations can produce a cosmological bounce, but they do not
derive this algebra selector or its circuit dynamics.

Palle's 2026 EC paper was one motivation for testing an EC interface, but its
role is contextual only. It studies gauge-invariant linear perturbations in a
macroscopic EC/Weyssenhoff-fluid cosmology and adopts a phenomenological torsion
history as a function of redshift. It does not derive the axial-current lattice
Hamiltonian, the admissible CAR family, the selector, or the circuit update law
used here. The finite mechanism in this note should therefore not be described
as a consequence of Palle's model.

## 8. Entropy and stationarity diagnostics

Let $d_{+,a}$ denote the four modes in the $+\hat{\mathbf y}$ factor and take

$$
|\Psi_+\rangle=\prod_{a=1}^{4}d_{+,a}^\dagger|0\rangle.
$$

For the same state,

$$
S_{\mathrm{site}}(|\Psi_+\rangle)=4\ \text{bits},
\qquad
S_{\mathrm{mom}}(|\Psi_+\rangle)=0.
$$

This is a maximal $16\times16$ fermionic **mode-entanglement** contrast,
obtained only after the Hamiltonian selected the candidate structures. It is
not automatically the operationally extractable entanglement under a local
fermion-parity superselection rule; Section 12.3 gives separate sector-resolved
diagnostics for the stationary states.

However,

$$
\langle H(t=1,g)\rangle=4g,
\qquad
\operatorname{Var}_{\Psi_+}H(t=1,g)=48g^2.
$$

Therefore this illustrative state is not stationary for $g\neq0$. At $g=0$ it
lies in a highly degenerate kinetic-energy eigenspace, not an isolated
nondegenerate eigenstate.

The Hamiltonian itself nevertheless supplies a better state. Full numerical
diagonalization of the $256\times256$ matrix at the equal-cost point,

$$
H_c=K+\frac13Q,
$$

gives a unique ground state $|\Omega_c\rangle$ with

$$
E_0\simeq-4.11560796875,
\qquad
E_1-E_0\simeq0.620514177337.
$$

The uniqueness and isolation can also be certified exactly. In a simultaneous
chirality/spin basis followed by a Fock-basis phase gauge, $3H_c$ is a real
integer symmetric matrix. Particle number, total chirality, and total spin
along the link split it into 65 blocks, the largest of dimension 18. Exact
rational $LDL^\mathsf{T}$ inertia gives exactly one eigenvalue of $3H_c$ below
$-21/2$. In the only block containing that eigenvalue, the characteristic
polynomial contains the factor

$$
p(\lambda)=
\lambda^4-20\lambda^3-144\lambda^2+3008\lambda-1792.
$$

Exact sign evaluation brackets its low root as

$$
-\frac{12347}{1000}
<\lambda_0<
-\frac{6173}{500}.
$$

It follows that the ground state is simple and

$$
E_1-E_0>\frac{923}{1500}\simeq0.615333.
$$

The supplied certificate constructs this integer matrix directly from exact
Gaussian-integer CAR data, without rounding, and then cross-checks it against
the independent NumPy Hamiltonian construction.

The eigenvector residual in the supplied calculation is below $5\times10^{-15}$.
It lies in the four-particle sector and has

$$
S_{\mathrm{site}}(|\Omega_c\rangle)
\simeq3.01251822001\ \text{bits},
$$

$$
S_{\mathrm{mom}}(|\Omega_c\rangle)
\simeq1.20884898928\ \text{bits},
$$

so that

$$
\Delta S_{\mathrm{mode}}
\simeq1.80366923073\ \text{bits}.
$$

Thus the explicit critical Hamiltonian has, within the stated CAR family,

1. two strict co-global factorization minima;
2. a stationary isolated pure state; and
3. a nonzero entropy contrast not used by the selector.

The unequal entropies also show that the two factorizations cannot be related
by local basis changes, factor exchange, or a symmetry preserving both $H_c$
and the ground-state projector, since all such equivalences preserve the
relevant Schmidt spectrum.

The mode-entropies are still numerical rather than interval-certified. Their
$1.8$-bit separation is much larger than the observed numerical error, but a
formal computer-assisted proof of the entropy inequality has not been supplied.

A 121-point numerical scan across the open bistability interval found no loss
of this stationary contrast. The smallest sampled ground-state gap was
$0.4949359$, and the smallest sampled entropy contrast was $1.3243883$ bits,
both near the upper spinodal. This scan supports, but does not prove, persistence
throughout the interval. Independently, continuity of an isolated eigenstate
and of the two positive Hessians guarantees persistence in some open
neighborhood of the critical point.

## 9. Relation to the v0.1.2 no-go result

There is no contradiction with the preliminary ICC no-go argument. That result
varies over the full unitary factorization space. The strict minima here are
strict only within the Dirac-algebra-normalizing, number-preserving CAR family.
The directions used by the general no-go argument are not all admissible in
this restricted space.

The critical ground state therefore gives an explicit finite construction for
a **restricted** version of the problem, with the entropy contrast evaluated
numerically. It is not a counterexample to the v0.1.2 statement. The burden is
now especially clear: the narrower admissible family must follow from physical
structure that is independently present in the theory. If it is imposed merely
to remove the no-go directions, the escape is circular.

For the cosmological application, a completed model must additionally derive
$r(\chi)$ from intrinsic relational data, construct a globally stationary
clock-plus-system state, and obtain $H(t,g(\chi))$ as a conditional Hamiltonian.
Without those steps this remains a proof of mathematical possibility inside a
selected finite model.

## 10. Controlled perturbation check

Two one-body perturbations can be handled exactly:

$$
H_\delta=\delta(N_1-N_2),
\qquad
H_m=m\sum_x\psi_x^\dagger\gamma^0\psi_x.
$$

The uniform mass term is local in every common-cell factorization and changes
only the normalization of the cost. The detuning adds

$$
512\delta^2(1-n_z^2)
$$

to the unnormalized interaction cost and is orthogonal to the kinetic and
contact residuals. For $|\delta|<|t|$, the transition and bistability survive:

$$
g_c^2=\frac{t^2-\delta^2}{9},
$$

$$
\frac{t^2-\delta^2}{12}<g^2<\frac{t^2-\delta^2}{6}.
$$

This establishes stability against these perturbations only. It is not a
general robustness theorem for larger lattices or arbitrary EC-compatible
operators.

## 11. Fixed-particle-number gate

The full-Fock Hilbert-Schmidt inner product in Section 4 uses

$$
\operatorname{Tr}_{\mathcal H}(X)
=\sum_{N=0}^{8}\operatorname{Tr}_{\mathcal H_N}(P_NXP_N).
$$

It weights orthonormal Fock-space basis states equally, not particle-number
sectors equally. In terms of normalized sector traces, sector $N$ carries
weight $\binom8N/256$. Problem A replaces the full-Fock trace by the trace on
the four-particle sector, which contains the stationary ground state used
above:

$$
\mathcal H_{N=4}
=\bigoplus_{k=0}^{4}
\left(\wedge^k\mathfrak h_+\right)
\otimes
\left(\wedge^{4-k}\mathfrak h_-\right),
\qquad
\dim\mathcal H_{N=4}=70.
$$

Let $P_4$ be the total-number projector and $N_\pm$ the factor-number
operators. The local Hamiltonian subspace is fixed independently of $H$ and
$\mathbf n$ as

$$
\mathfrak L_4=
\left\{
P_4\left(A_+\widehat\otimes I+I\widehat\otimes A_-\right)P_4:
[A_+,N_+]=[A_-,N_-]=0
\right\}.
$$

It has dimension $135$. In the charge block with dimensions
$d_k=\binom4k$ and $d_{4-k}$, its orthogonal projection is

$$
\Pi_k(X)=
\frac{\operatorname{Tr}_{-}X}{d_{4-k}}\otimes I
+I\otimes\frac{\operatorname{Tr}_{+}X}{d_k}
-\frac{\operatorname{Tr}X}{d_kd_{4-k}}I,
$$

while off-diagonal charge blocks project to zero. This automatically handles
the common particle-number center without counting its parametrization kernel
as extra local directions. The implementation verifies idempotence and
Hilbert-Schmidt orthogonality before evaluating the selector.

In this sector $\operatorname{Tr}K=0$ and
$\operatorname{Tr}Q/70=24/7$. With
$\widetilde Q_4=Q-(24/7)I_{70}$, the centered traces give

$$
\lVert K\rVert_{2,4}^2=160,
\qquad
\lVert \widetilde Q_4\rVert_{2,4}^2=\frac{15744}{7},
\qquad
\langle K,\widetilde Q_4\rangle_{2,4}=0,
$$

and

$$
\lVert K_{\mathrm{int}}(\mathbf n)\rVert_{2,4}^2
=160(1-n_y^2),
$$

$$
\lVert Q_{\mathrm{int}}(\mathbf n)\rVert_{2,4}^2
=24(1-n_z^2)(71+25n_z^2),
$$

with a vanishing residual cross term. The factor $1/70$ in the normalized
sector trace cancels from the ratio, so

$$
\boxed{
C_4(\mathbf n;r)=
\frac{
160(1-n_y^2)+24r^2(1-n_z^2)(71+25n_z^2)
}{160+(15744/7)r^2}
}.
$$

For fixed $n_z$, the minimum again has $n_x=0$. Writing $u=n_z^2$, the
unnormalized numerator is a concave quadratic,

$$
N_4(u)=160u+24r^2(1-u)(71+25u),
$$

so every global minimum is at the momentum or site endpoint. Their exchange
occurs at

$$
|r_c|=\sqrt{\frac{20}{213}}\simeq0.3064257065.
$$

The two strict local minima coexist in the interval

$$
\sqrt{\frac5{72}}<|r|<\sqrt{\frac{10}{69}}.
$$

At the transition the midpoint $u=1/2$ is the barrier and

$$
C_{4,\min}=\frac{497}{1153},
\qquad
C_{4,\mathrm{barrier}}=\frac{2163}{4612},
\qquad
\Delta C_4=\frac{175}{4612}.
$$

At the positive branch $r=r_c$, full numerical diagonalization gives a
numerically nondegenerate ground state in the four-particle sector with

$$
E_0\simeq-4.00762869277,
\qquad
E_1-E_0\simeq0.678109892996,
$$

$$
S_{\mathrm{site}}\simeq3.12434200135\ \text{bits},
\qquad
S_{\mathrm{mom}}\simeq1.11702420207\ \text{bits},
$$

and hence

$$
\Delta S_{\mathrm{mode}}\simeq2.00731779928\ \text{bits}.
$$

A 121-point scan through the fixed-sector bistability interval found a minimum
sampled gap of $0.5359112$ and a minimum sampled entropy contrast of
$1.4856425$ bits. These are numerical checks, not interval certificates.

**Gate verdict:** the two-branch selector, its finite barrier, and a stationary
entropy contrast survive the fixed-$N=4$ Hilbert-Schmidt weighting. The result
therefore is not confined to the unrestricted full-Fock weighting. This verdict
does not cover Gibbs/state-weighted norms, larger lattices, or continuum QFT.

The calculation is reproduced by
[`ec_fixed_sector_selector.py`](./ec_fixed_sector_selector.py).

## 12. Adversarial finite controls

Two controls test which parts of the result are structural and which are
specific to the chosen EC-inspired channel.

### 12.1 Other fixed-number sectors

Repeating the local projection in every nontrivial number sector gives

$$
\lVert K_{\mathrm{int}}(\mathbf n)\rVert_{2,N}^2
=8\binom{6}{N-1}(1-n_y^2),
$$

and, for $2\leq N\leq6$,

$$
\lVert Q_{\mathrm{int}}(\mathbf n)\rVert_{2,N}^2
=4\binom{4}{N-2}(1-n_z^2)(71+25n_z^2),
$$

with a zero residual cross term. The contact residual vanishes for $N=1$ and
$N=7$. For $2\leq N\leq6$, the endpoint exchange occurs at

$$
r_{c,N}^2=
\frac{2\binom{6}{N-1}}{71\binom{4}{N-2}}.
$$

Thus the two-minimum geometry occurs separately in several fixed-number
sectors. The stationary-state condition is less generic: numerical
diagonalization at the positive sector-specific exchange point finds a degenerate
sector ground space for $N=2,3,5,6$. Only $N=4$ passes the isolated-ground-state
gate in this scan, with gap $0.678109892996$. Entropy values chosen from the
degenerate sectors are basis-dependent and are not evidence for a robust
contrast.

### 12.2 Non-EC onsite-contact null model

Replace the axial-current operator by the spin-independent onsite contact

$$
Q_{\mathrm{dens}}
=\sum_x :N_x^2:
=\sum_x N_x(N_x-1).
$$

In the full Fock space its interaction residual is

$$
\lVert (Q_{\mathrm{dens}})_{\mathrm{int}}(\mathbf n)\rVert_2^2
=192(1-n_z^2)(3+n_z^2),
$$

which has exactly the same angular dependence as the EC-inspired residual,
with a different overall coefficient. At equal endpoint cost it produces two
strict minima and, in the four-particle sector, an isolated ground state with a
positive site-versus-momentum mode-entanglement contrast. The fixed-$N=4$
residual is likewise a concave endpoint-selecting polynomial,

$$
\lVert (Q_{\mathrm{dens}})_{\mathrm{int}}(\mathbf n)\rVert_{2,4}^2
=(1-n_z^2)(162+126n_z^2).
$$

This control removes any claim of EC specificity from the finite branch
geometry. The calculation demonstrates a generic competition between a
hopping term that is local in a momentum split and an onsite interaction that
is local in a site split. The EC axial channel is one concrete realization, not
an explanation or prediction of the selector mechanism.

### 12.3 Local superselection rules

The raw Schmidt entropy is fermionic mode entanglement. For a fixed total
charge, an operationally stricter diagnostic resolves the reduced state into
local-number or local-parity sectors. For sector projectors $P_s$, define

$$
E_{\mathrm{SSR}}=\sum_s p_s
S\!\left(\frac{P_s\rho_A P_s}{p_s}\right),
\qquad
p_s=\operatorname{Tr}(P_s\rho_A).
$$

At the positive-coupling full-Fock EC exchange point, the site-minus-momentum
contrast remains
$0.698734$ bits under local-number superselection and $0.995665$ bits under
local-parity superselection. At the positive fixed-$N=4$ exchange point the
corresponding
contrasts are $0.800293$ and $1.162493$ bits. The finite contrast is therefore
not entirely a local-number-fluctuation artifact. This probability-weighted
within-sector entropy excludes the Shannon entropy of the sector label and is
used here only as a pure-state diagnostic, not as a general mixed-state
entanglement measure. The local-number construction follows
[Wiseman and Vaccaro](https://arxiv.org/abs/quant-ph/0210002); fermionic
subsystems and parity-superselection subtleties are reviewed by
[Szalay et al.](https://arxiv.org/abs/2006.03087). Neither quantity is a
thermodynamic or gravitational entropy.

These controls are reproduced by
[`ec_selector_adversarial_controls.py`](./ec_selector_adversarial_controls.py)
and
[`ec_superselection_controls.py`](./ec_superselection_controls.py).

## 13. Three-cell finite-size stress test

The first size extension uses three cells in the half-filled fixed sector
$\bigwedge^6\mathbb C^{12}$ and the full restricted cell-factorization space

$$
U(3)/(U(1)^3\rtimes S_3).
$$

Its six continuous tangent directions are tested at both the site and
kinetic-eigenmode endpoints. The one-cell operator subspace has exactly rank
207: its 210 matrix-unit generators have three exact fixed-sector relations,
and row reduction of their integer Gram matrix modulo $1{,}000{,}003$ gives
rank 207.

At the separately tuned equal-endpoint coupling, the open-chain kinetic
endpoint has minimum Hessian eigenvalue $-0.0465277$ and an explicit descent
direction. Multi-start optimization finds a lower mixed factorization with
cost 0.4413803, below the endpoint value 0.4529795. The selected open-chain
ground space is threefold degenerate, so no arbitrary eigenvector entropy is
used as evidence.

For the periodic ring, the minimum site and kinetic Hessian eigenvalues are
0.4866812 and 0.2433404. A strengthened search over 32 Haar samples and eight
optimized random starts found no value below the endpoint cost 0.4717833. The
ground state is isolated by a gap 0.2033920 and has positive mode,
local-number-SSR, and local-parity-SSR contrasts. This is a restricted
numerical result, not a proof of global minimality.

The same endpoint-Hessian pattern occurs at the tested fillings
$N=4,5,6,7,8$, while a non-axial onsite density contact also produces strict
competing endpoints. More fundamentally, the three-cell open chain has two
links and the ring has three, so their difference is not a small boundary
perturbation. The ring's central-difference spectrum
$\{-\sqrt3,0,+\sqrt3\}$ is also specific to odd size. The combined result is
therefore a boundary-independent robustness failure, not evidence that
periodic boundaries rescue the EC/CAR selector. That comparison alone gives no
larger-size conclusion.

The complete calculation and its independent reviews are
[`three-cell-finite-gate.md`](./three-cell-finite-gate.md),
[`ec_three_cell_selector.py`](./ec_three_cell_selector.py),
[`three-cell-physics-review.md`](../feedback/three-cell-physics-review.md), and
[`three-cell-mathematical-review.md`](../feedback/three-cell-mathematical-review.md).

## 14. Four-cell phase and interaction-specificity gate

The even-size periodic follow-up uses the half-filled sector
$\bigwedge^8\mathbb C^{16}$ and the complete restricted cell-mixing quotient

$$
U(4)/(U(1)^4\rtimes S_4).
$$

The low-body implementation evaluates exact fixed-sector Hilbert-Schmidt
overlaps without constructing a dense $12{,}870\times12{,}870$ matrix. Dense
low-filling tests, direct half-filled occupation-mask actions, exact local-rank
relations, quotient invariance, and finite-difference step audits validate the
calculation.

The periodic axial site and resolved kinetic representatives are strict at the
equal-endpoint coupling $g_0=0.4298279139$. Under the fixed transport
$U_\phi=G(\phi)U_0$, both representatives pass at
$\phi=0,\pi/16,\pi/8$. The transported branch remains stationary but first
loses positive curvature on the prescribed grid at $\phi=\pi/2$.

The prospective control uses only

$$
Q_{\mathrm{dens}}=\sum_xN_x(N_x-1),
$$

a spinor-blind onsite density contact rather than the selected axial-current
contraction. It is not an affine copy of the axial contact after fixed-sector
centering. At its own equal-endpoint coupling, it nevertheless passes the same
periodic and small-twist gates and remains strict one grid point farther.

For both contacts, the transported residual components satisfy

$$
R_{\mathrm{branch}}=
\left(A\sin^2\frac{\phi}{4},B,0\right),
\qquad
g_0^2B=A,
$$

to errors below $7.0\times10^{-10}$. Both therefore have the retuned equal-cost
root $g_*(\phi)=g_0\cos(\phi/4)$. This common law identifies the positive branch
as shared finite selector kinematics, not an EC-specific signature.

The full onsite-contact closure makes that statement exact within the declared
finite class. For
$q=q^\dagger\in\operatorname{Herm}(\Lambda^2\mathbb C^4)$ repeated on every
cell, let $(\beta,\chi)$ parameterize the periodic kinetic zero-mode basis and
$x=\sin^2\beta\cos^2\chi$. Then

$$
B_q(\beta,\chi)=B_q(0,0)-p(q)x-r(q)x^2,
$$

where $p$ and $r$ are positive definite on the full 36-real-dimensional contact
space. Every $q\neq0$ therefore selects $x=1$ and the balanced zero modes,
which imply

$$
R_{\mathrm{branch}}(\phi)
=\left(A\sin^2\frac{\phi}{4},B(q),0\right).
$$

The result covers arbitrary Hermitian onsite pair scattering, not only diagonal
contacts. It remains conditional on translation invariance, the fixed
half-filled projection, and the declared periodic resolver.

Here "non-axial" is intentionally narrower than "non-EC": generalized torsion
effective theories may contain several four-fermion channels. The comparison
tests only whether the chosen axial contraction is distinguished by this
selector.

The full protocol, calculation, and separate reviews are
[`four-cell-matched-control-gate.md`](./four-cell-matched-control-gate.md),
[`ec_four_cell_matched_control.py`](./ec_four_cell_matched_control.py),
[`four-cell-matched-control-mathematical-review.md`](../feedback/four-cell-matched-control-mathematical-review.md),
and
[`four-cell-matched-control-physics-review.md`](../feedback/four-cell-matched-control-physics-review.md).
The full onsite classification and its review are
[`four-cell-onsite-closure.md`](./four-cell-onsite-closure.md),
[`ec_four_cell_onsite_closure.py`](./ec_four_cell_onsite_closure.py), and
[`four-cell-onsite-closure-mathematical-review.md`](../feedback/four-cell-onsite-closure-mathematical-review.md).

## 15. What has and has not been achieved

Demonstrated in the finite model:

- a finite truncation of the axial-current contact channel and a non-axial onsite
  control that separates generic selector behavior from EC-specific claims;
- a non-entropic Hamiltonian cost on a specified, structurally characterized
  CAR family;
- two strict competing minima, an exact transition, and a finite barrier in the
  two-cell model;
- a natural finite-dimensional circuit metric and a metastability window;
- a maximal kinematic entropy contrast for one fixed state;
- an exactly certified isolated, gapped stationary ground state with a
  numerically evaluated $1.80367$-bit mode-entanglement contrast at the
  positive-coupling co-global point;
- survival of the two-branch diagram and a numerically isolated stationary
  entropy contrast under fixed-$N=4$ Hilbert-Schmidt weighting;
- positive stationary contrast after local-number and local-parity
  superselection;
- survival under a uniform mass and sufficiently small cell detuning;
- failure of boundary-independent robustness in the first three-cell size
  extension, with an exact local-subspace rank certificate and reproducible
  numerical Hessians;
- four-cell periodic small-twist persistence followed by a full-grid curvature
  failure;
- failure of the prospective four-cell EC-specificity gate because an
  independent density contact reproduces the primary branch behavior; and
- analytic closure showing that every nonzero contact in the declared
  translation-invariant onsite quartic class shares the transported residual
  law.

Not demonstrated:

- a derivation from the EC field equations on a dynamical spacetime;
- any evidence that the competing-minimum geometry is specific to EC rather
  than generic kinetic-versus-onsite locality competition;
- validity at the Planckian strength required by the finite transition;
- a globally stationary Page-Wootters state producing the conditional model;
- interval-certified verification of the reported critical ground-state
  entropy contrast;
- a unique circuit action or algebra-update law;
- persistence at arbitrary cell count or across boundary conditions, in QFT
  local algebras, or under all allowed perturbations;
- persistence under a Gibbs or other state-weighted replacement for the
  Hilbert-Schmidt norm;
- a cosmological observable or a falsifiable prediction.

## 16. Hand-back to the main ICC program

The two-cell restricted gate passes, so that construction can be retained as a
bounded mathematical selector example. The non-axial onsite-contact controls,
the three-cell boundary-independent robustness failure, and the four-cell
specificity failure prevent interpreting it as evidence for a distinct or
scalable EC mechanism. The full onsite closure additionally proves that further
sampling inside the same finite contact class cannot change that conclusion.
This is the stopping point for the branch. The
model-independent ICC priorities remain the
definition of subalgebra-relative entropy, a non-circular general selector
principle, and an observable distinction from existing cyclic or bounce
cosmologies.

A relational-clock construction remains a deferred extension. It would require
a self-adjoint global constraint
$\mathcal H_{\mathrm{tot}}$ and a normalizable stationary state
$|\Psi\rangle$ such that conditioning on an intrinsic clock $\chi$ yields a
physically derived Hamiltonian and selector while the same global state
exhibits a nonzero subalgebra-relative entropy contrast. It would first need to
replace or repair the non-robust finite CAR selector without inserting the
branch, factorization, or entropy contrast into the clock boundary data.

Such a construction could connect the finite branch diagram to ICC, but it
should not precede the model-independent work above.

## References

- D. Diakonov, A. G. Tumanov, and A. A. Vladimirov,
  [Low-energy general relativity with torsion: a systematic derivative
  expansion](https://arxiv.org/abs/1104.2432), 2011/2012.
- S. Lucat and T. Prokopec,
  [Cosmological singularities and bounce in Cartan-Einstein
  theory](https://arxiv.org/abs/1512.06074), 2015/2017.
- D. Palle,
  [Einstein-Cartan cosmology and the $S_8$
  problem](https://arxiv.org/abs/2502.20425), v4, 2026. Contextual comparison
  only; it does not derive the selector studied here.
- S. Khanapurkar et al.,
  [Non-relativistic limit of Einstein-Cartan-Dirac
  equations](https://arxiv.org/abs/1804.04434), 2018.
- S. M. Carroll and A. Singh,
  [Quantum Mereology: Factorizing Hilbert Space into Subsystems with
  Quasi-Classical Dynamics](https://arxiv.org/abs/2005.12938), 2020/2021.
- M. A. Nielsen,
  [A geometric approach to quantum circuit lower
  bounds](https://arxiv.org/abs/quant-ph/0502070), 2005.
- L. Hackl and R. C. Myers,
  [Circuit complexity for free fermions](https://arxiv.org/abs/1803.10638),
  2018.
- S. Szalay et al.,
  [Fermionic systems for quantum information
  people](https://arxiv.org/abs/2006.03087), 2021.
- H. M. Wiseman and J. A. Vaccaro,
  [The entanglement of indistinguishable particles shared between two
  parties](https://arxiv.org/abs/quant-ph/0210002), 2003.
