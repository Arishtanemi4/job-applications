# Aventum Round 1: Study Notebooks

One notebook per topic in `../STRATEGY.md` §5 (plus the two §7 mini-builds). Each follows the same Board-textbook pattern: **Theory → boxed Formula → Solved Example (by hand) → Program → Output → Explanation → Exercise (answers hidden) → Viva questions → Formula sheet → "How to say it on Friday"**.

Work each Solved Example on paper **before** running its cell, then check that the code agrees.

| # | Notebook | STRATEGY | Time | Day |
|---|---|---|---|---|
| 01 | `01_sequence_intent_modelling.ipynb`: Markov, HMM, LSTM gates, attention, intent metrics | §5.1 | 75 min | Wed |
| 03 | `03_behavioural_cloning_decisions.ipynb`: BC, DAgger, selective labels, MDP, bandits | §5.2 | 90 min | Wed |
| 04 | `04_causal_inference_foundations.ipynb`: potential outcomes, IPW/AIPW, DAGs, CATE, DiD | §5.3 | 2 h | Wed |
| 02 | `02_markov_vs_lstm_practical.ipynb`: practical: Markov vs PyTorch LSTM | §7.2 | 90 min | Thu am |
| 05 | `05_dowhy_econml_lalonde.ipynb`: practical: DoWhy + EconML on Lalonde | §7.1 | 2 h | Thu am |
| 06 | `06_validating_deployed_models.ipynb`: OPE, shadow (kappa), A/B power, canary | §5.4 | 75 min | Thu pm |
| 07 | `07_digital_twin_simulation.ipynb`: a toy MGA twin, replay validation, the causal trap | §5.5 | 75 min | Thu pm |
| 08 | `08_production_mlops.ipynb`: PSI/KS drift, delayed labels, calibration, reason codes, registry | §5.6 | 75 min | Thu pm |

If time is short, prioritise **04 → 05 → 06 → 03**: causal inference and validation are the gaps the JD names most firmly.

## Environment

Everything runs in the dedicated conda env **`aventum`** (never base). The notebooks have no `pip install` cells.

```bash
conda env create -f environment.yaml      # first time
conda env update -n aventum -f environment.yaml --prune   # after editing requirements.txt
python -m ipykernel install --user --name aventum --display-name "Python (aventum)" --env PYTHONNOUSERSITE 1
```

- `requirements.txt` is the single list of packages (pinned). `environment.yaml` pulls it in, so add new packages to `requirements.txt` only.
- `PYTHONNOUSERSITE=1` is set on the env and on the kernel, because packages in `%APPDATA%\Python\Python312` would otherwise leak into every Python 3.12 env.
- In VS Code / Jupyter pick the kernel **Python (aventum)**. All notebooks are saved with their outputs, so you can read them without running anything. Every notebook runs end to end on CPU in under a minute.

Re-run everything from the command line:
```bash
conda activate aventum
for f in 0*.ipynb; do jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name=aventum "$f"; done
```

## Honesty guardrail
These are **study notebooks on synthetic or public data**, worked through after applying. In the interview: "I've been working through X since applying". Never present it as production experience, and don't add it to the CV or `EXPERIENCE.md` (STRATEGY §7, §8).
