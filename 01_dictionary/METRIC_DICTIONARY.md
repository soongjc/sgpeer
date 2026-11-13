# Metric Dictionary: Singapore Peer Set

Version 0.1 (2026-08-27). Drafted from DBS 2Q26 CFO presentation, OCBC 1H26 press release, UOB 1H26 results presentation (via secondary summary, to be confirmed against the primary deck), and Standard Chartered / HSBC subsidiary filing structure.

Each metric: canonical name, definition used in this pipeline, then how each bank reports it and any adjustment needed. "Group" means the consolidated listed entity unless stated.

## A. Income statement

### total_income
Definition: NII plus non-interest income, as reported by the bank.
- DBS: "Total income", split into Commercial book (NII, net fee and commission, treasury customer sales and other income) and Markets trading. Use the Group total.
- OCBC: "Total income". Includes Great Eastern insurance income. Keep both reported and ex-insurance variants (see insurance_income).
- UOB: "Total income" (net interest income, net fee income, other non-interest income).
- SCBSL / HSBCSG: "Operating income" from the audited income statement. Compute as net interest income plus net fee and commission income plus net trading income plus other operating income.
- MBB: "Net operating income" (net fund-based plus net non-fund-based income). Islamic banking income is embedded in fund-based; keep as is for the SG comparison and note in the card.

### nii
Definition: Net interest income.
- DBS: Group NII = Commercial book NII plus Markets trading NII. Commercial book NII is the cleaner franchise measure; store both. 1H26 Group 7,075, Commercial book 6,958.
- OCBC: "Net interest income" as reported.
- UOB: "Net interest income" as reported.
- SCBSL / HSBCSG: "Net interest income" from statements.
- MBB: Net fund-based income (includes Islamic financing income). Not strictly NII; flag in comparisons.

### non_ii
Definition: Total income minus NII.
- DBS: net fee and commission income plus treasury customer sales and other income plus Markets trading non-interest income.
- OCBC: net fee income plus net trading income plus insurance income plus other income. Report also non_ii_ex_insurance.
- UOB: net fee income plus other non-interest income (trading and investment income plus other).
- MBB: Net non-fund-based income.

### fee_income
Definition: Net fee and commission income.
- DBS: reports gross fee income by product (wealth management, investment banking, loan-related, cards, transaction services) and net fee income. Store net for the ratio, gross-by-product for mix. 1H26 net 2,942; gross 3,407.
- OCBC: "Net fee income" with wealth management fees broken out. 1H26 1,410; WM fees 63% of fees.
- UOB: "Net fee income" with wealth, credit card, loan and trade-related, and other. 1H26 1,730 (flat YoY).
- SCBSL / HSBCSG: net fee and commission income from statements; product split usually in notes.

### wealth_income
Definition: Income (NII plus non-II) attributed to the wealth franchise, as each bank defines it. Not directly comparable across banks; record the bank's definition in the row.
- DBS: "Wealth segment income" = Treasures, Treasures Private Client and Private Bank. 1H26 3,299. Separately, "Wealth management fees" within gross fee income, 1H26 1,826.
- OCBC: "Group WM income" = private banking, premier private client, premier banking, insurance, asset management, stockbroking. 1H26 3,290 (41% of total income). Broader than DBS because it includes insurance.
- UOB: "Wealth income" within Group Retail; 1H26 up 16% YoY. Wealth fees 1H26 462.
- MBB: Group Wealth Management (Maybank Premier and Private Wealth) income, from the results deck.

### wealth_aum
Definition: Assets under management for the wealth franchise as defined by the bank.
- DBS: Wealth segment AUM, 516 SGD b at Jun 26. NNM 1H26 21.
- OCBC: Banking WM AUM, 350 SGD b at Jun 26 (excludes GEH insurance AUM).
- UOB: Retail AUM 204 SGD b (HNW segment). Invested AUM mix 42%. NNM 1H26 4.
- MBB: Group Wealth AUM (MYR), from the results deck.

### insurance_income
OCBC only. Income from Great Eastern Holdings. 1H26 791. Needed to build non_ii_ex_insurance and cir_ex_insurance so OCBC's banking franchise is comparable with DBS and UOB. HSBC Holdings also has insurance in IWPB at group level, but HSBCSG statements are banking only.

