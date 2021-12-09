import random
import sys
import cv2
import numpy as np


# generagte a color dictionary. 
based = range(0, 16)
based_palette = [
    "%02x" % l
    for l in based
]

colered = [0] + [0x5f + 40 * n for n in range(0, 5)]
colered_palette = [
    "%02x%02x%02x" % (r, g, b)
    for r in colered
    for g in colered
    for b in colered
]

grayscale = [0x08 + 10 * n for n in range(0, 24)]
grayscale_palette = [
    "%02x%02x%02x" % (a, a, a)
    for a in grayscale
]

color_256 = based_palette + colered_palette + grayscale_palette
color_dict = {color: i for (i, color) in enumerate(color_256)}


def show_color_dict(color_dict):
    index = ''
    for (i, color) in enumerate(color_dict):
        index += "\033[38;5;%sm#" % i
    print(index)


def img_ascii(img, r=1, s=4):
    grays = '@%#*+=-:. '
    grayscale = 10

    width = img.shape[1]
    height = img.shape[0]
    ratio = r * float(width) / height
    scale = width // (s * 80)

    for y in range(0, height, int(scale * ratio)):
        for x in range(0, width, scale):
            idx = img[y][x] * grayscale // 255
            if idx == grayscale:
                idx = grayscale - 1
            sys.stdout.write(grays[idx])
        sys.stdout.write('\n')
        sys.stdout.flush()


def cv2rgb(rgb, color_dict):
    color = ''
    for i in range(3):
        if rgb[i] < 95:
            color += '00'
        elif rgb[i] < 135:
            color += '5f'
        elif rgb[i] < 175:
            color += '87'
        elif rgb[i] < 215:
            color += 'af'
        elif rgb[i] < 225:
            color += 'd7'
        else:
            color += 'ff'
        color_name = ''.join(color)

    color_value = color_dict[color_name]
    return color_value


def cv2img(img, color_dict):
    ascii_img = np.array(img[:, :, 0], dtype=np.string_)
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            ascii_img[h, w] = cv2rgb(img[h, w, :], color_dict)
    return ascii_img


def img_color_ascii(img, r=1, s=4):
    grays = '01'
    grayscale = 2

    width = img.shape[1]
    height = img.shape[0]
    ratio = r * float(width) / height
    scale = width // (s * 80)

    for y in range(0, height, int(scale * ratio)):
        strline = ''
        for x in range(0, width, scale):
            idx = int(img[100][100].mean()) * grayscale // 255
            if idx == grayscale:
                idx = grayscale - 1
            color_id = "\033[38;5;%sm%s" % (img[y][x], grays[random.randint(0, 1)])
            strline += color_id
        print(strline)
        #     sys.stdout.write(grays[idx])
        # sys.stdout.write('\n')
        # sys.stdout.flush()

