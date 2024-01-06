
# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('E:/AI/Extra/gitCheck/main/c6_1.jpg')

# # Define the coordinates of the pixel you want to sample
# x, y = 400, 400

# # Get the color of the specified pixel
# pixel_color = image[y, x]

# # Mark the pixel on the image
# marked_image = image.copy()
# cv2.circle(marked_image, (x, y), 5, (0, 255, 0), -1)  # Draws a green circle around the pixel

# # Display the color values
# print(f"Color of pixel at ({x}, {y}): BGR {pixel_color}")

# # Display the marked image
# cv2.imshow('Image with Marked Pixel', marked_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# =====================================================================================

# ====================================================================================


# ------------------------------------------------------------------------------

import math
import cv2
import numpy as np

# Load the image
image = cv2.imread('E:/AI/Extra/gitCheck/main/dis1_1.png')

# Define the coordinates of the pixel you want to sample
# x, y = 650, 560
# x, y = 150, 250  c1_568
x , y  = 80 , 140   # dis1_1.png
x , y  = 


# Get the BGR color of the specified pixel
pixel_color = image[y, x]

# Convert BGR to RGB
rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

# Define the ranges for different colors

# color_ranges = {
#     'Black': ((0, 0, 0), (63, 63, 63)),
#     'Brown': ((64, 64, 64), (127, 127, 127)),
#     'Yellow': ((128, 128, 128), (191, 191, 191)),
#     'Pink': ((192, 192, 192), (255, 255, 255))
# }
color_ranges = {
    'Black': ((0, 0, 0), (85, 85, 85)),
    'Brown': ((86, 86, 86), (170, 170, 170)),
    'Pink': ((171, 171, 171), (255, 255, 255))
}


# Function to calculate Euclidean distance between two points in 3D space
def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Initialize variables to track closest color and distance
closest_color = None
closest_distance = float('inf')

# Find the closest color
for color, (lower, upper) in color_ranges.items():
    # Calculate the center of the color range
    center = [(lower[i] + upper[i]) / 2 for i in range(3)]
    # Calculate the distance between the value and the center of the color range
    distance = euclidean_distance(rgb_color, center)
    # Update closest color if this color is closer
    if distance < closest_distance:
        closest_distance = distance
        closest_color = color

print(f"The closest color to the rgb_color {rgb_color} is {closest_color}.")







