---
name: ai-detector
description: |
  AI text detection using heuristic analysis (11 signal rules) and optional
  Hugging Face ML model. Scores text 0-100 for human-likeness. Use after
  humanizing output to verify it passes as human-written. No API keys needed.
license: MIT
compatibility: opencode
allowed-tools:
  - Bash
  - Read
---

# AI Text Detector

Detects AI-generated text patterns by analyzing 11 heuristic signals. Can optionally use a Hugging Face RoBERTa model for ML-based detection.

## How to Use

### Heuristic-only (always works, instant):
```bash
python3 ~/.config/opencode/skills/ai-detector/detect.py "your text here"
```

### With ML model (more accurate, needs model download):
```bash
python3 ~/.config/opencode/skills/ai-detector/detect.py --hf "your text here"
```

### Pipe from stdin:
```bash
echo "your text" | python3 ~/.config/opencode/skills/ai-detector/detect.py
```

### From a file:
```bash
python3 ~/.config/opencode/skills/ai-detector/detect.py -f essay.txt
```

## Output

The top-level `overall_score`, `verdict`, and `weaknesses` are what the agent should read.

### Without `--hf` (heuristic only):

```json
{
  "heuristic": { ... },
  "overall_score": 78.3,
  "verdict": "Likely human-written",
  "weaknesses": ["Passive voice overuse"]
}
```

Top-level fields are copied from the heuristic result.

### With `--hf` (heuristic + ML blended):

```json
{
  "heuristic": { ... },
  "ml": { ... },
  "overall_score": 86.5,
  "heuristic_weight": 37.9,
  "ml_weight": 48.6,
  "verdict": "Likely human-written",
  "weaknesses": []
}
```

Top-level `overall_score` is a **weighted blend** (40% heuristic + 60% ML).
`heuristic_weight` and `ml_weight` show each component's contribution.
`weaknesses` combines heuristic flaws with an ML-disagreement note if applicable.

To read only the heuristic score (faster, consistent), reference `heuristic.overall_score` instead.

## Score Interpretation

| Score | Meaning |
|-------|---------|
| 75-100 | Likely human-written |
| 55-74 | Mixed / uncertain |
| 0-54 | Likely AI-generated |

## How It Works

The heuristic engine checks 11 signals:

1. **Burstiness** — How much sentence lengths vary (low = AI-like)
2. **Sentence variance** — How many distinct sentence lengths exist
3. **Transition density** — Formulaic transitions ("furthermore", "moreover")
4. **AI vocabulary** — Words like "delve", "leverage", "navigate"
5. **Repetitive starts** — Many sentences starting with the same word
6. **Signposting** — "This essay will", "let us explore"
7. **Em dashes** — Overuse of em dashes (strong AI tell)
8. **Passive voice** — Excessive passive constructions
9. **Paragraph evenness** — All paragraphs the same length
10. **Filler phrases** — "In order to", "due to the fact that"
11. **Hedging** — "It could be argued", "this may indicate"

The ML model (`fakespot-ai/roberta-base-ai-text-detection-v1`) performs a transformer-based classification. When `--hf` is used, the final score is a weighted blend (40% heuristic, 60% ML).
