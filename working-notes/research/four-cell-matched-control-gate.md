# Four-Cell Matched Non-Axial Control Gate

Protocol fixed locally: 9 August 2026, before evaluating the four-cell density
control.

Status: completed prospective internal control; not externally preregistered or
independently peer reviewed. The protocol above was fixed before evaluating the
density control. Results below were appended after implementation and separate
internal mathematical and physics reviews.

Reproducible calculation:
[`ec_four_cell_matched_control.py`](./ec_four_cell_matched_control.py)

## 1. Question

Does the finite four-cell branch behavior distinguish the
Einstein-Cartan-motivated axial-current contact from a matched non-axial onsite
interaction, or is it generic competition between hopping locality and onsite
locality?

## 2. Interactions

The candidate EC interaction is the existing normal-ordered onsite axial-current
contact $Q_{\mathrm{ax}}$.

The sole prospective control is

$$
Q_{\mathrm{dens}}=\sum_x N_x(N_x-1).
$$

This control is number preserving, onsite, quartic, translation invariant, and
spinor blind. It is not the axial-current contraction used to represent the
minimal EC-induced channel in this finite model. "Non-axial" does not mean that
no generalized torsion effective theory could contain a density-like channel.
No additional control will be selected after the result is known.

Overall rescaling of either contact is immaterial because its coupling is fixed
by the same equal-endpoint rule.

## 3. Matched ingredients

Both interactions use exactly the same:

- four cells with four Dirac modes per cell;
- half-filled $N=8$ sector;
- naive nearest-neighbor twisted kinetic operator;
- centered fixed-sector Hilbert-Schmidt selector;
- candidate quotient $U(4)/(U(1)^4\rtimes S_4)$ and its 12 horizontal tangent
  directions;
- phase grid $\phi_j=j\pi/16$, $j=0,\ldots,16$;
- zero-eigenspace resolution rule at $\phi=0$;
- equal-endpoint coupling rule;
- gauge transport $U_\phi=G(\phi)U_0$ with
  $G_{xx}(\phi)=e^{ix\phi/4}$;
- stationarity tolerance $10^{-7}$ at every derivative step;
- minimum-curvature threshold $2\times10^{-5}$ at every Hessian step; and
- decomposition distinctness threshold $10^{-6}$.

No alternative optimizer basin may replace the transported branch in the
primary gate. Alternative stationary points, if found, are descriptive only.

## 4. Validation gate

Before interpretation, the density low-body operator must:

1. reproduce the direct fixed-sector density operator at small filling;
2. reproduce $\sum_x n_x(n_x-1)$ on every $L=4,N=8$ occupation mask;
3. be Hermitian and purely two body under the declared convention; and
4. pass the same sparse trace, norm, and local-projection checks used for the
   axial calculation.

A validation failure makes the comparison inconclusive. It cannot count as an
EC-specificity pass.

## 5. Primary gates

For each interaction, the **periodic endpoint gate** passes only if the resolved
site and transported periodic representatives are distinct, stationary, and
strict at $\phi=0$.

The **small-twist gate** passes only if those same branch definitions pass at

$$
\phi=0,\qquad \pi/16,\qquad \pi/8.
$$

The **full phase-grid gate** passes only if they pass all 17 prescribed points.
The full grid is descriptive once either model fails; it cannot change the
specificity rule below.

## 6. Prospective EC-specificity rule

The primary **EC-specificity gate passes** only if:

1. the axial interaction passes the small-twist gate; and
2. the density control fails either the periodic endpoint gate or the
   small-twist gate because its transported representative is nonstationary,
   non-strict, or identical to the site branch.

If both interactions pass the small-twist gate, EC specificity **fails**. A
different coupling, Hessian magnitude, or later critical phase is quantitative
information only and cannot rescue the primary claim.

If implementation validation or stationary-point resolution fails, the result
is **inconclusive**, not an EC pass.

## 7. Conditional diagnostics

If an interaction passes the small-twist gate, the calculation may, for each of
$\pi/16$ and $\pi/8$:

1. form the exact fixed-representative residual polynomial
   $A+2gC+g^2B$;
2. locate a positive equal-cost root in $[0.70g_0,1.05g_0]$;
3. re-audit both representatives at that root; and
4. run the same 24 seeded Haar samples and four descents.

These diagnostics compare mechanisms but are not part of the primary
specificity gate. Finite random searches do not prove global minimality.

## 8. Claim boundary

This gate can test interaction specificity only inside the declared finite
selector. It cannot establish EC dynamics, a continuum limit, a physical
factorization law, or cosmology.

## 9. Results

The completed calculation gives the following primary result:

