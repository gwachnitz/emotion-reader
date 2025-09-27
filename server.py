"""Run the Flask app that exposes an emotion analysis endpoint on localhost:5000."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the provided text and return emotion scores and dominant label."""
    # Retrieve the text to analyze from the query string
    text_to_analyze = request.args.get("textToAnalyze")

    # Early validation: missing/empty text
    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    # Run the detector
    response = emotion_detector(text_to_analyze)

    # If the detector could not produce a dominant emotion, treat as invalid
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    # Build a concise, readable message
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Serve the index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
