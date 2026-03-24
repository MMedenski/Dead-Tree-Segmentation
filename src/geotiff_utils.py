import rasterio


def get_pixel_size_meters(tiff_path):

    with rasterio.open(tiff_path) as dataset:

        transform = dataset.transform

        pixel_width = transform.a
        pixel_height = -transform.e

        pixel_size = (pixel_width + pixel_height) / 2

    return pixel_size