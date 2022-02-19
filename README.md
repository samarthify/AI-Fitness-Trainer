MEDIAPIPE BY GOOGLE

The fitness trainer project primarily utilizes the media pipe module to detect the pose of the person in the video. Mediapipe is a set of Customisable ML solutions by Google for Real time tracking. It provides solutions such as face recognition, hand detection, object tracking, human pose estimation etc. This project uses the solution called mediapipe pose.

MediaPipe Pose is a ML solution for high-fidelity body pose tracking, inferring 33 3D landmarks and background segmentation masks on the whole body from RGB video frames. Current state-of-the-art approaches rely primarily on powerful desktop environments for inference, whereas this method achieves real-time performance on most modern mobile phones, desktops/laptops, in python and even on the web.

Pose Landmark Model

The landmark model in MediaPipe Pose predicts the location of 33 pose landmarks. Optionally, MediaPipe Pose can predict a full-body segmentation mask represented as a two-class segmentation (human or background).

CODE FILES

I have divided the project into two files, the PoseModule.py and AITrainer.py. The PoseModule.py is coded such that it can be used to create several other projects with some different use cases and AITrainer.py is the iteration for this specific project. 


PoseModule.py

We start off by importing the required modules for the project. Then we define a class poseDetector() that would contain everything. The pose detection module is initialized giving suitable parameters and the self keyword is used so that we can access the attributes and methods of the class in python, drawing utilities and pose module are also initialized.
The function findPose() is defined that would first convert the bgr input (default) to rgb
(required for pose detection) then draw the landmarks skeleton everytime the landmarks are detected. The findPosition() function is used to convert landmark locations to x,y coordinates in the input. It then adds the information of every landmark to the list in the format [id, x coordinate, y coordinate] and draws circles at every landmark position. The findAngle() function is used to find the angle about a set of any three landmarks, It first picks th 1st and 2nd index from the list i.e. x and y coordinates then the function atan2() from the math module is used to find the angle and is stored in the variable angle. Then some more enhanced lines and circles are drawn at the three landmarks which are the region of interest so it can be easily identified.(I have commented out the part which shows the angle to make the interface look clean, if you want to see that you can remove the ‘#’s)


AITrainer.py

We import the required modules including PoseModule which we just created and define variables to store count (No. of reps), dir(direction of motion during movement 0&1) and pTime(Will be used later to find the frame rate)and read the input video. We then start a while loop that would run till the list we defined earlier becomes of 0 length. (That would happen when the video ends). Then parameters for landmarks are given about which we have to find the angle. For the right arm we use 12,14,16 for the left arm, 11,13,15 and so on. (You can find all the landmark values here). The variables per and bar are defined which contain the minimum angle and maximum angle value. A rep is completed when we start from the minimum angle, reach maximum and come back at minimum. (The values given here can be experimented with, I have chosen them as 210-280 for curls and pushups and 200-260 for squats as they worked for most of the samples. I have used different values for both to achieve increased accuracy). As you may have already noticed, the value of angles are being given in backward direction. I did this since this way it  was easier to give the min and max angle values. While counting push ups or curls leave the lines 20-26 uncommented and 28-33 commented. And vice-versa for counting squats. I have added only three exercises in this project for now but it can be easily extended to any exercise you want to track by changing the landmark values and the angle threshold (if needed). We then use an if loop to count no. of reps and increment the count variable, also the color of the bar changes when min or max angle is reached to give a feedback to the user. Then we draw The percentage count, percentage bar, curl count, some text, and fps count on the video.
