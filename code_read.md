[toc]
# 说明
这个代码阅读笔记根据[pytorch](https://github.com/jwyang/faster-rcnn.pytorch)的实现来分析和阅读的。  
这个实现可以支持多种数据集。
# 代码结构
todo

## dataset && dataloader
数据首先是读取成为`imdb`，然后交给`dataloader`处理的。  

`trainval_net.py`文件中相关函数
```python

imdb, roidb, ratio_list, ratio_index = combined_roidb(args.imdb_name)


dataset = roibatchLoader(roidb, ratio_list, ratio_index, args.batch_size, \
                           imdb.num_classes, training=True)
```
在`lib\roidatalayer\roidb.py`找到了`combined_roidb`的实现。

其中
```python 
imdb = get_imdb(imdb_name)
```
`get_imdb(imdb_name)`是`\lib\datasets\factory.py`的函数。
在这里面，定义了不同数据集的结构。当使用自己数据集的时候，需要在这里添加你的数据集的结构。


```python
def get_imdb(name):
  """Get an imdb (image database) by name."""
  if name not in __sets:
    raise KeyError('Unknown dataset: {}'.format(name))
  return __sets[name]()
```
这里的`__sets[name]()`，以`coco_2014_`为例


```python
for year in ['2014']:
  for split in ['train', 'val', 'minival', 'valminusminival', 'trainval']:
    name = 'coco_{}_{}'.format(year, split)
    __sets[name] = (lambda split=split, year=year: coco(split, year))

```
可以看到`__sets[name]()`即`coco(split, year)`, 也就是自己定义的`dataset`类。

其中 `imdb` 是根据微软开源的代码。如果需要对自己的数据集进行处理，需要明白数据的流动方式。下面介绍一些`imdb`的实现，以及主要功能。  
`imdb.py` 在`\lib\datasets\`目录下面。其主要成员以及函数如下

```python
class imdb(object):
    def __init__(self, name, classes=None):
        self._name = name
        self._num_classes = 0
        if not classes:
            self._classes = []
        else:
            self._classes = classes
        self._image_index = []
        self._obj_proposer = 'gt'
        self._roidb = None
        self._roidb_handler = self.default_roidb
        # Use this dict for storing dataset specific config options
        self.config = {}
    def name():
    def num_classes(self):
    def classes(self):
    def image_index(self):
    def roidb_handler(self):
    def roidb_handler(self, val):
    def set_proposal_method(self, method):
    def roidb(self):
    def cache_path(self):
    def num_images(self):
    def image_path_at(self, i):
    def image_id_at(self, i):
    def default_roidb(self):
    def evaluate_detections(self, all_boxes, output_dir=None):
    def _get_widths(self):
    def append_flipped_images(self):
    def evaluate_recall(self, candidate_boxes=None, thresholds=None, area='all', limit=None):
    def create_roidb_from_box_list(self, box_list, gt_roidb):
    def merge_roidbs(a, b):
    def competition_mode(self, on):
```
自己定义的`dataset`类需要继承`imdb`，一定需要自己实现的有

```python
def image_path_at(self, i):
def image_id_at(self, i):
def default_roidb(self):
def evaluate_detections(self, all_boxes, output_dir=None):
```
