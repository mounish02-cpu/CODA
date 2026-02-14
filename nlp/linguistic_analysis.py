import spacy
nlp = spacy.load("en_core_web_sm")

def analyze_linguistics(text):
    doc = nlp(text)
    indicators = {
        "emotional_language": [],
        "urgency_bias": [],
        "authority_framing": []
    }

    for token in doc:
        if token.text.lower() in ["shocking", "urgent", "breaking"]:
            indicators["urgency_bias"].append(token.text)
        if token.pos_ == "ADJ" and token.sentiment != 0:
            indicators["emotional_language"].append(token.text)

    return indicators
