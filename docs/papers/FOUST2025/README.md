# FOUST 2025

Paper introducing SULO, published in the CEUR-WS proceedings of FOUST 2025.

| File | What it is |
| --- | --- |
| `SULO_FOUST2025.pdf` | The **corrected** version. Differs from the version of record; see below. |
| `SULO_FOUST2025-as-published.pdf` | The **version of record**, exactly as published in the proceedings. |
| `SULO_FOUST2025.zip` | Submission bundle as published. |
| `2025-09-09-SULO@FOUST2025.pdf` | Presentation slides. |

The LaTeX source is at
[MaastrichtU-IDS/sulo-foust2026-manuscript](https://github.com/MaastrichtU-IDS/sulo-foust2026-manuscript),
whose README lists every correction in full.

## Why there are two PDFs

Neither Turtle listing in the published paper parsed. Each was extracted
verbatim and checked with an RDF parser: Figure 4 failed on an `@prefix`
declaration missing its terminating period and on an undeclared `xsd:` prefix,
and Figure 7 failed on a missing period, an undeclared `taxon:` prefix, and a
period in place of a semicolon that left a statement without a subject. The
class expression in Figure 5 misspelled `isFeatureOf`, the namespace was given
as `http://w3id.org/sulo/` rather than `https://`, and the stated inference in
Figure 7 was over `:visit_1`, a subject the example data never defines.

The corrected Figure 7 was then checked against `sulo.ttl` with a reasoner
rather than only a parser: it entails
`:encounter sulo:hasParticipant :alice, :drsmith`, which is exactly the
inference the figure claims.

The corrected version also names the object property `hasItem` throughout, as
SULO defines it (`sulo:hasItem`, inverse `sulo:isItemIn`); the published version
called it `hasMember` in two places.

No claim, result, or axiom of SULO is changed by any of this. The corrected
version keeps the published pagination, so page-level citations remain valid.

Both figures are now live regression tests in
[MaastrichtU-IDS/sulo-testharness](https://github.com/MaastrichtU-IDS/sulo-testharness),
so the inferences they claim are checked against every change to the ontology.
