#!/usr/bin/env python

from flask import request, url_for, send_from_directory, request
from flask_api import FlaskAPI, status, exceptions
from werkzeug import secure_filename
import os
import subprocess
app = FlaskAPI(__name__)

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath



@app.route("/", methods=['GET', 'POST'])
def notes_list():
    """
    List or create notes.
    """
    if request.method == 'GET':
        
        return "yarak", status.HTTP_201_CREATED
        #note = str(request.data.get('text', ''))
        #idx = max(notes.keys()) + 1
        #notes[idx] = note
        return note_repr(idx), status.HTTP_201_CREATED
    elif request.method == 'POST': 
        img = request.files['image']
        img_name = secure_filename(img.filename)
        create_new_folder("/tmp/openface")
        saved_path = os.path.join("/tmp/openface", img_name)
        app.logger.info("saving {}".format(saved_path))
        img.save(saved_path)
        out = subprocess.check_output("/bin/python2 /root/openface/demos/compare.py /tmp/openface/test2.jpeg /root/openface/target.jpeg")
        return out

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
