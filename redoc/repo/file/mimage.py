import os
import cv2

from redoc.core.entity import mimage

class image_meta_file_adapter(mimage.mimage_repository):
  def __init__(self):
    pass

  def load(self, src: str) -> mimage.image_meta:
    if not os.path.isfile(src):
      raise Exception(f'File not found in "{src}"')

    img = cv2.imread(src)
    img_meta = mimage.image_meta(img)

    if not os.path.isfile(f'{src}.meta'):
      # TODO load metadata
      pass

    return img_meta

  def save(self, src: str, img: mimage.image_meta) -> bool:
    success = True
    # TODO check validity
    # TODO write metadata

    c = cv2.imwrite(src, img.data)
    if not c:
      return False

    return success