### opex
Definition: Total operating expenses before allowances.
- DBS: "Expenses"; staff and other split available. 1H26 4,649.
- OCBC: "Operating expenses". 1H26 3,080.
- UOB: "Total expenses". 1H26 3,152.
- MBB: Overheads.

### ppop
Definition: Total income minus opex. Bank label varies ("Profit before allowances", "Operating profit before allowances", "Pre-provisioning operating profit"). Always recompute and check against reported.

### allowances
Definition: Total allowances for credit and other losses charged to P&L. Store SP (specific / impaired) and GP (general / non-impaired) separately.
- DBS: SP and GP reported; GP write-backs are shown negative. 1H26 total 303 (SP 345, GP -42).
- OCBC: "Allowances for impaired assets" and "for non-impaired assets". 1H26 total 372 (147 impaired, 225 non-impaired).
- UOB: specific and general allowances; also builds RLAR (regulatory loss allowance reserve) below the P&L line.
- MBB: Net impairment losses on loans; note ECL overlay movements.

### net_profit
Definition: Net profit attributable to shareholders. DBS "Net profit" 1H26 6,009; OCBC 4,190; UOB 2,920 (secondary). MBB: Profit attributable to equity holders.

## B. Ratios as reported

### roe
Definition: Annualised return on ordinary shareholders' equity as reported. Record whether the bank also reports ROTE.
- DBS: ROE and ROTE both reported. 2Q26 ROE 17.9, ROTE 19.6. 1H26 ROE 17.5 (press statement).
- OCBC: Annualised ROE. 1H26 13.7.
- UOB: Annualised ROE in results pack (not captured yet).
- SCBSL / HSBCSG: not reported; derive as annualised net profit / average total equity and flag as derived.
- MBB: Reported ROE.

### nim
Definition: Net interest margin as reported for the period, annualised. Store cumulative (YTD) and single-quarter separately.
- DBS: Group NIM and Commercial book NIM both reported quarterly. Use Group for the peer row, Commercial book for the funding analysis. 2Q26 Group 1.87, Commercial book 2.21; 1H26 Group 1.88, Commercial book 2.25.
- OCBC: single NIM. 1H26 1.73, 2Q26 down 22bp YoY.
- UOB: single NIM plus a loan margin figure. 2Q26 1.74, 1H26 1.78; loan margin 1H26 2.11. Do not confuse loan margin with NIM.
- SCBSL / HSBCSG: derive as NII / average interest-earning assets if the notes allow; otherwise NII / average total assets, flagged.
- MBB: Reported Group NIM; MBB also reports NIM excluding certain items in some quarters. Use the headline.

### cir
Definition: Opex / total income. Recompute from components; report the bank's figure if within 0.3pp.
- DBS 1H26 39 (recompute 4,649/12,041 = 38.6). OCBC 1H26 38.5. UOB 1H26 44.9.
- OCBC: also compute ex-insurance.
- MBB: Reported CIR.

### non_ii_ratio
Definition: Non-II / total income. OCBC 1H26 close to 44%. DBS derive: (12,041 minus 7,075)/12,041 = 41.2. UOB derive.

### npl_ratio
Definition: Non-performing loans / gross customer loans, as reported.
- DBS 1.0 (Jun 26). OCBC 0.9. UOB 1.6.
- MBB: Gross impaired loans ratio (GIL). Equivalent for this purpose.

### npa_coverage
Definition: Total allowances (SP plus GP plus RLAR where applicable) / total NPA. Use the bank's headline coverage figure but record the basis.
- DBS: 130% of NPA, 196% after considering collateral. Use 130.
- OCBC: "Total NPA coverage" 163%.
- UOB: NPA coverage 88%, unsecured NPA coverage 306%. Total allowances include RLAR 379. Use 88 and note RLAR inclusion.
- MBB: Loan loss coverage, lowest reported variant excluding regulatory reserve and collateral uplift, consistent with the Malaysian series.

### credit_cost_bp
Definition: Annualised total allowances for loans / average loans, in bp.
- DBS: reports SP/loans only (1H26 15bp). Total credit cost must be derived: total allowances / average gross loans.
- OCBC: "Credit costs" annualised, 1H26 18bp (total, includes non-impaired).
- UOB: "Total credit costs" 1H26 27bp; specific 26bp in 2Q.
- MBB: Net credit charge-off rate, already annualised, shown negative in the Malaysian table.

