"""
Emotion Detection Server

This module runs a Flask application that provides an endpoint for
emotion detection using the Watson NLP library.
"""

import flask
from flask import request
from EmotionDetection.emotion_detection import emotion_detector

app = flask.Flask("Emotion Detection")

@app.route("/emotionDetector")
def emp_detector():
    """
    Handle requests to the /emotionDetector endpoint.
    Retrieves the input text, processes it using the emotion_detector,
    and returns a formatted string with the emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
