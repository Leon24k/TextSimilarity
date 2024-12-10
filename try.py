import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import model_from_json
import tensorflow.keras as keras

app = Flask(__name__)

# Enable unsafe deserialization to handle Lambda layers
keras.config.enable_unsafe_deserialization()

# Load the saved model architecture and weights
with open('model_architecture.json', 'r') as json_file:
    model_json = json_file.read()
# Use safe_mode=False to allow lambda deserialization
model = model_from_json(model_json, safe_mode=False)
model.load_weights('model_weights.h5')

# Endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Expecting 'input_1' and 'input_2' in the JSON request
        input_1 = np.array(data['input_1']).reshape(1, -1)
        input_2 = np.array(data['input_2']).reshape(1, -1)

        # Ensure the input length matches the expected length (200 in this case)
        if input_1.shape[1] != 200 or input_2.shape[1] != 200:
            return jsonify({'error': 'Input length must be 200'}), 400

        # Make the prediction
        prediction = model.predict([input_1, input_2])

        # Return the prediction as JSON
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)