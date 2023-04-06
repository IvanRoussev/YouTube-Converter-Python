from flask import Flask, render_template, request
from Convert.convertmp3 import downloadMp3
from Convert.convertmp4 import downloadMp4

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/audio')
def audio():
    return render_template('audio.html')


@app.route('/audio_download', methods=['POST'])
def convert_audio():
    input_url = request.form['audio_input']
    converted_file = downloadMp3(input_url)
    return converted_file, 200


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/video_download', methods=['POST'])
def convert_video():
    input_url = request.form['video_input']
    converted_file = downloadMp4(input_url)
    return converted_file, 200


if __name__ == '__main__':
    app.run(port=5000)