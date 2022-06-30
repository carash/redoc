import numpy as np

def list2matrix(points):
  return np.array(points, dtype='float32')

def size2matrix(size):
  w = size[0]
  h = size[1]

  return np.array([
    [0,0],
    [w,0],
    [w,h],
    [0,h]], dtype='float32')
