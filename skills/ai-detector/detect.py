#!/usr/bin/env python3
"""
AI Text Detector — Hybrid Heuristic + HuggingFace Model
Usage:
  python3 detect.py "text to check"
  python3 detect.py --hf "text with ML model"
  cat file.txt | python3 detect.py
  python3 detect.py --hf -f file.txt
"""

import sys
import json
import re
import math

HEURISTIC_WEIGHTS = {
    'burstiness': 0.20,
    'sentence_variance': 0.15,
    'transition_density': 0.12,
    'ai_vocab_density': 0.12,
    'repetitive_starts': 0.08,
    'signposting_density': 0.08,
    'em_dash_density': 0.06,
    'passive_voice_ratio': 0.03,
    'paragraph_evenness': 0.06,
    'filler_density': 0.04,
    'hedging_density': 0.03,
}

TRANSITIONS = [
    'furthermore', 'moreover', 'in addition', 'additionally',
    'it is worth noting', 'it is important to', 'it should be noted',
    'consequently', 'nevertheless', 'nonetheless', 'in conclusion',
    'to summarize', 'in summary', 'firstly', 'secondly', 'thirdly',
    'lastly', 'for instance', 'for example', 'namely',
    'specifically', 'in particular', 'on the other hand',
    'in contrast', 'conversely', 'as a result', 'accordingly',
    'subsequently', 'thereafter', 'thus', 'hence', 'therefore',
]

AI_VOCAB = [
    'delve', 'leverage', 'navigate', 'utilize', 'showcase',
    'transformative', 'seamless', 'robust', 'holistic', 'empower',
    'unlock', 'dynamic', 'cutting-edge', 'bespoke', 'actionable',
    'streamline', 'paradigm', 'ecosystem', 'journey', 'landscape',
    'testament', 'ever-evolving', 'foster', 'garner', 'pivotal',
    'intricate', 'intricacies', 'tapestry', 'underscore', 'vibrant',
    'groundbreaking', 'enrich', 'elevate', 'revolutionize',
    'game-changer', 'state-of-the-art', 'world-class', 'best-in-class',
]

SIGNPOSTING = [
    'let\'s dive', 'let\'s explore', 'let\'s break down',
    'here\'s what you need', 'now let\'s look at', 'without further ado',
    'in this essay', 'in this paper', 'in this article',
    'this essay will', 'this paper will', 'this article will',
    'the purpose of this', 'the goal of this',
    'over the course of', 'throughout this',
]

FILLERS = [
    'in order to', 'due to the fact that', 'at this point in time',
    'a number of', 'in the event that', 'has the ability to',
    'it is important to note', 'it is crucial to',
    'it goes without saying', 'needless to say',
]

HEDGES = [
    'it could be argued', 'it could potentially', 'it might be',
    'this may indicate', 'this could suggest', 'this might imply',
    'some researchers believe', 'it is widely thought',
    'many would argue', 'it is commonly believed',
    'it is often said',
]

PASSIVE_INDICATORS = [
    r'\bwas\s+\w+ed\b', r'\bwere\s+\w+ed\b',
    r'\bhas been\s+\w+ed\b', r'\bhave been\s+\w+ed\b',
    r'\bhad been\s+\w+ed\b', r'\bis\s+\w+ed\b',
    r'\bare\s+\w+ed\b', r'\bbeen\s+\w+ed\b',
]


def get_sentences(text):
    raw = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in raw if len(s.strip().split()) >= 3]


def get_paragraphs(text):
    raw = re.split(r'\n\s*\n', text.strip())
    return [p.strip() for p in raw if len(p.strip().split()) >= 5]


def burstiness_score(text):
    sentences = get_sentences(text)
    if len(sentences) < 3:
        return 0.5
    lengths = [len(s.split()) for s in sentences]
    mean = sum(lengths) / len(lengths)
    if mean == 0:
        return 0.5
    variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    cv = math.sqrt(variance) / mean
    score = min(cv * 2.5, 1.0)
    return score


def sentence_variance_score(text):
    sentences = get_sentences(text)
    if len(sentences) < 3:
        return 0.5
    lengths = [len(s.split()) for s in sentences]
    unique_lens = len(set(lengths))
    ratio = unique_lens / len(lengths)
    return min(ratio * 3, 1.0)


def transition_density_score(text):
    text_lower = text.lower()
    words = len(text.split())
    if words < 20:
        return 0.5
    count = 0
    for t in TRANSITIONS:
        count += len(re.findall(r'\b' + re.escape(t) + r'\b', text_lower))
    per_1000 = (count / words) * 1000
    score = 1.0 - min(per_1000 / 12, 1.0)
    return score


