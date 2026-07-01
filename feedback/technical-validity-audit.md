# Technical-Validity Audit

Audit date: 2026-07-01

## Scope

This audit checks whether the manuscript's definitions, equations, and stated
conclusions are internally consistent. It is not expert peer review, a proof of
physical viability, or validation of the speculative cosmology.

## Overall verdict

After the corrections recorded below, the manuscript is internally coherent as
a schematic finite-dimensional research proposal. Its toy model establishes a
standard kinematic possibility: one fixed pure state can induce different local
entropies under different tensor-product structures. It does not establish that
such a change occurs cosmologically or that either structure is physically
preferred.

The proposal is not yet a working physical theory. Its central entropy decrease
is a required target condition, not a consequence derived from dynamics.

## Checks and corrections

### 1. Informational structure

The manuscript now gives the phrase "informational structure" a provisional
formal meaning in terms of a Hilbert space, global observable algebra, state,
and Hamiltonian or constraint. Claims that spacetime and matter emerge from
this structure remain programmatic.

### 2. Global state

The type-I ansatz explicitly assumes
$\rho=|\Psi\rangle\langle\Psi|$ to be pure and stationary. This does not follow
from unitarity alone. Consequently, the statement
$S_{\mathrm{vN}}(\rho)=0$ is correct under the stated assumption but is not a
general result about unitary cosmology.

### 3. Boundary notation

$\mathcal{R}$ is now typed as an unspecified relation between embedding spaces,
while $T_n=(\iota_n^{\infty},\iota_{n+1}^{0})$ is a candidate pair in that
relation. Neither symbol is presented as a unitary operator, quantum channel,
algebra homomorphism, or external-time evolution map.

The superscripts $\infty$ and $0$ are explicitly treated as mnemonic boundary
labels, not as values of external time or established mathematical limits. A
genuine limiting construction remains contingent on an intrinsic relational
parameter, topology, and convergence criterion.

### 4. Restricted states and entropy

For an embedding $\iota:\mathcal{A}\hookrightarrow\mathcal{M}$, the induced
state $\omega_{\iota}(a)=\omega(\iota(a))$ is well-defined. The manuscript now
makes effective entropy depend on both this state and its embedded observable
algebra.

A substantive ambiguity was corrected here: reducing the set of accessible
observables or applying a coarse-graining does not automatically lower entropy
and commonly raises observational uncertainty. The required low entropy must
come from a physically selected, differently embedded or refactored algebra for
which the induced state is low entropy. The inequality between the old and new
effective entropies is explicitly an unproved requirement.

### 5. Selection rule

The schematic selector acts on classes
$\mathfrak{E}_{\lambda}/\!\sim_{\mathrm{phys}}$, and its objective must be
invariant under the proposed physical equivalence relation. This avoids treating
two representatives of the same operational physics as distinct solutions.
Neither the equivalence relation nor the selector is presently defined, so the
formalism does not yet distinguish a physical transition from a global-unitary
relabeling.

### 6. Page-Wootters construction

The ideal conditional-state formula and the sign in
$\partial_t\rho_R=-i[H_R,\rho_R]$ are consistent with the stated constraint
$H_{\mathrm{tot}}=H_C\otimes I+I\otimes H_R$ and the clock convention
$|t\rangle=e^{-iH_Ct}|0\rangle$. A direct two-level calculation reproduced the
conditional equation, unit trace, and zero constraint residual.

The text now states the needed energy-support condition, the restriction to
$p(t)>0$, and the distinction between a single rank-one effect, a normalized
time POVM, and a measurement instrument. It also correctly separates relational
clock evolution from the thermodynamic arrow.

### 7. Two-qubit illustration

The four proposed primed basis vectors are orthonormal. In the old
factorization, the Bell state gives
$\rho_A=I/2$ and $S(\rho_A)=1$ bit. In the primed factorization, the same vector
is $|0_{A'}0_{B'}\rangle$, giving a pure reduced state and zero entropy. A direct
finite-dimensional calculation verified both entropy values and the unchanged
global pure state.

This is an illustration of established factorization dependence, not evidence
for an aeonic transition. The explicit global unitary relating the two
factorizations makes that limitation visible. The manuscript now denotes these
quantities by $S_{\mathrm{ent}}$ and explicitly distinguishes them from
thermodynamic, observational, and gravitational entropy. The illustration does
not establish the cosmological target inequality for $S_{\mathrm{eff}}$.

### 8. Field-theory boundary

The manuscript no longer presents $\mathcal{B}(\mathcal{H})$, tensor-product
factorization, or partial traces as a continuum-QFT construction. It now also
distinguishes the type-III local algebras typical of nongravitational QFT from
type-II algebras that can arise for gravitationally dressed observables. The
appropriate algebraic setting and entropy for the hypothesis remain open.

## Unresolved requirements

1. Define the admissible embeddings and the relation $\mathcal{R}$.
2. Define $\sim_{\mathrm{phys}}$ operationally.
3. Derive a non-circular selector for $T_n$ from physical data or dynamics.
4. Derive relational data $\lambda_n$ that can change the selected algebra while
   $\rho$ and $H$ remain fixed, without using an external clock or circularly
   assuming the desired aeon.
5. Choose and justify a full-theory effective-entropy functional.
6. Generalize the ansatz to QFT or quantum gravity.
7. Derive a low-entropy boundary and thermodynamic arrow.
8. Show that the boundary construction can be selected repeatedly, rather than
   only for one candidate pair.
9. Produce a quantitative prediction distinct from existing cosmologies.

Until these are supplied, the correct classification is a mathematically
literate conceptual hypothesis and research program, not a completed physical
model.
