# Emotion Detection Project

This is the final project for the web development course. It consists of a web application built with Flask that identifies the emotions present in a text using the IBM Watson NLP library.

## Project Details

The application takes an input string and returns a dictionary with the confidence scores for the following emotions:

- anger
- disgust
- fear
- joy
- sadness

It also identifies the dominant emotion and displays it to the user through a web interface.

## Files Structure

- `EmotionDetection/`: Directory containing the `emotion_detection.py` module responsible for making the API calls to Watson.
- `server.py`: The main Flask server script that handles routing and error management.
- `test_emotion_detection.py`: A python script containing unit tests to verify the accuracy of the Watson NLP model responses.
- `templates/` and `static/`: Folders containing the frontend files (HTML and Javascript).

## Setup Instructions

1. Clone this repository.
2. Ensure you have Python installed.
3. Install the dependencies by running:
   `pip install flask requests`
4. Start the server:
   `python3 server.py`
5. Go to `http://localhost:5000` in your web browser.
