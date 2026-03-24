import numpy as np


def compute_road_length(centerline, pixel_size_m=1):

    centerline = centerline.astype(bool)

    length = 0.0

    rows, cols = centerline.shape

    for i in range(rows):
        for j in range(cols):

            if not centerline[i, j]:
                continue

            # sprawdzamy sąsiadów (prawo i dół żeby nie liczyć 2x)
            for di, dj in [(0, 1), (1, 0), (1, 1), (1, -1)]:

                ni = i + di
                nj = j + dj

                if 0 <= ni < rows and 0 <= nj < cols:
                    if centerline[ni, nj]:

                        # diagonal = sqrt(2), reszta = 1
                        if di != 0 and dj != 0:
                            length += np.sqrt(2)
                        else:
                            length += 1

    length_pixels = length
    length_meters = length * pixel_size_m

    return length_pixels, length_meters