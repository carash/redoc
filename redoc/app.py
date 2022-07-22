'''Load and clean up raw document image

Steps:
* Load source image from file/url
* Preview and select 4-points
* Run post-processing
* Preview modified image
* Export modified image
'''

from redoc.config import sizes
from redoc.repo.file.image import image_file_adapter
from redoc.transform.image import image_processor

from PyQt5.QtWidgets import QApplication
import sys

# Hacky fix for PyQt5 and cv2 compatibility
import os
os.environ.update({'QT_QPA_PLATFORM_PLUGIN_PATH': '/home/wibisana/documents/muncher/redoc/env/lib/python3.8/site-packages/PyQt5/Qt5/plugins/xcbglintegrations/libqxcb-glx-integration.so'})

def run():
  # Initialize repopsitories
  image_repo = image_file_adapter()

  # Initialize interactors
  processor = image_processor(image_repo)

  # Load source image
  img = processor.load_image('image.png')

  # Process image
  # img = processor.rotate_ccw(img)
  img = processor.four_point_stretch(img, [
    [0, 0],
    [3000, 0],
    [3000, 4000],
    [0, 4000],
  ], sizes.a4_portrait * 3)

  # Save resulting image
  success = processor.save_image(img, 'image.2.png')
  print(f'Save status: {success}')

if __name__ == '__main__':
  run()
