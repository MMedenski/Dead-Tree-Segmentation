import numpy as np
from skimage.morphology import skeletonize
from scipy.ndimage import binary_dilation


def _get_neighbors(y, x, image):
    neighbors = []
    rows, cols = image.shape

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue

            ny, nx = y + dy, x + dx

            if 0 <= ny < rows and 0 <= nx < cols:
                if image[ny, nx]:
                    neighbors.append((ny, nx))

    return neighbors


def _find_endpoints(skeleton):
    endpoints = []
    rows, cols = skeleton.shape

    for y in range(rows):
        for x in range(cols):
            if skeleton[y, x]:
                neighbors = _get_neighbors(y, x, skeleton)
                if len(neighbors) == 1:
                    endpoints.append((y, x))

    return endpoints


def _remove_branch(skeleton, start, max_length=50):
    path = [start]
    visited = set(path)

    current = start

    for _ in range(max_length):
        neighbors = _get_neighbors(current[0], current[1], skeleton)

        neighbors = [n for n in neighbors if n not in visited]

        if not neighbors:
            break

        next_pixel = neighbors[0]
        path.append(next_pixel)
        visited.add(next_pixel)

        current = next_pixel

        if len(_get_neighbors(current[0], current[1], skeleton)) > 2:
            break

    for y, x in path:
        skeleton[y, x] = 0

    return skeleton


def prune_skeleton(skeleton, max_branch_length=50):
    skeleton = skeleton.copy()

    endpoints = _find_endpoints(skeleton)

    for endpoint in endpoints:
        skeleton = _remove_branch(skeleton, endpoint, max_branch_length)

    return skeleton


def extract_road_centerline(road_mask):

    road_mask = binary_dilation(road_mask, iterations=2)
    skeleton = skeletonize(road_mask)

    skeleton = prune_skeleton(skeleton, max_branch_length=50)

    return skeleton.astype("uint8")