import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Global variables for model and tokenizer
model = None
tokenizer = None
max_length = 40  # Adjust to your dataset


# Predefined tokenizer configuration
def initialize_tokenizer():
    global tokenizer

    # Define tokenizer and fit with sample vocabulary (customize this)
    tokenizer = Tokenizer(
        num_words=20000,  # Limit the vocabulary size
        oov_token="<UNK>"  # Token for words not in vocabulary
    )

    # Example sentences (replace with real training sentences if available)
    example_sentences = ["this is a sentence", "another example sentence", "text similarity detection"]
    tokenizer.fit_on_texts(example_sentences)

    print("Tokenizer initialized successfully!")
    print(f"Vocabulary size: {len(tokenizer.word_index)}")


# Load the model
def load_model():
    global model
    try:
        model = tf.keras.models.load_model('/model/final_model.h5')
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        raise


# Preprocess input texts
def preprocess_texts(text1, text2):
    """Preprocess input texts"""

    def clean_text(text):
        if isinstance(text, str):
            text = text.lower().strip()
            text = ' '.join(text.split())
            return text
        return ''

    text1 = clean_text(text1)
    text2 = clean_text(text2)

    if tokenizer is None:
        raise ValueError("Tokenizer not initialized!")

    seq1 = tokenizer.texts_to_sequences([text1])
    seq2 = tokenizer.texts_to_sequences([text2])

    pad1 = pad_sequences(seq1, maxlen=max_length, padding='post', truncating='post')
    pad2 = pad_sequences(seq2, maxlen=max_length, padding='post', truncating='post')

    return pad1, pad2


@app.route('/predict', methods=['POST'])
def predict_similarity():
    try:
        data = request.get_json()
        text1 = data.get('text1', '')
        text2 = data.get('text2', '')

        if not text1 or not text2:
            return jsonify({'error': 'Both text1 and text2 are required', 'status': 'failed'}), 400

        pad1, pad2 = preprocess_texts(text1, text2)
        similarity_score = model.predict([pad1, pad2])[0][0]

        return jsonify({
            'text1': text1,
            'text2': text2,
            'similarity_score': float(similarity_score),
            'is_similar': similarity_score > 0.5,
            'status': 'success'
        })

    except Exception as e:
        return jsonify({'error': str(e), 'status': 'failed'}), 500


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'tokenizer_initialized': tokenizer is not None
    })


if __name__ == '__main__':
    initialize_tokenizer()  # Initialize tokenizer
    load_model()  # Load model
    app.run(host='0.0.0.0', port=5000, debug=True)
