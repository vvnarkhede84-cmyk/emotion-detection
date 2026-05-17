"""
Emotion Detection Flask Server

This module implements a Flask web server that exposes the emotion detection
functionality through a REST API endpoint. It handles text input from clients,
processes it using the emotion detector module, and returns formatted
emotion analysis results.
"""

from flask import Flask, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Handle emotion detection requests.

    This route processes GET requests with a textToAnalyze query parameter,
    analyzes the text using the emotion detector, and returns either a
    formatted response with emotion scores or an error message if the input
    is invalid.

    Returns:
        str: A formatted string with emotion scores and dominant emotion,
             or an error message for invalid input.

    Example:
        GET /emotionDetector?textToAnalyze=I%20am%20very%20happy

    Status Codes:
        200: Successfully processed the request
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)
    # Check if dominant emotion is None (invalid input or API error)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response string with emotion scores and dominant emotion
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']:.1f}, "
        f"'disgust': {result['disgust']:.1f}, "
        f"'fear': {result['fear']:.1f}, "
        f"'joy': {result['joy']:.1f} and "
        f"'sadness': {result['sadness']:.1f}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


@app.route('/', methods=['GET'])
def index():
    """
    Handle root endpoint.

    Returns:
        str: A welcome message with API usage instructions.
    """
    return (
        "Welcome to the Emotion Detection API. "
        "Use /emotionDetector?textToAnalyze=<your_text> to detect emotions."
    )


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
