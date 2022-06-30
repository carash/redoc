import os
import cv2

from redoc.core.entity import image

class image_file_adapter(image.image_repository):
  def __init__(self):
    pass

  def load(self, src: str) -> image.image:
    if not os.path.isfile(src):
        raise Exception(f'File not found in "{src}"')

    img = cv2.imread(src)
    return image.image(img)

  def save(self, src: str, img: image.image) -> bool:
    # TODO check validity
    return cv2.imwrite(src, img.data)
