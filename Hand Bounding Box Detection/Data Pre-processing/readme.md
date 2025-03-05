# Convert .mat Annotations to YOLO and Faster-RCNN Formats

## **Usage Instructions**
Follow the steps below to convert `.mat` annotation files into the required formats for YOLO and Faster-RCNN.

## **Step 1: Navigate to the Dataset Directory**
In your Python environment, set the working directory to the dataset folder:

```python
import os
os.chdir('/content/drive/MyDrive/Colab Notebooks/BDRP/hand_dataset/')
```
Use one of the following commands to execute the conversion script:

## **Step 2:Convert to YOLO format:

```
!python converter_to_YOLO.py
```

Convert to Faster-RCNN format:

```
!python converter_to_FasterRCNN.py
```

This script will process .mat annotation files and generate the corresponding annotation files compatible with YOLO and Faster-RCNN.


Output

YOLO-formatted annotation files will be saved in the dataset directory.

Faster-RCNN annotation files will be structured accordingly for use with Faster-RCNN models.

Ensure that the dataset directory contains the .mat files before running the script.

