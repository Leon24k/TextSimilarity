# Text Similarity Detection API

This repository contains a Flask-based API for detecting text similarity using a pre-trained TensorFlow model. The application preprocesses input texts, tokenizes them, and uses the model to predict the similarity score between two text inputs.

## Features

- **Pre-trained Model**: The application uses a TensorFlow model for similarity predictions.
- **Tokenizer Initialization**: Automatically initializes a tokenizer with a sample vocabulary.
- **REST API Endpoints**:
  - `/predict`: Predicts the similarity between two text inputs.

---

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.8+
- Flask
- TensorFlow
- NumPy
- Pycharm / Collab / Ipynb

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

4. **Access the API**:
   - Open your browser or use a tool like `curl` or Postman to test the API.
   - Example for `/predict` endpoint:
     ```bash
     curl -X POST -H "Content-Type: application/json" \
     -d '{"text1": "Text one here", "text2": "Text two here"}' \
     http://127.0.0.1:5000/predict
     ```

## Example Response

### `/predict` Endpoint
Request:
```json
{
  "text1": "I love programming.",
  "text2": "Coding is my passion."
}
```

Response:
```json
{
  "similarity_score": 0.85
}
```
## Contribution Guidelines

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.😇

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as needed.

