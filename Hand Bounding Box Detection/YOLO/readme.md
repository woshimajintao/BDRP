
# Hand Detection with YOLO V8

This code implements a **hand detection model** using **YOLO V8** . The model is trained on a dataset of hand images with labeled bounding boxes and evaluated using **precision, recall, and average precision (AP)**.

## How to Run

### 1. Install Dependencies
You can install them using:

```bash
pip install pandas matplotlib opencv-python Pillow pyyaml
```

### Prepare Dataset:

Place training images in:

```bash
/kaggle/input/hand-dataset/hand_datasets/training_dataset/training_data/Images
```

Place labels in:
```bash
/kaggle/input/hand-dataset/hand_datasets/training_dataset/training_data/Annotation
```
### Run Training Script:
```bash
python main.py
```

### Output:

Trained model saved at:
```bash
D:/Code_pytorch/Jintao/hand detection/output/YOLO_best_model.pth
```

Loss curve plotted in the output directory.

Evaluation metrics (Precision, Recall, AP) displayed.

Predictions (Red) vs Ground Truth (Green) visualized.


