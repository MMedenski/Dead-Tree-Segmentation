from pathlib import Path
import numpy as np
from skimage import io


def load_image(image_name="StandardResolution.tiff", base_path=None):

    project_root = Path(base_path) if base_path else Path(__file__).resolve().parent.parent
    image_path = project_root / "images" / image_name

    if not image_path.exists():
        raise FileNotFoundError(f"Can not find image {image_path}")

    image = io.imread(image_path)

    if image.ndim == 2:
        image = np.stack([image] * 3, axis=-1)

    if image.ndim == 3 and image.shape[2] > 3:
        image = image[:, :, :3]

    return image.astype(np.uint8)