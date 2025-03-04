# BDRP
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



## Hand Bounding Box Detection

