import io
import requests
from PIL import Image
from torchvision import models, transforms
from torch.autograd import Variable
from torch.nn import functional as F
import numpy as np
import cv2
import os

LABELS_URL = 'https://s3.amazonaws.com/outcome-blog/imagenet/labels.json'

# download the imagenet category list
classes = {int(key):value for (key, value)
          in requests.get(LABELS_URL).json().items()}
# save
#dict_name = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
f = open('classes.txt', 'w')
f.write(str(classes))
f.close()

# 读取
f = open('classes.txt', 'r')
a = f.read()
dict_name = eval(a)
f.close()

