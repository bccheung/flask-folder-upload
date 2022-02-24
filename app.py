from flask import Flask, render_template, request, jsonify
from pathlib import Path
import shutil
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = Path(__file__).parent / 'uploads'
if UPLOAD_FOLDER.exists():
    shutil.rmtree(UPLOAD_FOLDER)
UPLOAD_FOLDER.mkdir()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('folder')
    for f in files:
        # Sanitize filename (could also implement checking for specific file names)
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] / filename)

    return jsonify({'response': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
