# -*- coding: utf-8 -*-
"""
SAM for Semantic Segmentation Setup

Created by Florent Poux, (c) 2023 Licence MIT
To reuse in your project, please cite the most appropriate article accessible on my Google Scholar page

Have fun with this script!
"""

#%% 1. Loading Libraries
import numpy as np
import time

import torch
import cv2
import matplotlib.pyplot as plt

from segment_anything import sam_model_registry
from segment_anything import SamAutomaticMaskGenerator

#%% 2. Testing the Pytorch / CUDA setup

print('pytorch version: ', torch.__version__)
print('Cuda available :', torch.cuda.is_available())
print('Device number :', torch.cuda.device_count())
print(torch.cuda.get_device_name(0))

#%% 3. Datapath
IMAGE_PATH = 

#%% 4. SAM Variable checks

#Model to get from: https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
CHECKPOINT_PATH =  
MODEL_TYPE = 
DEVICE = 

#%% 5. SAM Setup

sam = sam_model_registry[](checkpoint=)
sam.to(device=)

mask_generator = 

#%% 6. Loading and preparing the image

image_bgr = 
image_rgb = 

#%% 7. Runing SAM on the image

t0 = time.time()
result = 
t1 = time.time()

print(f"Semantic Segmentation with SAM in {t1-t0} seconds")

#%% 8. Masking, Plotting and Exporting the 360 panorama

def sam_masks(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)
    # polygons = []
    # color = []
    c_mask=[]
    for ann in sorted_anns:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for i in range(3):
            img[:,:,i] = color_mask[i]
        ax.imshow(np.dstack((img, m*0.8)))
        c_mask.append(img)
    return c_mask

fig = plt.figure(figsize=(np.shape(image_rgb)[1]/72, np.shape(image_rgb)[0]/72))
fig.add_axes([0,0,1,1])

plt.imshow(image_rgb)
color_mask = sam_masks(result)
plt.axis('off')
plt.savefig(IMAGE_PATH.split('.jpg')[0]+"_segmented.jpg")