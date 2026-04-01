'''Server of the Flask application which performs an
analysis of a provided text.
'''
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the degree of several emotions
        and the dominant one for the provided text.
    '''

    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    partial_replay = " "
    for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
        degree = response[emotion]
        partial_replay = f"{partial_replay} '{emotion}': {degree}"
        if emotion not in ['joy', 'sadness']:
            partial_replay += ', '
        elif emotion == 'joy':
            partial_replay += ' and '

    dominant_emotion = response['dominant_emotion']
    partial_replay = f"{partial_replay}. The domination emotion is <b>{dominant_emotion}</b>"

    final_replay = f"For the given statement, the system response is {partial_replay}"

    return final_replay

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''

    return render_template("index.html")

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
