#! python3
from PIL import Image
import sys
import time

gscale = " .,:;irsXA253hMHGS#9B&@"


def rescale(image, height=30):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_width)/float(old_height)
    width = int(aspect_ratio * height * 2)
    dim = (width, height)
    image = image.convert('L').resize(dim)

    initial_pixels = list(image.getdata())
    new_pixels = [gscale[min(int((pixel_value / 255) * len(gscale)), len(gscale) - 1)] for pixel_value in initial_pixels]
    pixels = ''.join(new_pixels)
    new_image = [pixels[index:index + width] for index in range(0, len(pixels), width)]
    return '\n'.join(new_image)


def runner(path):
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in", path)
        return
    image = rescale(image)

    return image


if __name__ == '__main__':
    frames = []
    print("☯The girls are now preparing. Please wait warmly.☯")
    for i in range(0, 6571):
        path = "./frames/BA" + str(i) + ".jpg"
        frames.append(runner(path))
    i = 0
    while i < len(frames) - 1:
        print('\n' + frames[i], end='')
        i += 1
        time.sleep(0.02800)
