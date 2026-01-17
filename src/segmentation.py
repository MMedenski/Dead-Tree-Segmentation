import numpy as np
from skimage import color, morphology

def generate_segment_mask_rgb(rgb_image, hue_min, hue_max, sat_thr, val_thr):
    hsv = color.rgb2hsv(rgb_image.astype(np.float32) / 255.0)
    H, S, V = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]
    return ((H > hue_min) & (H < hue_max) & (S > sat_thr) & (V > val_thr)).astype(np.uint8)

def generate_segment_mask_nrg(nrg_image):
    nrg = nrg_image.astype(np.float32)
    nir, red, green = nrg[:,:,0], nrg[:,:,1], nrg[:,:,2]

    nir = (nir - nir.min()) / (nir.max() - nir.min() + 1e-6)
    red = (red - red.min()) / (red.max() - red.min() + 1e-6)
    green = (green - green.min()) / (green.max() - green.min() + 1e-6)

    return ((nir < 0.4) & (red > 0.55) & (green > 0.55)).astype(np.uint8)

def fuse_masks(mask_rgb, mask_nrg):
    combined = mask_rgb & morphology.binary_dilation(mask_nrg, morphology.disk(2))
    combined = morphology.binary_closing(combined, morphology.disk(4))
    return combined.astype(np.uint8)
