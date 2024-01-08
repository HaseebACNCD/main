import math
import cv2
import numpy as np

# Load the image
# image = cv2.imread('E:/AI/Extra/gitCheck/main/realdata2/co91_1.jpg')
image = cv2.imread('E:/AI/Extra/gitCheck/main/c5_81.jpg')


# Define the list of 8xy values representing coordinates
# coordinates = [
#     (555, 760),
#     (570, 770),
#     (550, 750),
#     (555, 790),
#     (570, 820),
#     (550, 860)
#     # Add more coordinates if needed
# ]
coordinates = [
    
    # (120, 140),
    # (40, 180),
    # (160, 220),
    
    (20, 40),
    (80, 80),
    (50, 240)
    # Add more coordinates if needed
]


# Define the ranges for different colors
color_ranges = {
    'Black': ((0, 0, 0), (85, 85, 85)),
    'Brown': ((86, 86, 86), (170, 170, 170)),
    'Pink': ((171, 171, 171), (255, 255, 255))
}

# Function to calculate Euclidean distance between two points in 3D space
def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


for eight_xy in coordinates:
    # Unpack the x, y values from the tuple
    x, y = eight_xy

    # Get the BGR color of the specified pixel
    pixel_color = image[y, x]

    # Convert BGR to RGB
    rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

# # Loop through the list of 8xy values representing coordinates
# for eight_xy in coordinates:
#     # Convert 8xy values to (x, y) format
#     x = int(str(eight_xy)[0])
#     y = int(str(eight_xy)[1:])

#     # Get the BGR color of the specified pixel
#     pixel_color = image[y, x]

#     # Convert BGR to RGB
#     rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

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

    # Mark the pixel on the image
    cv2.circle(image, (x, y), 5, (0, 255, 0), -1)  # Draws a green circle around the pixel

# Display the image with marked pixels
cv2.imshow('Image with Marked Pixels', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
