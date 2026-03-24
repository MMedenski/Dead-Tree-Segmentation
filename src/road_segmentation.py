import numpy as np
from skimage.filters import threshold_otsu
from skimage.morphology import closing, opening, disk, remove_small_holes, remove_small_objects
from scipy.ndimage import binary_fill_holes


def extract_road_mask(image):

    red = image[:, :, 0].astype(np.float32)
    green = image[:, :, 1].astype(np.float32)
    blue = image[:, :, 2].astype(np.float32)

    red_t = threshold_otsu(red)
    green_t = threshold_otsu(green)
    blue_t = threshold_otsu(blue)

    channel_spread = np.max(image, axis=2) - np.min(image, axis=2)
    spread_t = threshold_otsu(channel_spread)

    road_mask = (
        (red > red_t)
        & (green > green_t)
        & (blue > blue_t)
        & (channel_spread < spread_t)
    )

    road_mask = closing(road_mask, disk(7))
    road_mask = closing(road_mask, disk(5))
    road_mask = opening(road_mask, disk(2))

    road_mask = remove_small_objects(road_mask, max_size=2000)
    road_mask = remove_small_holes(road_mask, max_size=8000)

    road_mask = binary_fill_holes(road_mask)

    return road_mask.astype(np.uint8)