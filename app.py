from flask import Flask, render_template, request, jsonify
import re
import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote

app = Flask(__name__)

# ==============================
# KEYWORD EXTRACTION
# ==============================
def extract_keywords(text):
    stopwords = {
        "the", "is", "in", "on", "at", "of", "and",
        "a", "an", "to", "for", "with", "by", "that",
        "this", "was", "are", "as", "it"
    }

    words = re.findall(r"\b[A-Za-z]{3,}\b", text)
    keywords = [w for w in words if w.lower() not in stopwords]

    return keywords[:5]


# ==============================
# GOOGLE NEWS SEARCH (WORKING)
# ==============================
def search_google_news(user_text):

    keywords = extract_keywords(user_text)
    if not keywords:
        return []

    query = quote(" ".join(keywords))
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            return []

        root = ET.fromstring(response.content)
        articles = []

        for item in root.findall(".//item"):
            title = item.find("title").text
            link = item.find("link").text

            articles.append({
                "title": title,
                "url": link
            })

        return articles[:6]

    except:
        return []


# ==============================
# HOME
# ==============================
@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# ANALYZE ROUTE
# ==============================
@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    text = data.get("text", "").strip()

    response = {
        "verdict": "",
        "confidence": 0,
        "warnings": [],
        "news": []
    }

    # EMPTY INPUT
    if not text:
        response["verdict"] = "No Input"
        return jsonify(response)

    score = 0

    # PERSONAL INFO DETECTION
    personal_patterns = [
        r"\bmy name is\b",
        r"\bi am\b",
        r"\b\d{10}\b",
        r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"
    ]

    for pattern in personal_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            response["warnings"].append(
                "Personal information detected. Sharing private data publicly may be unsafe."
            )
            score += 30
            break

    # EMOJI ANALYSIS
    emoji_map = {
        "🔥": "creates hype or urgency",
        "👇": "directs attention or manipulation",
        "😡": "indicates anger or emotional appeal",
        "😂": "used for mockery or exaggeration"
    }

    for emoji, meaning in emoji_map.items():
        if emoji in text:
            response["warnings"].append(
                f"Emoji {emoji} {meaning}."
            )
            score += 15

    # MANIPULATIVE LANGUAGE
    sensational_words = ["breaking", "shocking", "secret", "urgent", "exclusive"]

    for word in sensational_words:
        if word in text.lower():
            response["warnings"].append(
                "Manipulative or sensational language detected."
            )
            score += 20
            break

    # DETERMINE VERDICT
    if score >= 60:
        response["verdict"] = "High Risk"
    elif score >= 30:
        response["verdict"] = "Warning"
    else:
        response["verdict"] = "Safe"

    response["confidence"] = score

    # SEARCH GLOBAL NEWS (ONLY IF NOT PERSONAL ONLY)
    if response["verdict"] != "Warning" or score < 30:
        response["news"] = search_google_news(text)

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
