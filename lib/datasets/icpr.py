# --------------------------------------------------------
# Fast R-CNN
# 
# Licensed under The MIT License [see LICENSE for details]
# Written by Howie Chen
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

class ICPR(object):
  """docstring for ICPR"""
  def __init__(self, image_set):
    super(ICPR, self).__init__()
    self.arg = arg
    