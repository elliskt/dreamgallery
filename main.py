# -*- coding: utf-8 -*-
# author: Ellis Lam

import flask
from flask import request
from flask_cors import *
import imutils
import cv2
import numpy
# --- local
import stylize

# --- warning
import warnings

import utils

warnings.filterwarnings('ignore')


# --- flask server ----
server = flask.Flask(__name__)
CORS(server, supports_credetials=True)
# --- stylization
style = stylize.Stylization()


# --- API ---
@server.route("/stylization", methods=['POST'])
def stylization():
    # --- load image ---
    data = request.files['original_image'].read()
    npimg = numpy.fromstring(data, numpy.uint8)
    im = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
    im = imutils.resize(im, 2048)
    # --- load model path ---
    model_path = 'models/test.pth'
    style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8800, debug=True, threaded=True)