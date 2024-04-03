from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input text from the form
    text = request.form['text']
    
    # Vectorize the input text
    text_vectorized = vectorizer.transform([text])
    
    # Make prediction
    prediction = model.predict(text_vectorized)
    
    print("Prediction:", prediction)
    # Map prediction to human-readable emotion
    emotion_mapping = {
        0: 'sadness',
        1: 'joy',
        2: 'love',
        3: 'anger',
        4: 'fear',
        5: 'surprise'
    }
    predicted_emotion = emotion_mapping[prediction[0]]
    
    # Render the result template with the predicted emotion
    return render_template("index.html", prediction_text = "The emotion is {}".format(predicted_emotion))

if __name__ == '__main__':
    app.run(debug=True)
