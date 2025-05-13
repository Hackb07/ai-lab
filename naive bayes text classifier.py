import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Sample text data
data = {
    'text': [
        'I love this product',
        'This is an amazing movie',
        'I hate this item',
        'This is the worst experience',
        'What a great day!',
        'Terrible performance',
        'Absolutely loved it',
        'Not good at all',
        'Best I have ever seen',
        'Awful and disappointing'
    ],
    'label': [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]  # 1 = Positive, 0 = Negative
}

df = pd.DataFrame(data)

# Text vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy : {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall   : {recall * 100:.2f}%")

# --- User Input Section ---
print("\n--- Sentiment Prediction ---")
user_input = input("Enter a sentence to analyze its sentiment: ")

# Transform and predict
user_vector = vectorizer.transform([user_input])
prediction = model.predict(user_vector)[0]

sentiment = "Positive" if prediction == 1 else "Negative"
print(f"Predicted Sentiment: {sentiment}")