def ai_vocab_score(text):
    text_lower = text.lower()
    words = len(text.split())
    if words < 20:
        return 0.5
    count = 0
    for v in AI_VOCAB:
        count += len(re.findall(r'\b' + re.escape(v) + r'\b', text_lower))
    per_1000 = (count / words) * 1000
    score = 1.0 - min(per_1000 / 8, 1.0)
    return score


def repetitive_starts_score(text):
    sentences = get_sentences(text)
    if len(sentences) < 4:
        return 0.5
    starts = []
    for s in sentences:
        words = s.split()
        if words:
            starts.append(words[0].lower().strip('"\''))
    unique = len(set(starts))
    ratio = unique / len(starts)
    return min(ratio * 2.5, 1.0)


def signposting_score(text):
    text_lower = text.lower()
    words = len(text.split())
    if words < 20:
        return 0.5
    count = 0
    for s in SIGNPOSTING:
        count += text_lower.count(s)
    per_1000 = (count / words) * 1000
    score = 1.0 - min(per_1000 / 5, 1.0)
    return score


def em_dash_score(text):
    count = text.count('\u2014') + text.count('\u2013') + text.count(' -- ')
    paragraphs = get_paragraphs(text)
    if not paragraphs:
        return 1.0 if count == 0 else 0.0
    per_para = count / len(paragraphs)
    score = 1.0 - min(per_para / 2, 1.0)
    return score


def passive_voice_score(text):
    words = len(text.split())
    if words < 20:
        return 0.5
    text_lower = text.lower()
    count = 0
    for p in PASSIVE_INDICATORS:
        count += len(re.findall(p, text_lower))
    per_1000 = (count / words) * 1000
    score = 1.0 - min(per_1000 / 18, 1.0)
    return score


def paragraph_evenness_score(text):
    paragraphs = get_paragraphs(text)
    if len(paragraphs) < 2:
        return 0.5
    lengths = [len(p.split()) for p in paragraphs]
    mean = sum(lengths) / len(lengths)
    if mean == 0:
        return 0.5
    variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    cv = math.sqrt(variance) / mean
    high_cv = min(cv * 1.5, 1.0)
    return high_cv


def filler_score(text):
    text_lower = text.lower()
    words = len(text.split())
    if words < 20:
        return 0.5
    count = 0
    for f in FILLERS:
        count += text_lower.count(f)
    per_1000 = (count / words) * 1000
    score = 1.0 - min(per_1000 / 4, 1.0)
    return score


def hedging_score(text):
    text_lower = text.lower()
    words = len(text.split())
    if words < 20:
        return 0.5
    count = 0
    for h in HEDGES:
        count += text_lower.count(h)
    per_1000 = (count / words) * 1000
    score = 1.0 - min(per_1000 / 3, 1.0)
    return score


def get_weaknesses(signals):
    issues = []
    thresholds = {
        'burstiness': (0.35, 'Burstiness too low — sentence lengths barely vary'),
        'transition_density': (0.3, 'Too many formulaic transitions ("furthermore", "moreover", etc.)'),
        'ai_vocab_density': (0.5, 'AI vocabulary detected ("leverage", "delve", "navigate", etc.)'),
        'sentence_variance': (0.4, 'Sentence structure too uniform'),
        'repetitive_starts': (0.5, 'Too many sentences start the same way'),
        'signposting_density': (0.5, 'Signposting language detected ("this essay will", "let us explore")'),
        'em_dash_density': (0.5, 'Too many em dashes — use commas or separate sentences'),
        'passive_voice_ratio': (0.5, 'Passive voice overuse'),
        'paragraph_evenness': (0.4, 'Paragraphs too evenly sized'),
        'filler_density': (0.5, 'Filler phrases detected ("in order to", "due to the fact that")'),
        'hedging_density': (0.5, 'Over-hedging ("it could be argued", "this may indicate")'),
    }
    for key, (threshold, msg) in thresholds.items():
        if key in signals and signals[key] < threshold:
            issues.append(msg)
    return issues


