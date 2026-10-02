# Informational Cyclic Cosmology v0.1.5

Release date: 1 October 2026

## Purpose

This release consolidates completed bounded finite studies and closes that
example sequence. It clarifies what has been calculated and what remains
assumed. It does not introduce a cosmological selection law or claim an
observational prediction. The results-and-limits table, abstract, conclusions
and [reproducibility supplement](./research/v015/README.md) keep the studies
separate rather than presenting them as one working mechanism.

## Added Results

1. **Finite-time selector.** For the declared two-qubit Hamiltonian and
   fixed horizon, an exact-arithmetic certificate supports an entangled
   quotient-strict local minimum. A product-eigenbasis competitor has lower
   cost by more than 0.3 and better recovery in the stipulated task. This
   branch is not a global minimizer or a physically selected algebra. The
   example does not contradict the interaction-cost-specific obstruction.
2. **Measurement-relative entropy.** The original fixed Bell-state example
   is supplemented by a uniformly randomized Pauli POVM. With the same global
   trace convention its observational entropies are 2 and 5/3 bits. Explicit
   white-noise and sharpness formulas, zero-information controls and outcome
   merging distinguish this from reduced-state or cosmological entropy.
3. **Access and instruments.** Local measurements on both original qubits
   plus classical communication implement the new outcome statistics for
   arbitrary inputs. First-qubit-only access is insufficient at nonzero
   sharpness. Identical outcome statistics do not implement the ideal
   coherence-preserving parity instrument or arbitrary operations on the
   new subsystem. Intermediate records and their omission are explicit.
4. **Reproduction.** The supplement contains analytic derivations, unchanged
   checked calculation scripts, recorded results and a one-command runner.
   These checks are internal and LLM-assisted, not independent expert peer
   review, formal proof-assistant certification or experimental validation.

## Unchanged Limits

The earlier interaction-cost argument and EC/CAR lattice calculations are
unchanged. The three-cell boundary-independent robustness and four-cell
EC-specificity gates still fail. This release does not repeat that campaign.

Physical algebra selection, a cosmologically justified S_eff, intrinsic
relational inputs, transition dynamics, thermodynamic orientation, continuum
extension, cyclic repeatability and distinct empirical predictions remain
open. The finite measurement-entropy contrast is not a physical entropy reset.
No new model or larger finite simulation is added to address those gaps.

## Sources and Provenance

The manuscript adds direct references to Andreadakis, Dallas and Zanardi on
long-time scrambling; Styliaris, Anand and Zanardi on bipartition scrambling
and subsystem channels; Barnum and Knill on transpose recovery; and Chitambar
et al. on LOCC and quantum instruments. The Barnum-Knill reference identifies
the 2026 revised arXiv version of the 2002 article. The observational-entropy
definition retains its existing Buscemi-Schindler-Safranek attribution.
These sources support the stated frameworks, not the proposed ICC cosmology.

The author's originating idea and extensive AI assistance remain disclosed.
The author, ORCID and CC BY 4.0 license are unchanged. The manuscript uses the
[all-versions DOI](https://doi.org/10.5281/zenodo.21115416), without inventing
an unassigned v0.1.5 DOI. The PDF and source release are prepared locally;
this operation does not publish them to GitHub or Zenodo.

See [integration verification](./feedback/v0.1.5-integration-verification.md)
for the checks performed on this release and their limits. Historical v0.1.4
PDF and archive artifacts are preserved unchanged.
