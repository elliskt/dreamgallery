# -*- coding: utf-8 -*-
# author: Ellis Lam
import base64
import flask
import numpy as np
import requests
from flask import request
from flask_cors import *
import imutils
import cv2
from matplotlib import cm
from PIL import Image
import numpy
from io import StringIO
import sys
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
    url = request.form['image_url']
    r = requests.get(url, stream=True, verify=True)
    arr = np.array(bytearray(r.content), dtype=np.uint8)
    im = cv2.imdecode(arr, -1)
    im = imutils.resize(im, 1980)
    # --- load model path ---
    model_path = 'models/test.pth'
    generated_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)
    rgb = generated_img[..., ::-1].copy()
    pil_img = Image.fromarray(rgb.astype('uint8'))
    contents = pil_img.getvalue()
    print(contents[:100])
    return flask.Response(contents, mimetype='image/jpeg')


@server.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == '__main__':
    # model_path = 'models/test.pth'
    # im = utils.load_image('2.jpg')
    # new_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)
    # utils.saveimg(new_img, 'test.jpg')
    # rgb = new_img[..., ::-1].copy()
    # img = Image.fromarray(rgb.astype('uint8'))
    # img.show()
    # a = StringIO()
    # import io
    #
    # with io.BytesIO() as output:
    #     img.save(output, format="JPEG")
    #     contents = output.getvalue()
    #     print(contents[:100])
    # else:
    server.run(host='0.0.0.0', port=8800, debug=True, threaded=True)

    # url = 'https://www.tingmuseum.art/api/ting_museum_database/museum_banner/61bc5d7a75f01256c397a802.jpg'
    # r = requests.get(url, stream=True, verify=True)
    # arr = np.array(bytearray(r.content), dtype=np.uint8)
    # im = cv2.imdecode(arr, -1)
    #
    # cv2.imshow('', im)
    # cv2.waitKey()
    #
    # model_path = 'models/test.pth'
    # generated_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)
    # utils.show(generated_img)
