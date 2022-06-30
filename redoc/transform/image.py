from redoc.config import sizes
from redoc.core.entity import image
from redoc.utils.npmath import list2matrix, size2matrix

class image_processor:
  _image_repo = None

  def __init__(self, image_repo: image.image_repository):
    self._image_repo = image_repo

  def load_image(self, src: str) -> image.image:
    return self._image_repo.load(src)

  def load_watermark(self, src: str, opacity: int) -> image.image:
    return self._image_repo.load(src).set_opacity(opacity)

  def save_image(self, img: image.image, src: str) -> bool:
    return self._image_repo.save(src, img)

  def four_point_stretch(self, img: image.image, points: list, size: tuple = sizes.a4_portrait) -> image.image:
    '''Stretch an image such that 4 selected points become the new corners

    Parameters
    ----------------
    img : image.image, required
      Source image to be transformed.
    points : list(list(int)), required
      List of 4 pairs, corresponding to x-y coordinates of the corners of the transformed image. Ordered from top-left, going clockwise.
    size : list(int), optional
      Pair of x-y coordinates denoting the transformed image size. Default to A4 size.

    Returns
    ----------------
    image.image
      Transformed image.
    '''
    w, h = size[0], size[1]

    points = list2matrix(points)
    target = size2matrix((w,h))

    return img.four_point_stretch(points, target, (w,h))

  def rotate_cw(self, img: image.image) -> image.image:
    '''Rotate an image clockwise

    Parameters
    ----------------
    img : image.image, required
      Source image to be rotated clockwise.

    Returns
    ----------------
    image.image
      Rotated image.
    '''
    return img.rotate_cw()

  def rotate_ccw(self, img: image.image) -> image.image:
    '''Rotate an image counter clockwise

    Parameters
    ----------------
    img : image.image, required
      Source image to be rotated counter clockwise.

    Returns
    ----------------
    image.image
      Rotated image.
    '''
    return img.rotate_ccw()

  def add_watermark(self, img: image.image, watermark: image.image) -> image.image:
    '''Add a watermark overlay over original image
    '''
    return img
