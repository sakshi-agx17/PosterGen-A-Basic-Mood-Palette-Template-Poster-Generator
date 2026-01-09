# Keyword Extraction

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class TfidfKeywordExtractor:
    def __init__(self, max_features=20):
        corpus = [
            "playful spring sale", "bold summer event", "elegant winter gala", "retro pop party",
            "tech future expo", "calm nature retreat", "urban night market", "cozy autumn fair"
        ]
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=max_features)
        self.vectorizer.fit(corpus)

    def extract_keywords(self, caption, top_n=5):
        tfidf_matrix = self.vectorizer.transform([caption])
        scores = tfidf_matrix.toarray()[0]
        feature_names = self.vectorizer.get_feature_names_out()
        keywords = [feature_names[i] for i in np.argsort(scores)[::-1] if scores[i] > 0][:top_n]
        return keywords

if __name__ == "__main__":
    extractor = TfidfKeywordExtractor()
    caption = "playful spring sale with flowers and bright colors"
    print("Extracted keywords:", extractor.extract_keywords(caption))
