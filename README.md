# SAM for 3D Instance Segmentation

This script utilizes SAM (Segment Anything Model) for 3D instance segmentation, processing 3D point clouds, and generating spherical images. The main features include:

## Features

- **Library Loading and Path Configuration:** Import necessary libraries and set input/output paths.
- **SAM Model Setup:** Configure the SAM model with a specified checkpoint and device (CPU/GPU).
- **Point Cloud Processing:** Load and process point clouds using Laspy, extracting coordinates and colors.
- **Spherical Image Generation:** Create spherical images from point clouds by converting 3D coordinates to spherical coordinates.
- **Unsupervised Segmentation:** Apply SAM for unsupervised segmentation of the spherical images.
- **Visualization and Export:** Plot and save the segmented spherical images, and export modified point clouds with color information.
- **Back Projection:** Color point clouds based on spherical image segmentation, with options for single, multiple, or filtered points.

###  Libraries

```python
import os
import numpy as np
import time

import torch
import cv2
import matplotlib.pyplot as plt
import laspy

from segment_anything import sam_model_registry
from segment_anything import SamAutomaticMaskGenerator
