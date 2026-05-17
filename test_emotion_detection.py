"""
Unit Tests for Emotion Detection Module

This module contains comprehensive unit tests for the emotion_detector function.
Tests include validation of emotion detection accuracy across different emotional
contexts, as well as error handling for invalid inputs.
"""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_dominant_emotion_joy(self):
        """
        Test that joy is correctly identified as the dominant emotion.

        This test verifies that a statement with joyful content returns
        'joy' as the dominant emotion.
        """
        result = emotion_detector("I am very happy and delighted!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_dominant_emotion_anger(self):
        """
        Test that anger is correctly identified as the dominant emotion.

        This test verifies that a statement with angry content returns
        'anger' as the dominant emotion.
        """
        result = emotion_detector("This is absolutely outrageous and infuriating!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_dominant_emotion_sadness(self):
        """
        Test that sadness is correctly identified as the dominant emotion.

        This test verifies that a statement with sad content returns
        'sadness' as the dominant emotion.
        """
        result = emotion_detector("I feel very sad today and completely devastated.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_dominant_emotion_fear(self):
        """
        Test that fear is correctly identified as the dominant emotion.

        This test verifies that a statement with fearful content returns
        'fear' as the dominant emotion.
        """
        result = emotion_detector("I am terrified and extremely scared!")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_dominant_emotion_disgust(self):
        """
        Test that disgust is correctly identified as the dominant emotion.

        This test verifies that a statement with disgusting content returns
        'disgust' as the dominant emotion.
        """
        result = emotion_detector("This is absolutely disgusting and repulsive!")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_invalid_input_empty_string(self):
        """
        Test that empty string returns None as dominant emotion.

        This test verifies that an empty string input returns a result
        with all emotion scores at 0.0 and dominant_emotion as None.
        """
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])

    def test_invalid_input_none_value(self):
        """
        Test that None value handling doesn't cause exceptions.

        This test verifies that the function gracefully handles None input.
        """
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])

    def test_neutral_input(self):
        """
        Test processing of neutral content.

        This test verifies that neutral statements are processed without
        raising exceptions and return a valid result dictionary.
        """
        result = emotion_detector("The sky is blue.")
        self.assertIn('dominant_emotion', result)
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)

    def test_return_type(self):
        """
        Test that emotion_detector returns a valid dictionary.

        This test verifies that the function returns a dictionary with
        all required emotion keys.
        """
        result = emotion_detector("Test statement")
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 6)

    def test_emotion_scores_range(self):
        """
        Test that emotion scores are within valid range.

        This test verifies that all emotion scores are numeric and
        typically within the range [0.0, 1.0].
        """
        result = emotion_detector("I am feeling great and wonderful!")
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
            self.assertIsInstance(result[emotion], (int, float))
            self.assertGreaterEqual(result[emotion], 0.0)


if __name__ == '__main__':
    unittest.main()
