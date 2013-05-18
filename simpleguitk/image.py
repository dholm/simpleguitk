import urllib

from PIL import Image as PilImage
from PIL import ImageTk


class Image(object):
    def __init__(self, url):
        image = urllib.urlretrieve(url)[0]
        self._image = PilImage.open(image)
        self._image = self._image.convert('RGBA')
        self._versions = {}

    def get_width(self):
        return self._image.size[0]

    def get_height(self):
        return self._image.size[1]

    def _get_tkimage(self, center, wh_src, wh_dst, rot):
        version = ','.join([str(center), str(wh_src), str(wh_dst), str(rot)])
        if version not in self._versions:
            crop = (center[0] - wh_src[0] / 2, center[1] - wh_src[1] / 2,
                    center[0] + wh_src[0] / 2, center[1] + wh_src[1] / 2)
            image = self._image.crop(crop)
            image = image.resize(wh_dst, resample=PilImage.BILINEAR)
            image = image.rotate(-rot, resample=PilImage.BICUBIC, expand=1)
            self._versions[version] = ImageTk.PhotoImage(image)
        return self._versions[version]


def load_image(URL):
    return Image(URL)


def get_width(image):
    return image.get_width()


def get_height(image):
    return image.get_height()
