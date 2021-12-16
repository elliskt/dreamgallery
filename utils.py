from torchvision import transforms
import cv2
import imutils

def load_image(path, imsize = None):
    # Images loaded as BGR
    img = cv2.imread(path)

    print('[INFO] img original size: {}'.format(img.shape))
    # cv2.imshow('.', img)
    # cv2.waitKey()
    if imsize == None:
        return img
    else:
        img = imutils.resize(img, width=imsize)
        return img


def itot(img, max_size=None):
    # Rescale the image
    if (max_size == None):
        itot_t = transforms.Compose([
            # transforms.ToPILImage(),
            transforms.ToTensor(),
            transforms.Lambda(lambda x: x.mul(255))
        ])
    else:
        H, W, C = img.shape
        image_size = tuple([int((float(max_size) / max([H, W])) * x) for x in [H, W]])
        itot_t = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize(image_size),
            transforms.ToTensor(),
            transforms.Lambda(lambda x: x.mul(255))
        ])
    # Convert image to tensor
    tensor = itot_t(img)
    # Add the batch_size dimension
    tensor = tensor.unsqueeze(dim=0)
    return tensor


def ttoi(tensor):
    # Add the means
    # ttoi_t = transforms.Compose([
    #    transforms.Normalize([-103.939, -116.779, -123.68],[1,1,1])])

    # Remove the batch_size dimension
    tensor = tensor.squeeze()
    # img = ttoi_t(tensor)
    img = tensor.cpu().numpy()

    # Transpose from [C, H, W] -> [H, W, C]
    img = img.transpose(1, 2, 0)
    return img