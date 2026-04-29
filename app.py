from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import fitz
import nltk
import re
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

app = Flask(__name__)
CORS(app)

# -----------------------------
# 🔹 Extract text from PDF
# -----------------------------
def extract_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")

    text = []
    for page in doc:
        content = page.get_text()
        if content:
            text.append(content)

    return " ".join(text)


# -----------------------------
# 🔹 Smart Semantic Analysis
# -----------------------------
def analyze(text):

    # Clean text
    text = text.lower()
    text = re.sub(r'[^a-z\s\.]', '', text)

    # -------------------------
    # TF-IDF Keywords
    # -------------------------
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform([text])

    keywords = vectorizer.get_feature_names_out().tolist()

    # -------------------------
    # Word Frequency
    # -------------------------
    words = text.split()
    clean_words = [
        w for w in words
        if w not in stop_words and len(w) > 3
    ]

    common = Counter(clean_words).most_common(10)

    # -------------------------
    # Domain
    # -------------------------
    if len(keywords) >= 2:
        domain = f"Research related to {keywords[0]} and {keywords[1]}"
    else:
        domain = "General Research"

    # -------------------------
    # Insight
    # -------------------------
    if len(keywords) >= 4:
        summary = (
            f"This research paper focuses on {keywords[0]} and {keywords[1]}. "
            f"It explores techniques related to {keywords[2]} and {keywords[3]}, "
            f"and highlights their applications in practical scenarios."
        )
    else:
        summary = "This research paper presents important concepts and findings."

    # -------------------------
    # Tags
    # -------------------------
    tags = []
    for i in range(len(keywords) - 2):
        phrase = f"{keywords[i]} {keywords[i+1]} {keywords[i+2]}"
        tags.append(phrase)

    tags = list(set(tags))

    # -------------------------
    # Important Sentences
    # -------------------------
    sentences = text.split('.')
    scored_sentences = []

    for sentence in sentences:
        score = sum(1 for word in keywords if word in sentence)
        if score > 0 and len(sentence.strip()) > 40:
            scored_sentences.append((sentence.strip(), score))

    top_sentences = [
        s[0] for s in sorted(scored_sentences, key=lambda x: x[1], reverse=True)[:2]
    ]

    # -------------------------
    # 🔥 Keyword Meanings (NEW FEATURE)
    # -------------------------
    keyword_meanings = {}

    for keyword in keywords[:5]:
        for sentence in sentences:
            sentence = sentence.strip()
            if keyword in sentence and len(sentence) > 40:
                keyword_meanings[keyword] = sentence
                break

    # -------------------------
    # Confidence
    # -------------------------
    confidence = round((len(keywords) / 10) * 100, 2)

    return keywords, common, summary, tags, domain, confidence, top_sentences, keyword_meanings


# -----------------------------
# 🔹 API Route
# -----------------------------
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    text = extract_text(file)

    if not text.strip():
        return jsonify({"error": "Could not extract text"}), 400

    keywords, common, summary, tags, domain, confidence, top_sentences, keyword_meanings = analyze(text)

    return jsonify({
        "file": file.filename,
        "keywords": keywords,
        "common": common,
        "summary": summary,
        "tags": tags,
        "domain": domain,
        "confidence": confidence,
        "top_sentences": top_sentences,
        "keyword_meanings": keyword_meanings
    })


# -----------------------------
# 🔹 Run Server
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)