def heuristic_detect(text):
    signals = {
        'burstiness': round(burstiness_score(text), 3),
        'sentence_variance': round(sentence_variance_score(text), 3),
        'transition_density': round(transition_density_score(text), 3),
        'ai_vocab_density': round(ai_vocab_score(text), 3),
        'repetitive_starts': round(repetitive_starts_score(text), 3),
        'signposting_density': round(signposting_score(text), 3),
        'em_dash_density': round(em_dash_score(text), 3),
        'passive_voice_ratio': round(passive_voice_score(text), 3),
        'paragraph_evenness': round(paragraph_evenness_score(text), 3),
        'filler_density': round(filler_score(text), 3),
        'hedging_density': round(hedging_score(text), 3),
    }

    score = 0.0
    total_weight = 0.0
    for key, weight in HEURISTIC_WEIGHTS.items():
        if key in signals:
            score += signals[key] * weight
            total_weight += weight

    if total_weight > 0:
        score = score / total_weight

    overall = round(score * 100, 1)
    weaknesses = get_weaknesses(signals)

    if overall >= 75:
        verdict = 'Likely human-written'
    elif overall >= 55:
        verdict = 'Mixed / uncertain'
    else:
        verdict = 'Likely AI-generated'

    return {
        'overall_score': overall,
        'verdict': verdict,
        'signals': signals,
        'weaknesses': weaknesses,
        'source': 'heuristic',
    }


def ml_detect(text):
    try:
        from transformers import pipeline
        import warnings
        warnings.filterwarnings('ignore')

        model = 'fakespot-ai/roberta-base-ai-text-detection-v1'
        pipe = pipeline('text-classification', model=model, tokenizer=model)

        if len(text) > 512:
            text = text[:512]

        result = pipe(text)
        label = result[0]['label']
        confidence = result[0]['score']

        if label.upper() == 'AI' or label.upper() == 'LABEL_1' or 'AI' in label:
            ml_score = (1 - confidence) * 100
        elif label.upper() == 'HUMAN' or label.upper() == 'REAL' or label.upper() == 'LABEL_0':
            ml_score = confidence * 100
        else:
            ml_score = 50.0

        if ml_score >= 75:
            verdict = 'Likely human-written'
        elif ml_score >= 55:
            verdict = 'Mixed / uncertain'
        else:
            verdict = 'Likely AI-generated'

        return {
            'overall_score': round(ml_score, 1),
            'verdict': verdict,
            'ml_raw': {'label': label, 'confidence': round(confidence, 4)},
            'source': 'ml_model',
        }
    except Exception as e:
        return {'error': f'ML model failed: {e}', 'source': 'ml_model'}


def main():
    text = None
    use_ml = False

    args = [a for a in sys.argv[1:] if a]

    i = 0
    while i < len(args):
        if args[i] == '--hf':
            use_ml = True
        elif args[i] == '-f' and i + 1 < len(args):
            with open(args[i + 1], 'r') as f:
                text = f.read()
            i += 1
        elif args[i] == '--help' or args[i] == '-h':
            print(__doc__)
            return
        elif not args[i].startswith('-'):
            text = args[i]
        i += 1

    if text is None:
        if not sys.stdin.isatty():
            text = sys.stdin.read()

    if text is None or not text.strip():
        print(json.dumps({'error': 'No text provided'}, indent=2))
        sys.exit(1)

    text = text.strip()
    if len(text.split()) < 10:
        print(json.dumps({'error': 'Text too short (min 10 words)', 'overall_score': 0, 'verdict': 'Too short'}, indent=2))
        sys.exit(1)

    heuristic = heuristic_detect(text)
    result = {'heuristic': heuristic}

    if use_ml:
        ml_result = ml_detect(text)
        result['ml'] = ml_result

        if 'error' not in ml_result:
            # Weighted blend: 40% heuristic, 60% ML
            blended = round(0.4 * heuristic['overall_score'] + 0.6 * ml_result['overall_score'], 1)
            result['overall_score'] = blended
            result['heuristic_weight'] = round(0.4 * heuristic['overall_score'], 1)
            result['ml_weight'] = round(0.6 * ml_result['overall_score'], 1)

            if blended >= 75:
                result['verdict'] = 'Likely human-written'
            elif blended >= 55:
                result['verdict'] = 'Mixed / uncertain'
            else:
                result['verdict'] = 'Likely AI-generated'

            # Weaknesses: heuristic weaknesses + ML note if it disagrees with heuristic
            combined = list(heuristic['weaknesses'])
            if ml_result['verdict'] != heuristic['verdict']:
                combined.append(
                    f'ML model disagrees with heuristic — flags as {ml_result["verdict"].lower()} '
                    f'(ML: {ml_result["overall_score"]:.0f}, heuristic: {heuristic["overall_score"]:.0f}, '
                    f'confidence: {ml_result["ml_raw"]["confidence"]:.0%})'
                )
            result['weaknesses'] = combined
        else:
            # ML failed, fall back to heuristic
            result['overall_score'] = heuristic['overall_score']
            result['verdict'] = heuristic['verdict']
            result['weaknesses'] = heuristic['weaknesses']
    else:
        result['overall_score'] = heuristic['overall_score']
        result['verdict'] = heuristic['verdict']
        result['weaknesses'] = heuristic['weaknesses']

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
