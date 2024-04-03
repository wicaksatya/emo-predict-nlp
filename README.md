# Emotion Detection Web API

## Overview

This project implements a Flask web application that serves as a web API for emotion detection. The web application allows users to input text, and based on a trained machine learning model, predicts the emotion conveyed by the input text.

## Features

- **Input Text:** Users can input text through a web form.
- **Emotion Prediction:** The application predicts the emotion conveyed by the input text using a trained machine learning model.
- **Display:** The predicted emotion is displayed to the user.

## Getting Started
1. Prerequisites:
   * Python 3.x (https://www.python.org/downloads/)
   * Flask (https://flask.palletsprojects.com/)
   * joblib (https://scikit-learn.org/stable/model_persistence.html)
   * NLTK (for text processing, install using `pip install nltk`)
    
2. Clone the repository:
   `git clone https://github.com/your_username/emotion-detection-web-api.git`

3. Model File:
   * Replace 'model.pkl' in app.py with the actual filename of your trained model
   * Ensure the model file is present in the same directory as `app.py`.

4. Run and Access the App:
   * In the terminal, run: `py app.py`
   * Open `http://127.0.0.1:5000/` in your web browser.

## Development
* This code serves as a starting point for further development and customization.
* You can improve the text pre-processing steps (clean_text) and feature extraction (extract_features) based on your specific model and dataset.
   
