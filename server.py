"""Web deployment of the Emotion Detection application using Flask."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """Analyze the textToAnalyze query parameter and return the detected emotions."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid input! Please enter valid text and try again."

    return (
        f"The system detected the dominant emotion as: {response['dominant_emotion']}. "
        f"The emotion scores are anger: {response['anger']}, "
        f"disgust: {response['disgust']}, fear: {response['fear']}, "
        f"joy: {response['joy']}, sadness: {response['sadness']}."
    )


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
