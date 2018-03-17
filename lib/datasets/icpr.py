# --------------------------------------------------------
# Fast R-CNN
# 
# Licensed under The MIT License [see LICENSE for details]
# Written by Howie Chen & 2018.3
# --------------------------------------------------------

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .datasets.imdb import imdb
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


class icpr(imdb):
  """this is for the icpr detection commpetion"""
  def __init__(self, image_set, data_path=None):
    imdb.__init__(image_set)
    self._data_path = self._get_default_path() if data_path is None \
                      else data_path
    self._classes = ('__background__', 'text')
    self.__class_to_bind = dict(zip(self.classes, xrange(self.num_classes)))
    self._image_ext = '.jpg'
    self._image_index = self._load_image_set_index()
    
    self._roidb_handler = self.ge_roidb
    self._salt = None
    self._comp_id = ''


    #check if path exist


  def _get_default_path(self):
    """
    Return the default path where icpr is expected to be installed.
    """
    return os.path.join(cfg.DATA_DIR, 'icpr')
  def image_path_at(self, i):
    """
    Return the absolute path to i_th image 
    """
    return self.image_path_from_index(self._image_index[i])
  
  def image_path_from_index(self, index):
    
    image_dir_path = os.path.join(self._data_path, 'Images')
    image_path = osp.join(image_dir_path, index+self._image_ext)
    
    assert os.path.exists(image_path), \
      'Path does not exist: {}'.format(image_path)
    return image_path

  def _load_image_set_index(self):

    # example image set file:
    # self._data_path + ImageSets/train.txt
    image_set_file = osp.join(self._data_path, 'ImageSets', 'train.txt')
    
    assert os.path.exists(image_set_file), \
            'Path does not exists: {}'.format(image_set_file)
    with open(image_set_file) as f:
      image_index = [x.strip() for x in f.readlines()]
    return image_index

  def gt_roidb(self):
    """
    Return the database of ground-truth regions of interest.

    This function loads/saves from/to a cache file to speed up future calls.
    """
    cache_file = os.path.join(self.cache_path, self.name + '_gt_roidb.pkl')
    if os.path.exists(cache_file):
      with open(cache_file, 'rb') as fid:
        roidb = pickle.load(fid)
      print('{} gt roidb loaded from {}'.format(self.name, cache_file))
      return roidb

    gt_roidb = [self._load_icpr_annotation(index)[0]
          for index in self.image_index]
    with open(cache_file, 'wb') as fid:
      pickle.dump(gt_roidb, fid, pickle.HIGHEST_PROTOCOL)
    print('wrote gt roidb to {}'.format(cache_file))

    return gt_roidb

  def _load_icpr_annotation(self, index):
    annotation_dir = os.path.join(self._data_path, 'Annotations')
    annotation_file = os.path.join(annotation_dir, index+'.txt')
    annotations = []
    letters = []
    with open(annotation_file,encoding="utf8") as f:
        for line in f:
            data = line.split(',')
            annotations.append(data[:-1])
            letters.append(data[-1])
    annotations = [float(x) for x in annotations]
    return annotations, letters

  def selective_search_roidb(self):

    raise NameError("unimplemented")

if __name__ == '__main__':
  
  d = icpr('icpr')

  from IPython import emded;
  emded()