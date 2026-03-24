import numpy as np
import tensorflow as tf
import cv2

MODEL_PATH = "models/road_segmentation.h5"

model = tf.keras.models.load_model(MODEL_PATH, compile=False)


def extract_road_mask_ai(image):

    original_shape = image.shape[:2]

    img = cv2.resize(image, (256, 256))

    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)

    pred = pred[0, :, :, 0]

    print("pred min:", pred.min())
    print("pred max:", pred.max())
    threshold = pred.max() * 0.5
    mask = pred > threshold

    mask = cv2.resize(mask.astype(np.uint8), (original_shape[1], original_shape[0]))
    

    return mask.astype(np.uint8)