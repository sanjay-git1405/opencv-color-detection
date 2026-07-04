# Real-Time Color Detection

A beginner-friendly Computer Vision project built with Python and OpenCV. 

## Features
* Converts video frames from BGR to HSV color space.
* Uses masking to isolate specific colors (currently configured for Blue).
* Draws a dynamic bounding box and text label around the detected object in real-time.

## Installation
1. Clone this repository.
2. Install the required libraries:
   `pip install -r requirements.txt`
3. Add a test video to the folder and update the `video_path` variable in the code.
4. Run `python color_tracker.py`.