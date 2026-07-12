# Manual layer: per-family quality assessment

How well each device's user-manual PDF suits **lexical retrieval** (the
implemented mechanism — TOC-split chapters + keyword cross-links, grepped on
demand; see `docs/architecture.md`'s *"How the manual layer contributes (and
is it RAG?)"*), what had to be fixed to get there, and a look ahead to true
RAG chunking. Companion to `docs/performance.md` (which covers ingestion
*timing*) — this covers ingestion *quality*.

## Comparative verdict

| | etx1p | secflow | etx2 | mp4100 |
|---|---|---|---|---|
| Source structure | Flat, per-topic chapters (22 TOC entries) | Same shape as etx1p (23 entries) | 5 giant "Parts," real topics nested 3-6 levels deep | Hybrid: topic chapters + one 259-page "Cards and Ports" holding 26 port types + module annexes (1,202 pages total) |
| Out of the box | **Good immediately** — no fixes needed | **Good immediately** — no fixes needed | **Bad initially** — 1 cross-link hit, one 1,079-page unusable "chapter" | **Good immediately** — the etx2-built adaptive splitter fired automatically, zero code changes |
| Final chapters | 14 | 17 | 44 | 38 |
| Avg file size | 65.4 KB | 59.2 KB | 51.9 KB | 42.6 KB |
| Cross-link rows | 21 | 21 | 17 (3 topics genuinely absent — see below) | 12 (matcher vocabulary gap for MP-specific areas — see below) |
| Extraction (mojibake) | Clean | Clean | Clean | Clean |

**etx1p and secflow were naturally excellent for lexical retrieval from the
first ingest.** Their source PDFs already segment by topic at exactly the
level the ingester needed (level-1 TOC = real chapters, level-2 = real
sections), so the original naive logic (split on level-1, cross-link on
level-2) worked perfectly on the first try. No fixes, no reprocessing, and
their largest chapter (182-184 pages) never approached any size threshold.

## What etx2 specifically required (the asymmetric work)

**1. An adaptive recursive splitter.** etx2's manual is organized as a
*book* (Parts → Chapters → Sections → Subsections, 6 TOC levels deep), not a
topic-per-chapter manual. Its "Feature Reference" part alone is 1,079 pages —
68% of the whole 1,576-page document — as a single undifferentiated blob.
Fix: a generic threshold rule in `scripts/ingest_manual.py` — any chapter
unit over 220 pages with ≥3 sub-sections recurses into the next TOC level,
repeating until units are chapter-sized. Even after the first split, some
sub-parts ("Traffic Processing," 287pp; "Monitoring and Diagnostics," 301pp)
were still oversized and needed a second recursion pass down to true
protocol-level files (Router, BGP, OSPF, Syslog, TWAMP each on their own).
etx1p/secflow never trigger this rule — verified byte-identical output
before and after the fix.

**2. Deeper cross-link matching.** The original cross-link matcher only
scanned level-2 titles for topic keywords. etx2's real topic names (MQTT,
PKI, RSA key generation) sit at level-3, nested under coarse level-2 headings
like "3 Management and Security" — so the matcher initially found almost
nothing (1 row of 17 possible topics). Fix: extended the matcher to search
every TOC level below wherever a chapter's body-section split point landed,
not just exactly one level down. General-purpose (helps any future
deeply-nested manual); etx1p/secflow's already-shallow structure meant they
never needed it.

**3. Two full re-verification passes.** After each fix, all three families
had to be re-ingested to prove etx1p/secflow came out byte-identical (zero
regression) while etx2 actually improved. This verification overhead only
existed because etx2 needed the fixes in the first place.

**What did *not* need fixing for etx2:** extraction quality itself (PyMuPDF
handled all three PDFs equally cleanly — zero mojibake anywhere, verified by
grep), and final per-file size discipline — once split, etx2's 51.9 KB
average lands in the same range as the other two families; it is not more
fragmented, just correctly granular for a bigger, differently-organized
source document.

## A gap that looks real but isn't

etx2's cross-link table has no rows for MQTT, LoRa, OPC-UA, or Modbus (secflow
and etx1p have all four). This is **not a manual defect** — ETX-2I is a pure
carrier-Ethernet demarcation device with no IoT-gateway capability, unlike
SecFlow, which explicitly targets industrial IoT (`sd-iot`, LoRaWAN,
cellular). The manual correctly has nothing to link there; forcing a match
would be the actual bug.

## mp4100 — the first "next manual" (2026-07-12), checklist applied

The Megaplex-4 manual (Mn 4.91, 1,202 pages) was the first ingest after the
checklist below was written, and it validated the etx2 engineering: the
adaptive recursive splitter **triggered on its own** for the 259-page "Cards
and Ports" chapter, splitting it into 20 per-port-type files (T3, SDH/SONET,
teleprotection, voice, VCG, …) with no code changes and no reprocessing.
Checklist results: 38 chapters / 42.6 KB avg (inside the known range), zero
mojibake, all page ranges contiguous.

Two findings worth banking:

1. **Cross-link vocabulary is ETX-shaped.** Only 12 rows matched because the
   matcher's CLI-topic list was written for the ETX/SecFlow feature set. The
   MP-4100's *own* headline areas — `cross-connect`, `pwe`, `slot`/`chassis`,
   teleprotection — have rich manual chapters but no vocabulary entries, and
   `configure crypto` exists in the device tree yet matched nothing. Unlike
   the etx2/MQTT case this is NOT a legitimate absence — it's the first real
   improvement item for the matcher: per-family topic vocabularies (or
   deriving candidate topics from the family's harvested command tree).
2. **A French quick-start chapter** (`02-guide-d-installation-rapide…`) rode
   along from the bilingual PDF — harmless grep noise, but a reminder that
   chapter lists aren't always monolingual.

## Lexical vs. true RAG

Everything above is about **lexical retrieval quality** — grep-by-topic
against TOC-split chapters, the implemented mechanism (`docs/architecture.md`
is explicit that this is deliberately *not* vector-embedding RAG yet).

One RAG-relevant observation worth banking for later: if this ever moves to
real embeddings, etx1p/secflow's current chapter files (up to ~180 KB for
the largest) are *larger* than ideal embedding-chunk size — they'd need
further sub-chunking regardless of family. etx2's post-fix files, ironically,
already sit closer to good RAG-chunk granularity (individual protocol-level
files, ~52 KB average) *because* its messier source structure forced finer
splitting. The fix aimed at lexical grep happened to produce better-shaped
chunks for a future RAG pass too, on the exact family that needed the most
engineering to get there.

## Checklist for evaluating the next manual added

1. Ingest with `/rad-load-manual` (or `scripts/ingest_manual.py` directly).
2. Check chapter count and avg file size — compare against this table's
   range (14-44 chapters, ~52-65 KB avg). Wildly outside that range is a
   signal, not a failure: re-check the source TOC's depth/shape.
3. Grep for mojibake markers (`ג|â€¢|Â|�`) — expect zero hits.
4. Read the cross-link table in `manual-index.md` — are the topics you'd
   expect for that device's actual feature set present? Absence is only a
   bug if the device *has* that feature (see the etx2/MQTT case above).
5. If cross-links are sparse despite the device having the feature, check
   the source PDF's TOC depth (`fitz.open(pdf).get_toc()`, inspect `lvl`
   values) — a manual organized as a "book" (few, huge level-1 entries) is
   the known trigger for needing the adaptive splitter, which should already
   handle it; if not, the threshold constants
   (`EXPAND_MIN_PAGES`/`EXPAND_MIN_CHILDREN`) may need revisiting.
