from __future__ import annotations

import cv2
import numpy as np

from redoc.utils.npmath import size2matrix

class _meta:
  '''Opration order
  - Rotation
  - Stretch
  - Post processing'''
  _rotation = 0
  _stretch = None
  _size = None
  _opacity = 100

  def __init__(self):
    pass

  # --------------------------------
  # Rotation Configuration
  # --------------------------------
  def rotate_cw(self):
    _rotation -= 1
    if _rotation < 0:
      _rotation += 4

    # TODO rotate stretch

  def rotate_ccw(self):
    _rotation += 1
    if _rotation >= 4:
      _rotation -= 4

    # TODO rotate stretch
  
  def rotate_reset(self):
    # TODO reset stretch

    self._rotation = 0

  # --------------------------------
  # Stretch Configuration
  # --------------------------------
  def stretch(self, source, target, size):
    self._stretch = cv2.getPerspectiveTransform(source, target)
    self._size = (size[0], size[1])

  def stretch_reset(self):
    self._stretch = None
    self._size = None

  # --------------------------------
  # Opacity Configuration
  # --------------------------------
  def opacity(self, opac):
    self._opacity = max(min(opac, 100), 0)

  def opacity_reset(self):
    self._opacity = 100

  # --------------------------------
  # Execute Meta Operations
  # --------------------------------
  def render(self, img):
    img = self._render_rotation(img)
    img = self._render_stretch(img)
    img = self._render_post_process(img)
    return img

  def _render_rotation(self, img: np.array) -> np.array:
    return np.rot90(img, k=self._rotation)
  
  def _render_stretch(self, img: np.array) -> np.array:
    if self.stretch is None:
      return img

    w, h = self._size[0], self._size[1]
    return cv2.warpPerspective(img, self.stretch, (w, h))

  # TODO implement
  def _render_post_process(self, img: np.array) -> np.array:
    # TODO Set opacity
    return img
  
  # --------------------------------
  # Copy
  # --------------------------------
  def copy(self):
    new = _meta()
    new._rotation = new._rotation
    new._stretch = np.copy(new._stretch)
    new._size = new._size
    new._opacity = new._opacity

    return new

class mimage:
  _source = None
  _meta = None
  data = None

  def __init__(self, img):
    self._source = img
    self._meta = _meta()
    self.data = img

  def set_opacity(self, opacity: int) -> mimage:
    self._meta.opacity(opacity)
    self.data = self._meta.render(self._source)
    return self

  def stretch(self, source, target, size) -> mimage:
    self._meta.stretch(source, target, size)
    self.data = self._meta.render(self._source)
    return self

  def rotate_cw(self) -> mimage:
    self._meta.rotate_cw()
    self.data = self._meta.render(self._source)
    return self

  def rotate_ccw(self) -> mimage:
    self._meta.rotate_ccw()
    self.data = self._meta.render(self._source)
    return self

  def copy(self) -> mimage:
    new = mimage(np.copy(self._source))
    new._meta = self._meta.copy()
    return new

class mimage_repository:
  def load(self, src: str) -> mimage: pass
  def save(self, src: str, img: mimage) -> bool: pass
