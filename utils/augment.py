import imutils
import numpy as np
import cv2

def random_augment(img):
    idx = np.random.choice(4)
    
    if idx == 0:
        return random_rotate(img)
    elif idx == 1:
        return lr_flip(img)
    elif idx == 2:
        return ud_flip(img)
    else:
        return translate(img)

def random_rotate(img, range=np.arange(60)):
    return imutils.rotate(img, np.random.choice(range))

def lr_flip(img):
    return cv2.flip(img, 0)

def ud_flip(img):
    return cv2.flip(img, 1)
    
def translate(img, tx=0.2, ty=0.2):
    a, b = img.shape[:2]
    tx = np.random.choice(np.arange(-int(0.2*a), int(0.2*a)))
    ty = np.random.choice(np.arange(-int(0.2*b), int(0.2*b)))
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    
    return cv2.warpAffine(img, translation_matrix, (b, a))