import cv2

# Open the default camera (usually index 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # Capture a single frame
    ret, frame = cap.read()
    if ret:
        # Save the captured image
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured and saved as captured_image.jpg")
    else:
        print("Error: Could not capture image.")

# Release the camera
cap.release()
