# sgpeer

Singapore bank peer comparison: Maybank Singapore against DBS, OCBC, UOB, Standard Chartered Bank Singapore (SCBSL) and HSBC Singapore (HSBCSG).

**Live dashboard:** https://soongjc.github.io/sgpeer/ (passphrase required; ask the owner)

`index.html` is an encrypted shell (AES-256-GCM, PBKDF2-SHA256, 600k iterations). The page source reveals nothing; the browser decrypts it with the passphrase. All underlying figures come from public bank disclosures.

## Layout

| Path | What it is |
|---|---|
| `index.html` | Locked Exco dashboard served by GitHub Pages |
| `00_spec/PIPELINE_SPEC.md` | Pipeline design: coverage set, artefact layers, cycle stages |
| `00_spec/COWORK_SCHEDULED_TASK.md` | Prompt for the weekly refresh task |
| `01_dictionary/METRIC_DICTIONARY.md` | Canonical metric definitions and per-bank quirks |
| `02_sources/SOURCE_REGISTRY.md` | Investor-relations document URLs and cadence per bank |
| `03_facts/facts.csv` | Long-format fact store: bank x period x metric, with source, page and confidence |
| `04_cards/` | Insight cards (claim, evidence, implication, confidence) |
| `05_digest/` | Period digest |
| `lock_dashboard.py` | Encrypts an unlocked dashboard into the shell |

## Refreshing for a new period

1. Update `03_facts/facts.csv` and the dashboard per `00_spec/COWORK_SCHEDULED_TASK.md`.
2. Lock it (needs `pip install cryptography`):

   ```
   python3 lock_dashboard.py SGPEER_<period>_exco_dashboard.html index.html "<passphrase>"
   ```

3. Commit and push `index.html`. Pages redeploys in a minute or two.

Unlocked dashboards (`*_exco_dashboard.html`) are git-ignored and must never be committed here, since that would expose the content without the passphrase.
