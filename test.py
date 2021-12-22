import cv2
import requests
import numpy as np
import time
import base64
# --- local
import stylize


# style = stylize.Stylization()


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
    # server.run(host='0.0.0.0', port=8800, debug=True, threaded=True)

    # generated_img = cv2.imread('1.png')
    # _, buffer = cv2.imencode('.jpg', generated_img)
    # base64_im = base64.b64encode(buffer)
    # print(base64_im[:100])

    url = 'https://www.tingmuseum.art/api/ting_museum_database/museum_banner/61bc5d7a75f01256c397a802.jpg'
    # # url = 'https://cdc-material.qq.com/202112201608/5b7e836ed6ffff7b1d1b5a5d0dce84e2/ewesion_hdd_2/4060975/91513296/staff_1024.jpg/preview600'
    start = time.time()
    r = requests.get(url, verify=False)
    print(r)
    print('requests get used for: ', time.time() - start)
    start = time.time()
    arr = np.array(bytearray(r.content), dtype=np.uint8)
    print('np array from bytearray used for: ', time.time() - start)
    #
    # start = time.time()
    # arr1 = np.frombuffer(r.content, dtype=np.int16)
    # print(time.time() - start)
    #
    # start = time.time()
    # im = cv2.imdecode(arr, -1)
    # # print(im)
    # print('cv imdecode used for: ', time.time() - start)
    # # cv2.imshow('', im)
    # # cv2.waitKey()
    #
    # start = time.time()
    # model_path = 'models/test.pth'
    # generated_img = style.stylize(CONTENT_IMAGE=im, MODEL_PATH=model_path)
    # print('stylization used for: ', time.time() - start)