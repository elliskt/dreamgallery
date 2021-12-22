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
import io
import base64
# --- local
import stylize

# --- warning
import warnings
warnings.filterwarnings('ignore')


# --- flask server ----
server = flask.Flask(__name__)
CORS(server, supports_credetials=True)
# --- stylization
style = stylize.Stylization()


# --- API ---
@server.route("/stylization", methods=['POST'])
def stylization():
    print('Doing stylization now!')
    # --- load image ---
    url = request.form['image_url']
    r = requests.get(url, verify=False)
    print('image url requests:', r)
    arr = np.array(bytearray(r.content), dtype=np.uint8)
    print(arr)
    im = cv2.imdecode(arr, -1)
    print(im.shape)
    if im.shape[0] > 1980 or im.shape[1] > 1980:
        im = imutils.resize(im, 1980)
    print(im.shape)
    # --- load model path ---
    model_path = 'models/test.pth'
    generated_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)
    # rgb = generated_img[..., ::-1].copy()
    # pil_img = Image.fromarray(rgb.astype('uint8'))
    # buf = io.BytesIO()
    # pil_img.save(buf, 'JPEG')
    # contents = buf.getvalue()
    _, buffer = cv2.imencode('.jpg', generated_img)
    base64_im = base64.b64encode(buffer)
    print(base64_im[:100])
    # print(contents[:100])
    # return flask.Response(contents, mimetype='image/jpeg')
    return '<p>{}</p>'.format(base64_im)

@server.route("/stylizationtest")
def stylizationtest():
    print('Doing stylization now!')
    # --- load image ---
    # url = 'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=air&step_word=&hs=0&pn=18&spn=0&di=36740&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=3244956887%2C994088757&os=4114866371%2C3673146577&simid=3244956887%2C994088757&adpicid=0&lpn=0&ln=1860&fr=&fmq=1640159068929_R&fm=index&ic=0&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fwww.viigee.net%2Fdatabase%2Fmagazine%2Ffootwear%2Fcommon%2Fupfiles%2F2018%2F02%2F03%2F154800r2q.jpg%26refer%3Dhttp%3A%2F%2Fwww.viigee.net%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1642751097%26t%3Dd84fdc183715388347c3dc7c6dff9433&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bett2jj_z%26e3BgjpAzdH3FoooAzdH3F4w2wztgjAzdH3Fu55pojw6AzdH3F%3Fpyrj%3D1jpwts%26t1%3D8m8b8&gsm=13&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined'
    # r = requests.get(url, stream=True, verify=False)
    # print('image url requests:', r)
    # arr = np.array(bytearray(r.content), dtype=np.uint8)
    # print(arr)
    # im = cv2.imdecode(arr, -1)
    # print(im.shape)
    # if im.shape[0] > 1980 or im.shape[1] > 1980:
    #     im = imutils.resize(im, 1980)
    # print(im.shape)
    # --- load model path ---
    # model_path = 'models/test.pth'
    # generated_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)
    # rgb = generated_img[..., ::-1].copy()
    # pil_img = Image.fromarray(rgb.astype('uint8'))
    # buf = io.BytesIO()
    # pil_img.save(buf, 'JPEG')
    # contents = buf.getvalue()
    generated_img = cv2.imread('1.png')
    _, buffer = cv2.imencode('.jpg', generated_img)
    base64_im = base64.b64encode(buffer)
    print(base64_im[:100])
    # print(contents[:100])
    # return flask.Response(contents, mimetype='image/jpeg')
    return '<p>{}</p>'.format(base64_im)


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

    # model_path = 'models/test.pth'
    # generated_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)
    # print(generated_img)
