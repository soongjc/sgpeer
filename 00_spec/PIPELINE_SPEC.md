# Singapore Peer Bank Analysis Pipeline

Version 0.1 (2026-08-27). Owner: Soong. Runtime: Claude (this chat) for generation, Copilot Agent Builder over SharePoint for retrieval.

## 1. Purpose

Produce periodic competitor analysis of Singapore-market banks for Maybank C-suite, and publish the outputs in a form a lower-capability retriever (Copilot Agent Builder) can answer from by lookup rather than inference.

Coverage set (six banks):

| Code | Entity analysed | Depth |
|---|---|---|
| DBS | DBS Group Holdings | Full: results pack, CFO deck, annual report |
| OCBC | Oversea-Chinese Banking Corp | Full |
| UOB | United Overseas Bank | Full |
| SCBSL | Standard Chartered Bank (Singapore) Ltd | Statements only (SGX interim FS, annual FS) plus Standard Chartered PLC group narrative on Singapore/ASEAN |
| HSBCSG | HSBC Bank (Singapore) Ltd | Statements only (MAS-required annual FS) plus HSBC Holdings country disclosures for Singapore |
| MBB | Maybank (reference bank) | Full, MYR |

The two foreign subsidiaries publish audited statements but no investor decks. They yield statement-derived metrics (income mix, CIR, loan and deposit growth, NPL, capital) but not management-reported NIM, ROE or segment commentary. Their cards carry a "statement-derived" flag and the group-level narrative is used for strategy context only.

## 2. Design principle

Intelligence at generation time, not retrieval time. Claude reads, reconciles and reasons once. Every published artefact must let a weak model answer by finding the right chunk, so each chunk is self-describing (bank, period, metric, definition, source) and small enough to be retrieved whole.

## 3. Artefact layers

Working format is markdown and CSV (kept in this bundle). Published format is Word and PDF, because Agent Builder accepts PDF, Word, Excel and PowerPoint, and markdown in SharePoint libraries has been reported as not retrievable.

| Layer | Working file | Published as | Purpose |
|---|---|---|---|
| L0 Dictionary | 01_dictionary/METRIC_DICTIONARY.md | PDF | Canonical metric definitions, per-bank line-item mapping, quirks |
| L1 Sources | 02_sources/SOURCE_REGISTRY.md | PDF | Where each document lives, cadence, what it provides |
| L2 Facts | 03_facts/facts.csv | Word (one table per bank) + Excel copy | Long format, one row per bank x period x metric, with value, unit, source, page, definition, confidence |
| L3 Derived | rows in facts.csv with derived=Y | same | Ratios computed by Claude, with formula and inputs in the row |
| L4 Cards | 04_cards/{BANK}_{PERIOD}_{TOPIC}.md | PDF, one per card | 200 to 400 words: Claim, Evidence, Implication for Maybank, Confidence |
| L5 Digest | 05_digest/DIGEST_{PERIOD}.md | PDF | Cross-bank metric table plus "what changed" list; answers most questions alone |
| L6 FAQ | 05_digest/FAQ_{PERIOD}.md | Word | Question, answer, source triples generated mechanically from L2/L3 |

## 4. Stages per cycle

1. Collect. Pull results pack, CFO/CEO presentation, press release and (annually) annual report for DBS, OCBC, UOB from IR sites; SGX interim FS for SCBSL; annual FS for HSBCSG; Maybank results from maybank.com. Record every document in SOURCE_REGISTRY with URL and retrieval date.
2. Extract. Populate facts.csv. Every row cites source document and page. Confidence = primary (bank document), secondary (analyst or press summary of bank document, must be replaced by primary before publish), derived (computed).
3. Validate. Arithmetic identities must hold before publish:
   - NII + non-II = total income
   - Total income minus opex = PPOP
   - CIR = opex / total income within 0.3pp of reported
   - Reported NPL, CET1, CIR fall within plausible bands (NPL 0.3 to 5.0, CET1 10 to 20, CIR 30 to 60)
   - YoY figures reconcile to prior-period rows where prior rows exist
   Any failure blocks the affected card and is listed in the digest under "Open items".
4. Derive. ROE DuPont decomposition, non-II ratio, fee-to-income, cost of funds proxy, loan and deposit growth, LDR (gross loans / customer deposits, uniform), SGD-MYR conversions for absolute figures using period-average rate recorded in the digest.
5. Narrate. Write cards (one topic per file) and the digest. Standard card topics: profitability, margin_and_funding, fee_and_wealth, cost_and_tech, asset_quality, capital_and_returns, geography_asean, guidance_vs_delivery, strategy_signals.
6. Publish. Convert markdown to PDF (cards, dictionary, digest, registry) and Word (facts tables, FAQ). Header block on page one of every file: bank, period, topic, as-of date, source list. Zip as SGPEER_{PERIOD}.zip for upload to the SharePoint folder for that period.

## 5. Publish rules for Agent Builder

- One SharePoint folder per period, e.g. /SGPeer/2026-1H/. Under 1,000 files and 50 subfolders per knowledge source.
- Filenames encode retrieval keys: {BANK}_{PERIOD}_{TOPIC}.pdf. Example: OCBC_1H26_fee_and_wealth.pdf.
- Cards as PDF (page-level citations only work on PDF). Keep each card above 4 KB so it gets chunk-level rather than document-level citation; pad with the evidence table if needed.
- Facts as Word tables, not only Excel, because the agent cannot run code and answers analytical questions from XLSX poorly.
- No charts as images without the underlying numbers in text on the same page.
- Repeat bank, period and metric definition inside every table row and every card section; assume no header survives chunking.

## 6. State handling between sessions

The container resets between chats. The bundle is the state. Each cycle starts by uploading the previous SGPEER_{PERIOD}.zip plus the new source documents (or letting Claude fetch public ones). Claude appends to facts.csv, never overwrites prior periods.

## 7. Standard output table (C-suite view)

Kept aligned with the existing Malaysian peer table so the two series can sit side by side. Rows, in fixed order:

1. Net profit growth (YoY)
2. PPOP growth (YoY)
3. Total income growth (YoY)
4. Opex growth (YoY)
5. ROE (reported, annualised)
6. CIR
7. NIM (cumulative, reported)
8. NIM (individual quarter)
9. Non-interest income ratio
10. Non-interest income growth (YoY)
11. NII growth (YoY)
12. Fee income growth (YoY)
13. Wealth income growth (YoY)
14. Gross NPL ratio
15. Allowance coverage of NPA (lowest reported variant, excl. collateral uplift)
16. Credit cost (bp, annualised)
17. CET1 (transitional and fully phased-in where both reported)
18. Total capital ratio
19. CASA ratio
20. Loans growth (YoY, constant currency where reported)
21. Deposits growth (YoY)
22. LDR (gross loans / customer deposits)
23. Dividend payout ratio
24. Wealth AUM (SGD b) and growth
25. Tech spend share of opex (where disclosed)
26. Income per employee (where headcount disclosed)
27. Guidance delivered vs stated (qualitative flag)

Maybank rank among the SG-comparable set is shown per row where the metric is comparable across currencies.

## 8. What "insight" means here

Each card must pass the test: would a Maybank CFO, CEO or business head change a decision, or at least a question they ask, because of this? Ratios alone fail the test; the narrative of why the ratio moved and what Maybank's equivalent lever is passes it.
