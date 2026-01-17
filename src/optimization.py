import numpy as np
from skimage import color

def search_best_thresholds(hsv_images, masks, hue_ranges, sats, vals):
    best_iou, best_params = -1, None

    for hmin, hmax in hue_ranges:
        for s in sats:
            for v in vals:
                scores = []
                for hsv, gt in zip(hsv_images, masks):
                    H,S,V = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]
                    mask = (H>hmin)&(H<hmax)&(S>s)&(V>v)
                    inter = (mask & gt).sum()
                    union = (mask | gt).sum()
                    scores.append(inter/union if union else 0)
                mean_iou = np.mean(scores)
                if mean_iou > best_iou:
                    best_iou, best_params = mean_iou, (hmin,hmax,s,v)

    return best_params, best_iou
