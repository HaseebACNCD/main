# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('E:/AI/Extra/gitCheck/main/dis1_1.png')

# # Convert BGR to HSV color space
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # Define the lower and upper bounds for the color you want to detect (e.g., red)
# lower_color = np.array([0, 100, 100])  # Lower HSV values for red
# upper_color = np.array([10, 255, 255])  # Upper HSV values for red

# # Create a mask to isolate the specified color range
# mask = cv2.inRange(hsv, lower_color, upper_color)

# # Find contours in the mask
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Draw the detected contours on the original image
# for contour in contours:
#     area = cv2.contourArea(contour)
#     if area > 100:  # To filter out small areas (adjust as needed)
#         cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)  # Draw contours in green

# # Display the image with detected spots
# cv2.imshow('Detected Spots', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Load the image
image = cv2.imread('E:/AI/Extra/gitCheck/main/dis1_1.png')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for the colors you want to detect (example: red and green)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

# Create masks for the specified color ranges
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Combine masks to get the regions with the specified colors
result = cv2.bitwise_or(mask_red, mask_green)  # Add more masks as needed

# Find contours of the detected regions
contours, _ = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:  # Filter out small areas (adjust as needed)
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)  # Draw contours in green

# Display the image with detected regions of different colors
cv2.imshow('Detected Colors', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
