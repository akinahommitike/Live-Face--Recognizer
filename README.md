Real-Time Face Matching with DeepFace
This project demonstrates a real-time face-matching application using OpenCV and the DeepFace library. The application captures video from a webcam, periodically compares frames to a reference image, and displays the match result on the video feed.

**1.Prerequisites**
Before you begin, ensure you have met the following requirements:

Python 3.7 or later
OpenCV
DeepFace
A webcam connected to your computer
A reference image named reference.jpg in the same directory as the script
**Installation**
1. Clone this repository or download the script to your local machine.
2. Install the required Python packages:
**Script Overview**

The script performs the following steps:

1. Initialize Video Capture:

Captures video from the default webcam.
Sets the frame width and height.

2. Load Reference Image:

Loads the reference image (reference.jpg).
Check if the reference image is loaded successfully.

3. Define Face Matching Function:

Uses DeepFace to compare a video frame with the reference image.
Sets a global flag (face_match) based on whether the faces match.

4. Main Loop:

Continuously captures video frames.
Every 30 frames, spawns a new thread to check for face matching.
Displays the match result ("Match" or "No Match") on the video feed.
Allows exiting the loop by pressing the 'q' key.
