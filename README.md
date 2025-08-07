# Text Similarity Detection API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/github/license/Leon24k/TextSimilarity)

## Overview

Text Similarity Detection API is a Flask-based RESTful service that leverages a pre-trained TensorFlow model to predict the similarity between two pieces of text. Designed for flexibility and integration, this API is ideal for applications such as plagiarism checking, content recommendation, or semantic search.

---

## Features

- **Pre-trained Model:** Utilizes a TensorFlow model for accurate similarity predictions.
- **Automated Tokenization:** Initializes and uses a tokenizer with a sample vocabulary.
- **Easy-to-use REST API:** 
  - `/predict` endpoint for real-time similarity scoring.
- **Simple Setup:** Minimal configuration required; just clone, add your model, and run.

---

## Requirements

- Python 3.8+
- Flask
- TensorFlow
- NumPy

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## File Structure

```
TextSimilarity/
├── app.py                 # Main Flask application
├── model/                 # Directory to store the pre-trained model
│   └── final_model.h5     # Pre-trained model file
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Leon24k/TextSimilarity.git
   cd TextSimilarity
   ```

2. **Add your pre-trained model:**
   - Place `final_model.h5` in the `model/` directory.

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Test the API:**
   - Use Postman, curl, or your browser.

   **Example using curl:**
   ```bash
   curl -X POST -H "Content-Type: application/json" \
     -d '{"text1": "Text one here", "text2": "Text two here"}' \
     http://127.0.0.1:5000/predict
   ```

---

## API Usage

### `/predict` Endpoint

- **Method:** `POST`
- **Request Body:**

    ```json
    {
      "text1": "I love programming.",
      "text2": "Coding is my passion."
    }
    ```

- **Response:**

    ```json
    {
      "similarity_score": 0.85
    }
    ```

---

## Development & Contribution

Contributions, feature requests, and bug reports are encouraged! Please submit issues or pull requests via GitHub.

---

## Troubleshooting

- Ensure your model is named `final_model.h5` and located in the `model/` directory.
- Verify Python and package versions match the requirements.
- If you encounter errors, check the Flask output for debugging information.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as needed.

---

## Contact

For questions or support, open an issue or reach out via [GitHub Issues](https://github.com/Leon24k/TextSimilarity/issues).