| Quantity | Axial contact | Density control |
|---|---:|---:|
| Equal-endpoint coupling $g_0$ | 0.4298279139 | 1.2984286349 |
| Periodic endpoint gate | pass | pass |
| Three-point small-twist gate | pass | pass |
| Branch Hessian minimum at $\phi=\pi/8$ | 0.111885 | 0.181435 |
| Maximum primary branch-gradient norm | $5.92\times10^{-12}$ | $6.45\times10^{-11}$ |
| Site/branch decomposition overlap | 0.375000 | 0.375000 |

Both Hessian margins are far above the declared $2\times10^{-5}$ threshold,
and both gradient maxima are far below $10^{-7}$. The primary outcome is
therefore

> **EC-specificity fail:** the matched non-axial density control passes the same
> periodic and small-twist gates as the axial contact.

This verdict follows the rule in Section 6. No later result changes it.

### 9.1 Operator and independence validation

All density reconstruction, $N=8$ occupation-mask action, off-diagonal action,
projection-overlap, trace, norm, one-body-zero, and Hermiticity discrepancies
are zero at displayed double precision.

After removing each interaction's fixed-sector identity component, the centered
operator cosine is 0.2119995760. The density contact retains a relative residual
of 0.9772697579 after its best centered axial rescaling. The one-cell
two-particle spectra are

$$
(-4,-4,-4,4,8,8)\quad\text{and}\quad(2,2,2,2,2,2),
$$

respectively. The adverse result is not an identity shift or rescaling artifact.

### 9.2 Full-grid diagnostics

Both transported representatives remain stationary and distinct across the
complete grid, but each eventually loses positive curvature:

| Quantity | Axial contact | Density control |
|---|---:|---:|
| Full 17-point gate | fail | fail |
| First failed grid index | 8 | 9 |
| First failed phase | $\pi/2$ | $9\pi/16$ |
| Branch Hessian there | -0.010441 | -0.064837 |

The density branch remains strict at $\pi/2$, with minimum Hessian 0.004766,
and fails one point later. This quantitative difference cannot rescue axial
specificity under the prospective rule.

### 9.3 Post-result analytic audit

For both interactions, the site and transported residual components obey

$$
R_{\mathrm{site}}=(A,0,0),
\qquad
R_{\mathrm{branch}}=
\left(A\sin^2\frac{\phi}{4},B,0\right),
\qquad
g_0^2B=A.
$$

The maximum component-and-cost identity discrepancies across all 17 points are
$4.66\times10^{-10}$ for the axial contact and
$6.98\times10^{-10}$ for density. Consequently, the retuned equal-cost root is

$$
g_*(\phi)=g_0\cos\frac{\phi}{4}.
$$

At $\pi/16$ and $\pi/8$, both models reproduce this root to at worst
$5.33\times10^{-15}$, both audited representatives are distinct and strict,
and the seeded 24-sample/four-descent searches find no lower value. The random
searches do not prove global minimality.

The common residual law was identified after the primary outcome and is not a
retrospective gate. It explains why the branch-cost phenomenon is shared by
these two independent onsite contacts.

### 9.4 Subsequent full onsite closure

A later bounded calculation classifies the complete 36-real-dimensional space
of Hermitian, translation-invariant, number-preserving onsite quartic contacts
in this same $L=4$, $N=8$ selector. Every nonzero contact makes the declared
periodic resolver select the balanced kinetic zero modes and satisfies the same
transported residual law. Thus the axial and density rows above are two special
cases of a finite-class identity, not isolated coincidences.

This strengthens the negative specificity interpretation but does not change
the prospective primary verdict. See the
[closure report](./four-cell-onsite-closure.md),
[closure script](./ec_four_cell_onsite_closure.py), and separate
[mathematical review](../feedback/four-cell-onsite-closure-mathematical-review.md).

## 10. Reviews and interpretation

The separate reviews are:

- [deep mathematical review](../feedback/four-cell-matched-control-mathematical-review.md);
- [physics review](../feedback/four-cell-matched-control-physics-review.md).

The mathematical review finds the finite comparison coherent and the negative
specificity verdict numerically well separated from all thresholds. The physics
review concludes that the result should stop this branch geometry from being
used as EC-specific support. It does not test or refute the main ICC proposal.

## 11. Reproduction

Run the primary three-point gate before the descriptive full calculation:

```bash
python3 research/ec_four_cell_matched_control.py --max-index 2
```

Then run the complete grid and conditional diagnostics:

```bash
python3 research/ec_four_cell_matched_control.py --max-index 16 --conditional
```

On the reviewed Apple-silicon laptop, the complete command took approximately
385 seconds. Runtime is implementation and hardware dependent.
