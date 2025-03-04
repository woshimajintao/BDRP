# Hand Detection with Faster R-CNN

This code implements a **hand detection model** using **Faster R-CNN** with a **ResNet-50 backbone**. The model is trained on a dataset of hand images with labeled bounding boxes and evaluated using **precision, recall, and average precision (AP)**.

## How to Run

### 1. Install Dependencies
Ensure you have **PyTorch, torchvision, and other required libraries** installed. You can install them using:

```bash
pip install torch torchvision matplotlib numpy
```

### Prepare Dataset:

Place training images in:

```bash
D:/Code_pytorch/Jintao/hand detection/training_dataset/training_data/images/
```

Place labels in:
```bash
D:/Code_pytorch/Jintao/hand detection/labels_fast_rcnn/
```
### Run Training Script:
```bash
python main.py
```

### Output:

Trained model saved at:
```bash
D:/Code_pytorch/Jintao/hand detection/output/faster_rcnn_model.pth
```

Loss curve plotted in the output directory.

Evaluation metrics (Precision, Recall, AP) displayed.

Predictions (Red) vs Ground Truth (Green) visualized.


