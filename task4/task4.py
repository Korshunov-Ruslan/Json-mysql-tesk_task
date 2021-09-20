import os

from flask import request

from app import app, root

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'tiff', 'psd'}
ONE_MB = 1024 ** 2
UPLOAD_FOLDER = f'{root}/friendship/magic/photo'


# file.PNG -> file.png
# ....endswith(tuple('.png', '.jpg'....))
def is_image(filename):
    return filename.lower().endswith(tuple(f'.{extension}' for extension in ALLOWED_EXTENSIONS))


def get_file_size(file):
    file.seek(0, os.SEEK_END)
    file_length = file.tell()
    file.seek(0, 0)
    return file_length


@app.route('/photo', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No {file} parameter specified", 400

    file = request.files['file']
    if not is_image(file.filename):
        return f"File has invalid extension. Allowed are: {ALLOWED_EXTENSIONS}", 400

    if get_file_size(file) > ONE_MB:
        return "File size > 1MB", 400
    file.save(os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)))
    return "Uploaded", 200
