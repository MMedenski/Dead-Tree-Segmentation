# Dead Tree Segmentation using RGB and NRG Imagery

This project implements a pixel-wise segmentation pipeline for detecting standing dead trees in aerial forest imagery.  
The method combines information from RGB images and NRG (Near-Infrared, Red, Green) images and evaluates the results using quantitative metrics.

---

## Project Overview

The main goal of this project is to:
- segment dead trees from aerial imagery,
- fuse RGB-based and NRG-based masks,
- evaluate segmentation quality using IoU and confusion matrix,
---

## Segmentation Pipeline

The segmentation pipeline consists of the following steps:

1. Load RGB and NRG images  
2. Generate independent segmentation masks  
   - RGB-based mask (HSV thresholding)  
   - NRG-based mask (channel normalization and thresholding)  
3. Fuse masks using morphological operations  
4. Compare predicted masks with ground truth masks  
5. Compute evaluation metrics  
   - Intersection over Union (IoU)  
   - Confusion Matrix (normalized, percentage-based)  
6. Threshold optimization using grid search  

---

## Dataset

The project already contains example data in data folder:

- 10 RGB images of forest areas  
- 10 corresponding NRG images  
- 10 ground truth masks (binary masks of dead trees)  

These example images allow the pipeline to be run immediately after installation.

The number of images used in experiments is fully configurable by the user via the configuration file.

---

## Configuration

All global parameters and dataset paths are stored in an external configuration file config.txt which includes:

- dataset paths (RGB, NRG, masks),
- segmentation thresholds,
- number of images used for evaluation.

This approach ensures reproducibility and allows you to modificate parameters for your own usage. 

---

## Evaluation

The segmentation results are evaluated using:

- Intersection over Union (IoU), computed per image and summarized across the dataset.
- Confusion matrix computed pixel-wise using all images and normalized row-wise to percentages.

---

## Project Setup

### Requirements

1. Prepare external libraries for the program using pip :
```
pip install numpy scikit-image matplotlib opencv-python scikit-learn
```
That program includes:
- numpy  
- scikit-image  
- matplotlib  
- opencv-python  
- scikit-learn
  
2. Make sure that main.py and config.txt are located in the same directory.

4. Verify that the dataset folders specified in config.txt exist and contain:

- RGB images,
- NRG images,
- ground truth masks.
  
4. Optionally adjust segmentation thresholds and the number of images to be processed in config.txt.

### Running the program
To run the segmentation, execute:
```
python main.py
```
The program performs the following steps automatically:

- previews the loaded RGB, NRG, and ground truth images,
- generates segmentation masks,
- evaluates results using IoU and confusion matrix,
- displays qualitative and quantitative results.

No manual interaction is required apart from optional keyboard navigation in visualization windows and modification of parameters.

---

Thank you for reading and enjoy using this code.


