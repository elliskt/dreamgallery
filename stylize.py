import torch
import utils
import transformer
import time


PRESERVE_COLOR = False
CUR_IMG_NAME = None


class Stylization(object):
    def __init__(self):
        self.device = ("cuda" if torch.cuda.is_available() else "cpu")
        print('[INFO] Stylizing device is using....', self.device)

    def stylize(self, CONTENT_IMAGE, MODEL_PATH):
        torch.cuda.empty_cache()
        net = transformer.TransformerNetwork()
        net.load_state_dict(torch.load(MODEL_PATH))
        net = net.to(self.device)

        with torch.no_grad():
            torch.cuda.empty_cache()
            print("[INFO] Stylizing Image...")

            starttime = time.time()
            content_tensor = utils.itot(CONTENT_IMAGE).to(self.device)
            generated_tensor = net(content_tensor)
            generated_image = utils.ttoi(generated_tensor.detach())
            # if PRESERVE_COLOR:
            # generated_image = utils.transfer_color(CONTENT_IMAGE, generated_image)
            # generated_image_pserved_color = cv2tran.color_transfer(source=generated_image, ref=CONTENT_IMAGE)
            print("[INFO] Done. Transfer Time: {}s".format(time.time() - starttime))
            return generated_image


