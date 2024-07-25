import unittest

from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        #test for joy
        result_1 = emotion_detector("I am glad this happened")
        print(result_1)
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        #test for anger
        result_1 = emotion_detector("I am really mad about this")
        print(result_1)
        self.assertEqual(result_1['dominant_emotion'], 'anger')

        #test for disgust
        result_1 = emotion_detector("I feel disgusted just hearing about this")
        print(result_1)
        self.assertEqual(result_1['dominant_emotion'], 'disgust')
        
        #test for sadness
        result_1 = emotion_detector("I am so sad about this")
        print(result_1)
        self.assertEqual(result_1['dominant_emotion'], 'sadness')

        #test for fear
        result_1 = emotion_detector("I am really afraid that this will happen")
        print(result_1)
        self.assertEqual(result_1['dominant_emotion'], 'fear')

unittest.main()