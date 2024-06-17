'''----------------------------------------
Adrial Armijo
Colorado State University - Global
CSC515 - Computer Vision

Portfolio Assignment 1: OpenCV Demonstration
Tasks:
    - Import an image
    - Display the image
    - Write the image to a directory
    
imports: 
    opencv-python-4.10.0.82
    numpy-1.26.4
-------------------------------------------'''
import cv2
import os

# Step 1: Import an image
image_path = 'brain.jpg' 
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image.")
else:
    # Step 2: Display the image
    cv2.imshow('Imported Image', image)
    print("Image is now displayed.")
    
    # Wait until a key is pressed, then clear the screen
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 3: Write a copy of the image to a directory on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop') #MacOS/Linux specific
    
    output_directory = os.path.join(desktop_path, 'Copies')
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    output_path = os.path.join(output_directory, 'copied_brain.jpg')
    cv2.imwrite(output_path, image)
    print(f"Image saved to {output_path}")

