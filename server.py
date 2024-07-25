'''server.py '''
from flask import Flask, render_template, request
# Import the Maths package here
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def emotion_detection_route():
    '''invoke emotion detection'''
    text_to_analyze = request.args.get('textToAnalyze')
    # Write your code here
    results = emotion_detector(text_to_analyze)
    if results['dominant_emotion'] is None:
        str_results = "Invalid text! Please try again!"
    else:
        str_results = \
        f"For the given statement, the system response is 'anger': {results['anger']}, " + \
        f"'disgust': {results['disgust']}, 'fear': {results['fear']}, " + \
        f"'joy': {results['joy']}, " + f"'sadness': {results['sadness']}. " + \
        f"The dominat emotion is {results['dominant_emotion']}."
    return str_results
@app.route("/")
def home_index_page():
    ''' manage home page ''' 
    # Write your code here
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="localhost", port=5000)
