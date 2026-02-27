import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        # Helper function to mock the response
        def get_mock_response(dominant):
            scores = {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0
            }
            scores[dominant] = 1.0
            
            mock_resp = unittest.mock.Mock()
            mock_resp.status_code = 200
            import json
            mock_resp.text = json.dumps({"emotionPredictions": [{"emotion": scores}]})
            return mock_resp

        # Case 1: Joy
        mock_post.return_value = get_mock_response('joy')
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Case 2: Anger
        mock_post.return_value = get_mock_response('anger')
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Case 3: Disgust
        mock_post.return_value = get_mock_response('disgust')
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Case 4: Sadness
        mock_post.return_value = get_mock_response('sadness')
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Case 5: Fear
        mock_post.return_value = get_mock_response('fear')
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
