import os
import cv2

def image(source: str):
    '''Load image from local file

    Parameters
    ----------------
    source : str, required
        Location of the image file.

    Returns
    ----------------
    binary
        Image file loaded by cv2.
    '''
    if not os.path.isfile(source):
        raise Exception(f'File not found in "{source}"')

    return cv2.imread(source)

def pdf(source: str):
    pass
