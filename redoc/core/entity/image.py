from __future__ import annotations

import cv2
import numpy as np

from redoc.utils.npmath import size2matrix

class image:
  data = None

  def __init__(self, img):
    self.data = img

  # TODO implement
  def set_opacity(self, opacity: int) -> image:
    return self

  def four_point_stretch(self, points, target, size) -> image:
    (w, h) = size[0], size[1]

    tmat = cv2.getPerspectiveTransform(points, target)
    self.data = cv2.warpPerspective(self.data, tmat, (w, h))
    return self

  def rotate_cw(self) -> image:
    self.data = np.rot90(self.data, k=3)
    return self

  def rotate_ccw(self) -> image:
    self.data = np.rot90(self.data, k=1)
    return self

  def copy(self) -> image:
    return image(np.copy(self.data))

class image_repository:
  def load(self, src: str) -> image: pass
  def save(self, src: str, img: image) -> bool: pass
