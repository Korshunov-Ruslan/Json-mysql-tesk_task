import json

from flask import request

from app import app, root

# with open(f'{root}/task3/langs.json') as file:
#    file_content = json.load(file)
#    ALLOWED_LANGUAGES_EXAMPLE = file_content['languages']

ALLOWED_LANGUAGES = json.load(open(f'{root}/task3/langs.json'))['languages']
TARGET_FOLDER = f"{root}/friendship/magic"


@app.route('/', methods=['POST'])
def process_langs_json():
    lang = request.args.get("language")
    content = request.json
    if not lang:
        return f"Specify 'language' parameter", 400
    if lang not in ALLOWED_LANGUAGES:
        return f"Code '{lang}' does not exist", 400

    with open(f'{TARGET_FOLDER}/{lang}.json', 'w') as target_file:
        json.dump(content, target_file)

    return "Success", 200
