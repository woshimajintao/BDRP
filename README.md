# BDRP_Jintao_Ma
## Work Timeline
During the past months.  I firstly practiced on some simulation tools like Mujoco,then I accomplished the critical milestone of reproducing the methodol-
ogy presented in the selected paper AnyTeleop: A General Vision-Based Dexterous Robot
Arm-Hand Teleoperation System[https://yzqin.github.io/anyteleop/],then I focused on a smaller task and finished the hand
bounding box detection task based on the Oxford Hand Dataset[https://www.robots.ox.ac.uk/~vgg/data/hands/]
![image](https://github.com/user-attachments/assets/db6c70cd-ba84-438c-8a64-a67e44e5fa37)


## Paper Reproduction
### System Architecture:

The most important part of AnyTeleop is the Teleoperation Server.So I also drew this architecture as Figure show.

![image](https://github.com/user-attachments/assets/f343959e-95e2-4fdd-b01b-10cfb3ce08e3)


### Key Functions :

• Hand Pose Detection:

– Processes visual data captured by the Camera Driver to estimate the 3D hand
pose of the human operator.

– Uses advanced algorithms to track joint angles, fingertip positions, and overall
hand configuration in real time.

• Multi-Camera Fusion:

– If multiple cameras are used, the server fuses input data to enhance tracking
accuracy and minimize occlusion effects.

– Aligns and calibrates inputs from different viewpoints for a comprehensive un-
derstanding of hand movements.

• Hand Pose Retargeting:

– Translates human hand movements into corresponding robotic hand motions
through kinematic optimization.

– Maps the human hand’s degrees of freedom (DOF) to the robot hand’s spe-
cific kinematics, ensuring compatibility while respecting the robotic hardware’s
constraints.

• Motion Command Generation:

– Generates collision-free and smooth motion trajectories for both the robotic
arm and hand using algorithms such as Riemannian Motion Policies (RMPs).

– Ensures safe and stable teleoperation by dynamically adapting to environmental
constraints.
### Reproduction Results :

https://drive.google.com/file/d/1tnQRBRV70f7sH1B5BF6acbjSkgz5Q01Z/view?usp=sharing
 
https://drive.google.com/file/d/1CXYVzcWUpEsoNcZla_Rn1jxIrapQWOE2/view?usp=sharing
 
https://drive.google.com/file/d/1MLhhJQ72tMmFT0PrJjlvZJVFfp1srKw7/view?usp=sharing

## Hand Bounding Box Detection
### Data Pre-processing
For Faster-RCNN: Extract bounding box coordinates from the .mat file, then com-
pute the top-left corner (xmin, ymin) and the width and height of the bounding box. Store
the annotations in COCO format and save them as a JSON file.

For YOLO: Extract bounding box coordinates from the .mat file, then determine
the bounding box limits (maxX, minX, maxY, minY). Normalize the center coordinates,
width, and height relative to the image dimensions. Store the annotations in YOLO format
and save them as a .txt file.
![image](https://github.com/user-attachments/assets/19250fd1-bd2e-47bd-bfb3-a42c96c73330)


### Faster_RCNN

Below is a structured text-based workflow diagram explaining each stage of the Faster R-CNN pipeline when using ResNet50 as the backbone for hand bounding box detection.
![Faster-RCNN](https://github.com/user-attachments/assets/fed7478c-2059-443b-be99-cf3edb5203fc)
This section details the pipeline for hand detection using Faster R-CNN with ResNet50 as the backbone. The process consists of multiple stages, including feature extraction, region proposal, classification, and bounding box refinement.

### YOLO
YOLO (You Only Look Once) is a single-shot object detection framework that directly
predicts object bounding boxes and class probabilities from an image in one forward pass.
This section details the key steps in the YOLO detection pipeline.
![image](https://github.com/user-attachments/assets/88e00aed-1c60-47f9-b288-2df66a98ee30)


It divides the input image into a grid, predicts bounding boxes and class probabilities in
a single forward pass, filters low-confidence detections, applies Non-Maximum Suppression
(NMS) to remove duplicates, and outputs the final detected objects.


## Some Document Links:
### Supervisor's Feedback and Meeting Records every time: https://drive.google.com/file/d/1yS3ZDzt_QWBXg7xbEHecqk0ybkTOYvET/view?usp=sharing

