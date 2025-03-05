import os
import json
import scipy.io as sio
from PIL import Image

# 📌 Dataset Paths
dataset_paths = {
    "train": "/content/drive/MyDrive/Colab Notebooks/BDRP/hand_dataset/training_dataset/training_data",
    "validation": "/content/drive/MyDrive/Colab Notebooks/BDRP/hand_dataset/validation_dataset/validation_data",
    "test": "/content/drive/MyDrive/Colab Notebooks/BDRP/hand_dataset/test_dataset/test_data"
}

# 📌 COCO JSON Save Paths
coco_json_paths = {
    "train": "/content/drive/MyDrive/Colab Notebooks/BDRP/hand_dataset/train_coco.json",
    "validation": "/content/drive/MyDrive/Colab Notebooks/BDRP/hand_dataset/validation_coco.json",
    "test": "/content/drive/MyDrive/Colab Notebooks/BDRP/hand_dataset/test_coco.json"
}

# 📌 Category Definition (COCO Format)
categories = [{"id": 1, "name": "hand"}]

def convert_mat_to_coco(dataset_type):
    img_folder = os.path.join(dataset_paths[dataset_type], "images")
    mat_folder = os.path.join(dataset_paths[dataset_type], "annotations")

    # Initialize COCO Data Structure
    coco_data = {"images": [], "annotations": [], "categories": categories}

    annotation_id = 1  # Incremental annotation ID
    image_id = 1       # Incremental image ID

    # Iterate through MAT files
    for mat_file in os.listdir(mat_folder):
        if not mat_file.endswith(".mat"):
            continue

        image_file = mat_file.replace(".mat", ".jpg")
        image_path = os.path.join(img_folder, image_file)
        mat_path = os.path.join(mat_folder, mat_file)

        # Ensure the image exists
        if not os.path.exists(image_path):
            continue

        # Read image dimensions
        with Image.open(image_path) as img:
            img_width, img_height = img.size

        # Load MAT file
        mat_data = sio.loadmat(mat_path)
        boxes = mat_data["boxes"]

        # Add image information
        coco_data["images"].append({
            "id": image_id,
            "file_name": image_file,
            "width": img_width,
            "height": img_height
        })

        # Parse all bounding boxes
        for box in boxes.T:
            a = box[0][0][0][0]
            b = box[0][0][0][1]
            c = box[0][0][0][2]
            d = box[0][0][0][3]

            # Get bounding box coordinates
            x_coords = [a[0][1], b[0][1], c[0][1], d[0][1]]
            y_coords = [a[0][0], b[0][0], c[0][0], d[0][0]]

            xmin, ymin = min(x_coords), min(y_coords)
            xmax, ymax = max(x_coords), max(y_coords)
            width = xmax - xmin
            height = ymax - ymin
            area = width * height  # Compute area

            # Generate annotation
            coco_data["annotations"].append({
                "id": annotation_id,
                "image_id": image_id,
                "category_id": 1,  # Category ID (hand)
                "bbox": [xmin, ymin, width, height],  # COCO format bbox
                "area": area,
                "iscrowd": 0
            })
            
            annotation_id += 1

        image_id += 1  # Increment image ID

    # Save COCO JSON
    with open(coco_json_paths[dataset_type], "w") as json_file:
        json.dump(coco_data, json_file, indent=4)

    print(f"✅ {dataset_type} dataset conversion completed, COCO JSON saved to: {coco_json_paths[dataset_type]}")


# 📌 Run Conversion
convert_mat_to_coco("train")
convert_mat_to_coco("validation")
convert_mat_to_coco("test")

print("🎯 All dataset conversions completed!")
