import cv2
import numpy as np

# Load the image with the green screen background
image = cv2.imread('shiva.jpg')

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the green color in HSV format
lower_green = np.array([35, 100, 50])  # Adjust these values
upper_green = np.array([85, 255, 255])  # Adjust these values

# Create a mask that selects the green screen color in the HSV color space
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Apply morphological erosion to the mask to reduce the outline
kernel = np.ones((5, 5), np.uint8)  # Adjust the kernel size as needed
mask = cv2.erode(mask, kernel, iterations=1)

# Load the replacement background image
background = cv2.imread('bg.jpg')

# Resize the background image to match the dimensions of the original image
background = cv2.resize(background, (image.shape[1], image.shape[0]))

# Invert the mask, so we select the non-green areas
mask_inv = cv2.bitwise_not(mask)

# Extract the foreground and background regions
fg = cv2.bitwise_and(image, image, mask=mask_inv)
bg = cv2.bitwise_and(background, background, mask=mask)

# Combine the foreground and background
result = cv2.add(fg, bg)

# Display the result
cv2.imshow('Green Screen Replacement', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
