from flask import Flask, request
from flask import render_template
# import the locally developed module
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''web app route for emotion detection with blank input handling'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Handle blank/invalid input returned as None by the error handling function
    if response['dominant_emotion'] is None:
        return "Invalid input! Please enter valid text and try again."

    anger   = response['anger']
    disgust = response['disgust']
    fear    = response['fear']
    joy     = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"The system detected the dominant emotion as: {dominant_emotion}. "
        f"anger: {anger}, disgust: {disgust}, fear: {fear}, "
        f"joy: {joy}, sadness: {sadness}."
    )

@app.route("/")
def render_index_page():
    '''render the home page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
