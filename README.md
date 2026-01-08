# Dead Tree Segmentation using RGB and NRG Imagery

A **research-oriented classical computer vision project** for pixel-wise detection of standing dead trees in aerial forest imagery.

The pipeline combines **RGB imagery** with **NRG (Near-Infrared, Red, Green) data**, supports **YAML-based configuration**, **command-line overrides**, and provides both **qualitative visualization** and **quantitative evaluation** of results.

---

## 🚀 Key Features

- Pixel-wise segmentation of dead trees using handcrafted features
- Independent RGB- and NRG-based masks
- Morphological mask fusion
- Fully configurable via `config.yaml`
- Command-line interface (CLI) with `argparse`
- Quantitative evaluation using IoU and confusion matrix
- Automatic saving of generated segmentation masks
- Reproducible environment via `requirements.txt`

---

## 🧠 Segmentation Pipeline

1. Load RGB and NRG images
2. Generate independent segmentation masks:
   - RGB mask based on HSV thresholding
   - NRG mask based on spectral normalization
3. Fuse masks using morphological operations
4. Compare predicted masks with ground truth
5. Compute evaluation metrics:
   - Intersection over Union (IoU)
   - Confusion Matrix (normalized)
6. Perform threshold optimization via grid search

---

## 🖼️ Segmentation Results – Visual Explanation

This section explains **when and how each mask is created in the pipeline** and how the visual outputs relate to one another. You can insert your own figures in the indicated places.

### 1️⃣ RGB Image (Input)

The original RGB image used as one of the inputs to the segmentation pipeline.

<p align="center">
  <img src="data/img_readme/RGB_ar037_2019_n_06_04_0.png" width="400">
  <br>
  <em>Generated segmentation mask</em>
</p>


---

### 2️⃣ NRG Image (Input)

The corresponding NRG (Near-Infrared, Red, Green) image, providing spectral information useful for vegetation analysis.

<p align="center">
  <img src="data/img_readme/NRG_ar037_2019_n_06_04_0.png" width="400">
  <br>
  <em>Generated segmentation mask</em>
</p>

---

### 3️⃣ Generated Mask (Prediction)

The **generated segmentation mask** is produced during the pipeline after:

- computing the RGB-based mask,
- using NRG-based mask comparing with RGB mask,
- optimalize using morphological operations.

This mask represents the **final prediction** of dead tree locations.

<p align="center">
  <img src="data/img_readme/RGB_ar037_2019_n_06_04_0_mask.png" width="400">
  <br>
  <em>Generated segmentation mask</em>
</p>

---

### 4️⃣ Ground Truth Mask (Main Mask)

The **main mask (ground truth)** is a manually prepared binary mask used for evaluation. It represents the reference annotation against which the generated mask is compared.

<p align="center">
  <img src="data/img_readme/mask_ar037_2019_n_06_04_0" width="400">
  <br>
  <em>Generated segmentation mask</em>
</p>

---

### 5️⃣ Visual Comparison

During visualization, the following elements are displayed side by side:

- RGB image
- NRG image
- Generated (predicted) mask
- Ground truth (main) mask

This allows for qualitative inspection of segmentation accuracy and typical error patterns.

---

---

## 📂 Dataset Structure

The expected dataset layout is:

```
data/
├── RGB_images/    # RGB images (.png)
├── NRG_images/    # NRG images (.png)
└── masks/         # Ground truth binary masks (.png)
```

The number of images used for **preview** and **evaluation** is configurable.

---

## ⚙️ Configuration

All experiment parameters are defined in a YAML configuration file.

### Configuration files

- `temp.config.yaml` – configuration template (tracked in git)
- `config.yaml` – local configuration file (ignored by git)

Create your local configuration by copying the template:

```bash
cp temp.config.yaml config.yaml
```

### Configurable parameters include:

- paths to RGB, NRG and mask images
- output directory
- HSV segmentation thresholds
- number of preview images (`num_images`)
- number of evaluation images (`num_compare`)

> ⚠️ A sanity check prevents running the program if `num_compare > num_images`.

---

## 🖥️ Command-Line Interface (CLI)

All configuration values can be overridden from the command line.

### Show available options

```bash
python main.py --help
```

### Example run

```bash
python main.py \
  --config config.yaml \
  --num-images 5 \
  --num-compare 5 \
  --hue-min 0.75 \
  --hue-max 0.95 \
  --sat-thr 0.25 \
  --val-thr 0.55 \
  --output-dir output/final_run/
```

> Command-line arguments have **higher priority** than values defined in `config.yaml`.

---

## 📊 Evaluation

The pipeline provides both qualitative and quantitative evaluation:

### Quantitative metrics

- Per-image **Intersection over Union (IoU)**
- Global pixel-wise **confusion matrix** (percentage-normalized)

### Qualitative visualization

For each image:

- RGB image
- NRG image
- RGB-based mask
- NRG-based mask
- Fused segmentation mask
- Ground truth mask

---

## 🛠️ Installation & Setup

### 1️⃣ Create virtual environment

```bash
python -m venv .venv
```

### 2️⃣ Activate virtual environment (Windows PowerShell)

```bash
.\.venv\Scripts\Activate.ps1
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

Optional parameters can be supplied via the CLI.

---

## 📁 Project Structure

```
Dead-Tree-Segmentation-main/
│
├── main.py                 # Main pipeline script
├── requirements.txt        # Project dependencies
├── temp.config.yaml        # Configuration template
├── config.yaml             # Local config (gitignored)
├── README.md
├── .gitignore
├── data/
│   ├── RGB_images/
│   ├── NRG_images/
│   └── masks/
└── output/                 # Generated results
```

---

## 🔬 Design Notes

- The project intentionally uses **classical computer vision techniques** rather than deep learning.
- Thresholds are heuristic but fully configurable and optimizable.
- The codebase is designed for clarity, reproducibility, and extensibility.

---

## 📌 Reproducibility

- All dependencies are specified in `requirements.txt`
- Runtime configuration is separated from code
- Local paths are excluded from version control

---

## 🏁 Final Notes

This project is suitable as:

- a research prototype,
- a baseline for further ML or DL-based approaches.

Feel free to extend or adapt the pipeline for your own experiments.

