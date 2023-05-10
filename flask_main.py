import time
from flask import Flask, render_template, flash, redirect, url_for, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
import queue
import split_song
from pathlib import Path

q = queue.Queue()
UPLOAD_FOLDER = 'UPLOADS FOLDER'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'aiff', 'flac', 'm4a', 'ogg'}
key = os.urandom(12).hex()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.update(
    TESTING=True,
    SECRET_KEY=key
)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template('main.html')


@app.route("/splitter", methods=['GET', 'POST'])
def splitter():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No File Part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No File Selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fileopen = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filesave = os.path.dirname(fileopen)
            file_name_no_extension = Path(fileopen).stem
            file_name = Path(fileopen).name
            flash('File added to queue')
            size = q.qsize()
            q.put((filesave, fileopen, file_name_no_extension, file_name))
            time.sleep(30 * size)
            split_song.execute(filesave, fileopen)
            split_song.archive_make(filesave, file_name, file_name_no_extension)
            sending_file = fileopen + ".zip"
            filesave, fileopen, file_name_no_extension, file_name = q.get()
            return send_file(sending_file)
    return render_template('audio_splitter.html', queue_size=q.qsize())


@app.route("/refresh", methods=["POST"])
def refresh():
    return jsonify(queue_size=q.qsize())


@app.route("/tuner")
def tuner():
    return render_template('tuner.html')


@app.route("/about")
def about():
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run()
