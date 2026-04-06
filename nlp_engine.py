import spacy
from pdfminer.high_level import extract_text
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

GENERIC_WORDS = {
    "paper", "result", "method", "analysis", "approach", "study",
    "model", "data", "work", "system", "research", "use", "used"
}

def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text if text else ""
    except Exception:
        return ""

def clean_text_for_nlp(text):
    doc = nlp(text.lower())
    words = []

    for token in doc:
        if (
            token.is_alpha
            and not token.is_stop
            and len(token.text) > 2
            and token.lemma_ not in GENERIC_WORDS
        ):
            words.append(token.lemma_)

    return words

def get_frequent_tags(text, top_n=8):
    words = clean_text_for_nlp(text)
    freq = Counter(words)
    return [word for word, count in freq.most_common(top_n)]

def get_important_tags(text, top_n=8):
    doc = nlp(text.lower())

    phrases = []
    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip()
        if len(phrase.split()) <= 4 and len(phrase) > 3:
            if not any(word in GENERIC_WORDS for word in phrase.split()):
                phrases.append(phrase)

    if not phrases:
        words = clean_text_for_nlp(text)
        joined_text = " ".join(words)
        vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=20)
        X = vectorizer.fit_transform([joined_text])
        return list(vectorizer.get_feature_names_out())[:top_n]

    vectorizer = TfidfVectorizer(max_features=20)
    X = vectorizer.fit_transform(phrases)
    scores = zip(vectorizer.get_feature_names_out(), X.sum(axis=0).A1)
    sorted_terms = sorted(scores, key=lambda x: x[1], reverse=True)

    important = []
    for term, score in sorted_terms:
        if term not in important and term not in GENERIC_WORDS:
            important.append(term)

    return important[:top_n]