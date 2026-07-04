import cv2
import numpy as np

# 1. Load your pre-recorded video
video_path = 'test_video.mp4' # Make sure this matches your video file name
cap = cv2.VideoCapture(video_path)

# Graceful Error Handling: Check if the video loaded correctly
if not cap.isOpened():
    print(f"Error: Could not open video file '{video_path}'. Please check the file path.")
    exit()

while True:
    success, frame = cap.read()
    
    # If the video ends, exit the loop
    if not success:
        break

    # Resize the frame for a consistent viewing window
    frame = cv2.resize(frame, (640, 480))

    # 2. Convert the frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 3. Define the color bounds for Blue 
    # (Adjust these if your specific object needs tweaking based on your trackbar testing)
    lower_bound = np.array([90, 100, 100])
    upper_bound = np.array([130, 255, 255])

    # 4. Create the black-and-white mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # 5. Find contours on the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through all found contours
    for contour in contours:
        area = cv2.contourArea(contour)

        # Filter out background noise (only track objects larger than 500 pixels)
        if area > 500:
            # Get the bounding box coordinates (x, y, width, height)
            x, y, w, h = cv2.boundingRect(contour)

            # Draw a Green rectangle around the object on the original frame
            # Parameters: image, top-left corner, bottom-right corner, color (BGR), thickness
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Define the text label
            label = "Blue Object"
            
            # Draw the text slightly above the rectangle (y - 10 moves it up)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # 6. Display the video windows
    cv2.imshow("Original Video", frame)
    cv2.imshow("Mask (White = Target)", mask)

    # 7. Press 'q' to exit the video early
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Clean up memory and close windows when done
cap.release()
cv2.destroyAllWindows()