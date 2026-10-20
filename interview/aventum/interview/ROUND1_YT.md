# Aventum Round 1: YouTube Prep Topics

Ordered by priority for an interview with the Head of AI on Fri 23 Oct. Section numbers point to `interview/aventum/STRATEGY.md`. Search phrases are what to type into YouTube; channels in brackets are reliable sources to prefer when they appear. Watch at 1.25 to 1.5x and write a 3-line summary of each topic in your own words.

Rough budget: P1 about 4 to 5 hours (Wed), P2 about 3 hours (Thu), P3 only if time is left.

## P1: Must watch (the gaps the JD names most firmly)

### Causal inference (§5.3)
1. **Correlation vs causation, confounding, potential outcomes (ATE / CATE)**. Search: `introduction to causal inference potential outcomes` (Brady Neal, "Introduction to Causal Inference" course).
2. **Causal graphs (DAGs), backdoor criterion, colliders and mediators**. Search: `backdoor criterion causal DAG explained`, `collider bias explained`.
3. **Propensity scores, inverse probability weighting, doubly robust estimation**. Search: `propensity score matching explained`, `inverse probability weighting causal`, `doubly robust estimator`.
4. **DoWhy walkthrough: model, identify, estimate, refute**. Search: `DoWhy tutorial`, `PyWhy DoWhy causal inference python`.
5. **Double Machine Learning / EconML and heterogeneous treatment effects**. Search: `double machine learning explained`, `EconML tutorial`, `heterogeneous treatment effects causal forest`.
6. **Uplift modelling and meta-learners (S, T, X learner), CausalML**. Search: `uplift modeling meta learners`, `CausalML uber tutorial`.
7. **Quasi-experiments: difference-in-differences, regression discontinuity, synthetic control**. Search: `difference in differences explained`, `regression discontinuity explained` (Ben Lambert, Nick Huntington-Klein "The Effect").

### Behavioural modelling and decision processes (§5.2)
8. **Imitation learning and behavioural cloning, compounding error, DAgger**. Search: `imitation learning behavioral cloning DAgger lecture` (Sergey Levine, CS285 Berkeley, imitation learning lecture).
9. **Markov Decision Processes: states, actions, rewards, policies**. Search: `markov decision process explained` (David Silver RL course lecture 2; StatQuest or similar for intuition).
10. **Offline reinforcement learning (learning from logged data)**. Search: `offline reinforcement learning explained` (Sergey Levine offline RL talk).
11. **Contextual bandits: exploration vs exploitation, Thompson sampling, LinUCB**. Search: `contextual bandits explained`, `thompson sampling explained`.
12. **Inverse reinforcement learning (intro level only)**. Search: `inverse reinforcement learning explained`.

### Validating models in production (§5.4)
13. **Shadow deployment, canary releases, A/B testing ML models**. Search: `shadow deployment machine learning`, `A/B testing machine learning models production`.
14. **Off-policy evaluation and offline replay (IPS, replay method)**. Search: `off-policy evaluation explained`, `counterfactual evaluation recommender systems`.
15. **A/B test statistics: power, sample size, guardrail metrics**. Search: `A/B testing sample size power explained` (StatQuest).

## P2: Should watch (sharpen what you partly know)

### Sequence and intent modelling (§5.1)
16. **Markov chains and Hidden Markov Models**. Search: `markov chains explained`, `hidden markov model explained` (StatQuest, Normalized Nerd).
17. **LSTM internals (gates, vanishing gradients)**. Search: `LSTM explained` (StatQuest "Long Short-Term Memory"; Colah's blog is the written classic).
18. **Attention and Transformers, Bahdanau vs self-attention**. Search: `attention mechanism explained`, `transformers explained` (3Blue1Brown "Attention in transformers"; StatQuest "Attention for neural networks").
19. **Sequential recommendation / next-event prediction (SASRec, session-based models)**. Search: `sequential recommendation transformer SASRec`, `session based recommendation`.
20. **Calibration of model probabilities**. Search: `probability calibration machine learning`.

### Digital Twins and the domain (§5.5, §6)
21. **What a Digital Twin is and how simulation is used to test decisions**. Search: `digital twin explained`, `agent based simulation customer behaviour`.
22. **AI in insurance underwriting: submission triage, underwriter decision support**. Search: `AI underwriting specialty insurance`, `submission triage insurance AI`, `Lloyd's market AI`.
23. **How the London / Lloyd's market works: MGAs, brokers, capacity providers**. Search: `how Lloyd's of London works`, `what is an MGA insurance`.
24. **Aventum / Rokstone / Consilium**. Search: `Aventum Group`, `Rokstone underwriting` (company talks or interviews with leadership, if any).

### PyTorch quick refresh (§5.6)
25. **PyTorch training loop and nn.LSTM basics**. Search: `pytorch training loop explained`, `pytorch LSTM tutorial` (official PyTorch channel, Patrick Loeber).

## P3: Nice to have (if time remains)

26. **ML monitoring: data drift, concept drift, delayed labels**. Search: `ML model monitoring data drift` (Evidently AI talks).
27. **Explainability for regulated decisions: SHAP**. Search: `SHAP values explained`.
28. **Fairness and bias in insurance ML, FCA Consumer Duty**. Search: `FCA consumer duty AI`, `fairness in insurance pricing machine learning`.
29. **Event-driven ML architectures and feature stores**. Search: `event driven architecture machine learning`, `feature store explained`.
30. **MLflow model registry and the model lifecycle**. Search: `MLflow model registry tutorial`.

## After watching
- Do the Thursday mini-build (§7) to make P1 topics concrete.
- For each P1 topic, be able to answer: what it is, when it fails, and how you'd use it at Aventum.
- Don't describe anything here as experience. "I've been studying X since applying" is the honest framing (§8).
