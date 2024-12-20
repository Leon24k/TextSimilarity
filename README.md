# Text Similarity Detection API

This repository contains a Flask-based API for detecting text similarity using a pre-trained TensorFlow model. The application preprocesses input texts, tokenizes them, and uses the model to predict the similarity score between two text inputs.

## Features

- **Pre-trained Model**: The application uses a TensorFlow model for similarity predictions.
- **Tokenizer Initialization**: Automatically initializes a tokenizer with a sample vocabulary.
- **REST API Endpoints**:
  - `/predict`: Predicts the similarity between two text inputs.
  - `/health`: Checks the health of the application.

---

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.8+
- Flask
- TensorFlow
- NumPy

Install dependencies using:
```bash
pip install -r requirements.txt
```

## File Structure
```
project/
├── app.py                 # Main Flask application
├── model/                 # Directory to store the pre-trained model
│   └── final_model.h5     # Pre-trained model file
└── requirements.txt       # Python dependencies
```

## Setup
1. Clone this repository:
```
git clone https://github.com/your-repo/text-similarity-api.git
cd text-similarity-api
```
2. Place the pre-trained model (final_model.h5) in the model/ directory.

3. Initialize the application:
```
python app.py
```
