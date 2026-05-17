"""
Emotion Detection Module

This module provides functionality to detect emotions in text using the Watson
NLP Emotion Detection API. It extracts emotion scores and determines the
dominant emotion based on the highest score.
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Watson API credentials from environment variables
WATSON_API_KEY = os.getenv('API_KEY')
WATSON_URL = os.getenv('URL')


def emotion_detector(text_to_analyze):
    """
    Analyze text and detect emotions using Watson Emotion Detection API.

    This function sends the provided text to the Watson Emotion Detection API
    and retrieves emotion scores for: anger, disgust, fear, joy, and sadness.
    It then determines which emotion has the highest score as the dominant
    emotion.

    Args:
        text_to_analyze (str): The text string to analyze for emotional content.

    Returns:
        dict: A dictionary containing emotion scores for 'anger', 'disgust',
              'fear', 'joy', 'sadness', and 'dominant_emotion'. If the input
              is invalid or the API returns a 400 status, all values are set
              to 0.0 and 'dominant_emotion' is set to None.

    Example:
        >>> result = emotion_detector("I am happy today")
        >>> print(result['dominant_emotion'])
        'joy'
    """
    # Initialize response dictionary with default values
    emotion_result = {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0,
        'dominant_emotion': None
    }

    # Check for invalid/blank input first
    if not text_to_analyze or not text_to_analyze.strip():
        return emotion_result

    # ============================================================
    # WATSON API MODE: Watson NLP Emotion Detection
    # ============================================================
    # Initialize Watson API endpoint with version parameter
    url = f"{WATSON_URL}/v1/analyze?version=2021-08-01"

    # Headers for API request
    headers = {
        "Content-Type": "application/json"
    }

    # Payload for API request with correct format for Watson NLU
    payload = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    try:
        # Make API request to Watson NLP service
        # Use apikey as username with basic authentication
        response = requests.post(
            url, 
            json=payload, 
            headers=headers, 
            auth=('apikey', WATSON_API_KEY),
            timeout=10
        )
        # Check for 400 Bad Request
        if response.status_code == 400:
            return emotion_result

        # Only process successful responses
        if response.status_code == 200:
            # Parse response JSON
            response_data = response.json()

            # Navigate to emotion scores in the response
            # Watson response structure: {"emotion": {"document": {"emotion": {...}}}}
            if 'emotion' in response_data and 'document' in response_data['emotion']:
                emotion_scores = response_data['emotion']['document']['emotion']

                # Extract emotion scores
                emotion_result['anger'] = emotion_scores.get('anger', 0.0)
                emotion_result['disgust'] = emotion_scores.get('disgust', 0.0)
                emotion_result['fear'] = emotion_scores.get('fear', 0.0)
                emotion_result['joy'] = emotion_scores.get('joy', 0.0)
                emotion_result['sadness'] = emotion_scores.get('sadness', 0.0)

                # Determine dominant emotion (highest score)
                emotions = {
                    'anger': emotion_result['anger'],
                    'disgust': emotion_result['disgust'],
                    'fear': emotion_result['fear'],
                    'joy': emotion_result['joy'],
                    'sadness': emotion_result['sadness']
                }
                emotion_result['dominant_emotion'] = max(emotions, key=emotions.get)

    except requests.exceptions.RequestException as e:
        # Handle network errors or API unavailability
        print(f"API Request Error: {e}")
        return emotion_result
    except (KeyError, ValueError) as e:
        # Handle JSON parsing or key access errors
        print(f"JSON Parsing Error: {e}")
        return emotion_result

    return emotion_result

    # ============================================================
    # DEMO MODE (COMMENTED OUT): Keyword-based emotion detection
    # Uncomment below to use demo mode (useful for testing without API)
    # ============================================================
    # text_lower = text_to_analyze.lower()
    # emotion_scores = {emotion: 0.0 for emotion in emotion_result.keys() if emotion != 'dominant_emotion'}
    #
    # # Demo keyword mappings
    # EMOTION_KEYWORDS = {
    #     'joy': ['happy', 'delighted', 'love', 'excellent', 'great', 'wonderful', 'thrilled', 'excited', 'amazing'],
    #     'anger': ['angry', 'furious', 'outrageous', 'infuriating', 'terrible', 'hate', 'disgusted', 'mad'],
    #     'sadness': ['sad', 'devastated', 'unhappy', 'miserable', 'depressed', 'sorrowful', 'grief', 'lonely'],
    #     'fear': ['terrified', 'scared', 'afraid', 'fearful', 'frightened', 'anxious', 'nervous', 'panic'],
    #     'disgust': ['disgusting', 'repulsive', 'gross', 'nasty', 'vile', 'horrible', 'revolting', 'abhorrent']
    # }
    #
    # # Count keyword occurrences for each emotion
    # for emotion, keywords in EMOTION_KEYWORDS.items():
    #     for keyword in keywords:
    #         emotion_scores[emotion] += text_lower.count(keyword) * 0.1
    #
    # # Normalize scores to be between 0 and 1
    # max_score = max(emotion_scores.values()) if max(emotion_scores.values()) > 0 else 1
    # if max_score > 1:
    #     emotion_scores = {k: v / max_score for k, v in emotion_scores.items()}
    #
    # # Update result with calculated scores
    # for emotion, score in emotion_scores.items():
    #     emotion_result[emotion] = round(score, 2)
    #
    # # Determine dominant emotion
    # if max(emotion_scores.values()) > 0:
    #     emotion_result['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)
    #
    # return emotion_result

