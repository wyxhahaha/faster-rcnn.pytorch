# --------------------------------------------------------
# Fast R-CNN
# 
# Licensed under The MIT License [see LICENSE for details]
# Written by Howie Chen & 2018.3
# --------------------------------------------------------

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datasets.imdb import imdb
import datasets.ds_utils as ds_utils
from model.utils.config import cfg
import os.path as osp
import sys
import os
import numpy as np
import scipy.sparse
import scipy.io as sio
import pickle
import json
import uuid

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


DATA_DIR = "C:/myFile/faster-rcnn.pytorch/data"
class ICPR(imdb):
  """docstring for ICPR"""
  def __init__(self, image_set):
    imdb.__init__(self, image_set)
    self._image_set = image_set
    self._data_path = osp.join(cfg.DATA_DIR, image_set, 'icpr_9000', 'txt_9000')
    self._image_path = osp.join(cfg.DATA_DIR, image_set, 'icpr_9000', 'image_9000')
    self._file_list = self._load_file_names()
    ####  No need care about classes for text detection  
    
    self._classes = ['text']


  def image_path_at(self, i):
    raise NotImplementedError

  def image_id_at(self, i):
    raise NotImplementedError

  def default_roidb(self):
    raise NotImplementedError
  def image_path_from_index(self, index):
    """
    Construct an image path from the image's "index" identifier.
    """
    assert self._file_list != None
    image_path = osp.join(self._image_path, self._file_list[index])
    return image_path

  def _load_image_set_index(self):
    """
    Load the indexes listed in this dataset's image set file.
    """
    # Example path to image set file:
    # self._data_path + /ImageSets/val.txt 
    pass
  def _load_file_names(self):
    """
    Get all the file names for indexing
    """
    directory = self._data_path
    self.file_list = os.listdir(dir_name)
    self.file_list = [item[:-4] for item in file_list]
    return file_list

  def gt_roidb(self):
    """
    Return the database of ground-truth regions of interest.
    This function loads/saves from/to a cache file to speed up future calls.
    """
    pass
  def _load_icpr_annotation(self, index):
    """
    Load image and bounding boxes info from txt files of imagenet.
    """
    pass
  def evaluate_detections(self, all_boxes, output_dir=None):
    """
    all_boxes is a list of length number-of-classes.
    Each list element is a list of length number-of-images.
    Each of those list elements is either an empty list []
    or a numpy array of detection.

    all_boxes[class][image] = [] or np.array of shape #dets x 5
    """
    raise NotImplementedError

                       