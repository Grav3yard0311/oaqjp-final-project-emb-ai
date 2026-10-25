"""Unit tests for the EmotionDetection package."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_emotion_detector_anger(self):
        """Anger is the dominant emotion for an angry statement."""
        result = emotion_detector("I am angry about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        """Disgust is the dominant emotion for a disgusting statement."""
        result = emotion_detector("I feel disgusted by this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_fear(self):
        """Fear is the dominant emotion for a fearful statement."""
        result = emotion_detector("I am scared of this")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_emotion_detector_joy(self):
        """Joy is the dominant emotion for a joyful statement."""
        result = emotion_detector("I am so happy about this")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_sadness(self):
        """Sadness is the dominant emotion for a sad statement."""
        result = emotion_detector("I feel depressed about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == "__main__":
    unittest.main()
