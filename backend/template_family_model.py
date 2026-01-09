# Multinomial Logistic Regression Model

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

class TemplateFamilyModel:
    def __init__(self, captions, families):
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
        X = self.vectorizer.fit_transform(captions)  # Convert captions to TF-IDF
        self.model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=200)
        self.model.fit(X, families)  # Train model

    def predict_family(self, caption):
        # Predict the template family for the caption
        X = self.vectorizer.transform([caption])
        return self.model.predict(X)[0]  # Return the predicted family label

# Example usage
if __name__ == "__main__":
    # Training data: captions and their families
    captions = [
        "playful spring sale", "bold summer event", "elegant winter gala", "retro pop party",
        "tech future expo", "calm nature retreat", "urban night market", "cozy autumn fair"
    ]
    families = [
        "Playful", "Bold", "Elegant", "Retro",
        "Tech", "Calm", "Modern", "Warm"
    ]
    # Create and train the model
    model = TemplateFamilyModel(captions, families)
    # Predict for a new caption
    test_caption = "playful spring sale with flowers and bright colors"
    family = model.predict_family(test_caption)
    print(f"Predicted family: {family}")