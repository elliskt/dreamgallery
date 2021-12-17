# -*- coding: utf-8 -*-
# author: Ellis Lam

import flask
from flask import request
from flask_cors import *
import imutils
import cv2
from matplotlib import cm
from PIL import Image
import numpy
from io import StringIO
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
    new_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)


@server.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == '__main__':
    model_path = 'models/test.pth'
    im = utils.load_image('1.png')
    new_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)
    utils.show(new_img)
    new_im = Image.fromarray(numpy.uint8(new_img)).convert('RGB')
    new_im.show()
    a = StringIO()
    new_im.save(a, 'png')
    a.seek(0)
    print(a)
    print(type(new_img))
    print(new_img)
    # server.run(host='0.0.0.0', port=8800, debug=True, threaded=True)