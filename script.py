import cv2
import numpy as np
import pyautogui, pydirectinput
import time
from PIL import Image, ImageGrab
from skimage.metrics import structural_similarity as ssim
import keyboard

# Function to capture the screen
def capture_screen_and_save(filename):
    screenshot = ImageGrab.grab()  # Capture the screen
    screenshot.save(filename)

# Function to perform image recognition
def check_similarity(screenshot_path, reference_image_path):
    screenshot = cv2.imread(screenshot_path)
    reference_image = cv2.imread(reference_image_path)
    similarity = 0.0

    if screenshot is None or reference_image is None:
        print("Error: Unable to load image.")
        return similarity

    # Convert the images to grayscale
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    gray_reference = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

    # Compute the Structural Similarity Index (SSI)
    similarity = ssim(gray_screenshot, gray_reference)

    return similarity

# Function to perform inputs if similarity is above a threshold
def perform_inputs():
    time.sleep(3)
    pydirectinput.press('w')
    time.sleep(1)
    pydirectinput.press('enter')
    pass

# Main function
def main():
    reference_image_path = 'test.png'
    similarity_threshold = 0.9
    capture_interval = 20  # in seconds
    screenshot_filename = 'captured_screenshot.png'
    print('Script is running...')
    while True:
        start_time = time.time()
        
        # Capture the screen and save it as a PNG file
        capture_screen_and_save(screenshot_filename)

        # Check similarity with the reference image
        similarity = check_similarity(screenshot_filename, reference_image_path)

        # Perform inputs if similarity is above the threshold
        if similarity >= similarity_threshold:
            perform_inputs()

        # Calculate time elapsed and sleep until the next capture
        elapsed_time = time.time() - start_time
        sleep_time = max(capture_interval - elapsed_time, 0)
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()
