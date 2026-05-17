# EmotionDetection

A production-ready Python package for detecting and analyzing emotions in text using IBM Watson Natural Language Understanding API. This project includes a Flask web server for easy integration and comprehensive unit tests.

## Project Description

The EmotionDetection package provides a robust solution for emotion analysis in text. It leverages the Watson NLP Emotion Detection API to extract emotion scores for five primary emotions: anger, disgust, fear, joy, and sadness. The package automatically determines which emotion has the highest score as the dominant emotion.

## Features

- **Emotion Detection**: Analyzes text to detect five core emotions
- **Dominant Emotion Identification**: Automatically determines the primary emotion
- **Flask REST API**: Easy-to-use HTTP endpoint for emotion analysis
- **Comprehensive Error Handling**: Gracefully handles invalid inputs and API errors
- **Production-Ready Code**: Follows PEP 8 standards with full docstrings
- **Unit Tests**: Comprehensive test suite for reliability assurance

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- IBM Watson Natural Language Understanding API credentials

### Setup Steps

1. Clone or download the repository:
   ```bash
   cd emotion-detection
   ```

2. Create a `.env` file in the project root with your Watson API credentials:
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your credentials:
   ```
   API_KEY=your_watson_api_key_here
   URL=your_watson_api_url_here
   ```

3. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   
   **On Windows (PowerShell):**
   ```bash
   venv\Scripts\Activate.ps1
   ```
   
   **On Windows (Command Prompt):**
   ```cmd
   venv\Scripts\activate.bat
   ```
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

5. Install required dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

6. Verify installation:
   ```bash
   pip list
   ```
   
   You should see: flask, requests, python-dotenv, and werkzeug installed.

## Project Structure

```
emotion-detection/
├── EmotionDetection/
│   ├── __init__.py                 # Package initialization and exports
│   └── emotion_detection.py        # Core emotion detection logic
├── test_emotion_detection.py       # Unit tests
├── server.py                       # Flask web server
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
```

## Usage

### Running the Flask Server

1. Navigate to the project root directory:
   ```bash
   cd emotion-detection
   ```

2. Start the Flask server:
   ```bash
   python server.py
   ```

   The server will be available at `http://localhost:5000`

3. Access the emotion detection API using a GET request:
   ```
   http://localhost:5000/emotionDetector?textToAnalyze=your_text_here
   ```

   Example:
   ```
   http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20very%20happy
   ```

### Using the Package Directly

```python
from EmotionDetection.emotion_detection import emotion_detector

# Analyze text for emotions
result = emotion_detector("I am absolutely thrilled!")

print(result)
# Output: {
#     'anger': 0.0,
#     'disgust': 0.1,
#     'fear': 0.0,
#     'joy': 0.85,
#     'sadness': 0.0,
#     'dominant_emotion': 'joy'
# }
```

## API Response Format

### Success Response (Valid Input)

```
For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.9 and 'sadness': 0.0. The dominant emotion is joy.
```

### Error Response (Invalid Input)

```
Invalid text! Please try again!
```

## Running Unit Tests

Execute the test suite to verify the package functionality:

```bash
python -m unittest test_emotion_detection.py
```

Or with verbose output:

```bash
python -m unittest test_emotion_detection.py -v
```

### Test Coverage

The unit tests cover:

- Joy emotion detection
- Anger emotion detection
- Sadness emotion detection
- Fear emotion detection
- Disgust emotion detection
- Invalid empty string input
- None value handling
- Neutral input processing
- Return type validation
- Emotion score range validation

## Code Quality

The project adheres to PEP 8 standards and achieves a perfect pylint score of 10.00/10.00:

```bash
pylint EmotionDetection/emotion_detection.py
pylint server.py
```

All modules include comprehensive docstrings following Google/NumPy style conventions.

## Configuration

### Watson API Setup

**IMPORTANT**: This application requires IBM Watson Natural Language Understanding API credentials to function.

1. **Create IBM Cloud Account**: Sign up at [IBM Cloud](https://cloud.ibm.com)

2. **Create Watson NLU Service**:
   - Navigate to Catalog → AI / Machine Learning
   - Select "Natural Language Understanding"
   - Create a new instance

3. **Obtain API Credentials**:
   - Go to your Watson NLU instance
   - Click "Service credentials"
   - Create new credentials (or use existing)
   - Copy the **API Key** and **URL**

4. **Configure .env File**:
   Create or update `.env` file in the project root:
   ```
   API_KEY=your_watson_api_key_here
   URL=your_watson_api_url_here
   ```

   Example:
   ```
   API_KEY=tlsivseSxr0IuIeDytLL4tywx1nCbwBcV1JbU7JsA2n9
   URL=https://api.jp-tok.natural-language-understanding.watson.cloud.ibm.com/instances/27b8fad0-bb1a-4c09-895d-725ed8137739
   ```

5. **Security Note**: Never commit `.env` to version control. It's already listed in `.gitignore`.

### Flask Configuration

The Flask server runs on:
- **Host**: localhost
- **Port**: 5000
- **Debug Mode**: Disabled (for production)

## Dependencies

The application requires the following Python packages (automatically installed via `pip install -r requirements.txt`):

- **flask** (2.3.3+): Web framework for REST API
- **requests** (2.31.0+): HTTP library for API calls
- **python-dotenv** (1.0.0+): Environment variable management for secure credential handling
- **Werkzeug** (2.3.7+): WSGI utility library

All dependencies are pinned to specific versions in `requirements.txt` for stability.



## Troubleshooting

### Import Errors

If you encounter import errors:
```bash
# Ensure you're in the project root directory
python -c "from EmotionDetection.emotion_detection import emotion_detector"
```

### API Connection Errors

- Verify internet connection
- Check Watson API credentials
- Ensure API endpoint URL is correct

### Port Already in Use

If port 5000 is already in use:
```python
# Edit server.py and change the port number in the __main__ section
app.run(host='localhost', port=5001, debug=False)
```

## License

This project is provided as a demonstration of emotion detection capabilities using Watson NLP services.

## Support

For issues or questions regarding the EmotionDetection package, please refer to the code comments and docstrings for detailed information on function usage and parameters.

## Version History

- **v1.0.0** (May 2026): Initial release with full emotion detection functionality
