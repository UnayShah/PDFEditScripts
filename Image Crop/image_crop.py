import cv2
import os
import numpy as np
from PIL import Image

def crop(img):
    image = np.copy(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.blur(image, (10, 10))
    image = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    y1 = -1
    y2 = -1
    for i in range(len(image)):
        if 0 in image[i]:
            if y1 == -1:
                y1 = i
            y2 = i
    x1 = -1
    x2 = -1
    transposed = np.transpose(image)
    for i in range(len(transposed)):
        if 0 in transposed[i]:
            if x1 == -1:
                x1 = i
            x2 = i
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img[0:y2, 0:x2]


if __name__ == '__main__':
    input_directory = input('Enter image directory: ')
    output_directory = input('Enter output directory: ')
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    if os.path.isdir(input_directory):
        for file in os.listdir(input_directory):
            if os.path.isfile(input_directory + '\\' + file):
                # try:
                    Image.fromarray(
                        crop(cv2.imread(input_directory + '\\' + file))).save(output_directory+"\\"+file)
                # except:
                #     print('cant', file)