### cet1
Definition: Common Equity Tier 1 ratio. Singapore banks are mid-transition to MAS final Basel III (phased 1 Jul 2024 to 1 Jan 2029), so store both transitional and fully phased-in.
- DBS Jun 26: transitional 16.6, fully phased-in 14.6.
- OCBC Jun 26: 15.7 / 14.0.
- UOB Jun 26: fully loaded 15.4 (transitional not captured yet).
- SCBSL / HSBCSG: Pillar 3 disclosures on their SG sites.
- MBB: Group CET1 (after proposed dividend). Malaysian banks are on BNM Basel III, not mid-transition; compare with SG fully phased-in figures.

### casa_ratio
Definition: CASA deposits / total customer deposits.
- DBS: Casa 347 of 638 = 54.4% (derive). OCBC: reports CASA ratio in results pack (not captured). UOB: Group CASA 243 of 437 customer deposits (derive); Retail CASA mix 58% is segment-level, do not use as Group.

### ldr
Definition: Gross customer loans / customer deposits, computed uniformly. Banks' own LDR figures use net loans in some cases.
- DBS 475/638 = 74.5 (derive). OCBC reports 78.4. UOB reports 81.7.

### payout_ratio
Definition: Dividends declared for the period / net profit for the period.
- DBS: quarterly ordinary 66c plus capital return 15c; record both. OCBC 50% interim (47c). UOB 50% (88c interim), plus 2 SGD b buyback programme 2025 to 2027.

## C. Balance sheet

- gross_loans: DBS 475 SGD b (Jun 26). OCBC customer loans 364. UOB 361.
- customer_deposits: DBS 638. OCBC 459. UOB 437 (derive from CASA 243 plus FD and others 194; confirm).
- total_assets, rwa, leverage_ratio: DBS RWA 382, leverage 5.8. UOB RWA 279, leverage 6.8.
- lcr, nsfr: UOB LCR 159, NSFR 114. Others from Pillar 3.

## D. Growth conventions

- YoY on half-year and quarter figures as reported. Constant-currency growth is used by all three SG banks for loans and deposits; store both reported and constant-currency where given, use constant-currency for the peer row.
- No YTD annualisation is needed for the SG banks (they report annualised ratios directly). This differs from the Malaysian series where YTD balance growth is annualised by 4/quarters elapsed.
- Fiscal year: all six banks are December year-end. No mapping needed.

## E. Currency

- SG banks report SGD. SCBSL and HSBCSG statements are SGD. MBB is MYR.
- Ratios and growth rates are compared directly.
- Absolute figures converted to MYR at the period-average SGD/MYR rate recorded in the digest for that period. State the rate on every converted row.

## F. Bank-specific quirks (one line each)

- DBS: Commercial book vs Markets trading split; Group NII includes Markets trading NII, which can be negative (1H25 minus 15). Capital return dividend of 15c per quarter is separate from ordinary dividend. Global minimum tax (15%) depressed Singapore net profit in 2025.
- OCBC: Great Eastern consolidated; insurance income and GEH investment income sit inside non-II and trading income. Strip for banking-only comparisons. Share of associates (Bank of Ningbo) is material, 637 in 1H26. S$2.5b capital return programme to complete by FY26.
- UOB: Citi consumer integration one-offs mostly done; 1H26 includes non-recurring gains (UOB Asset Management sale to AllianzGI, pre-tax gain about 330). Track core vs reported. Greater China NPL 4.8% concentrated in one real-estate account. RLAR sits in allowances. Guidance: FY26 NIM 1.75 to 1.80, credit cost 25 to 30bp, fee growth cut to low single digit.
- SCBSL: locally incorporated 2013, consolidates all SC Singapore business. Publishes interim FS on SGX (bond issuer) and annual FS. Segment re-presentation in Apr 2025 changed product lines; check comparability across 2024/2025.
- HSBCSG: locally incorporated subsidiary; annual FS published under MAS requirements. HSBC Holdings gives Singapore as a country line (loans, deposits, PBT) in its annual report; use that for trend, not for ratio comparison.
- MBB: Fund-based / non-fund-based split; Islamic banking inside fund-based; regional (Singapore, Indonesia) segment data in the results deck allows a direct Singapore-market comparison with the peer set.
