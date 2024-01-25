import os
import numpy as np
import cv2 
import math

# DETECTING COLOUR FROM THE IMAGE
def color_detect(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Define the coordinates of the pixel you want to sample
    x, y = 200, 250

    # Get the BGR color of the specified pixel
    pixel_color = image[y, x]

    # Convert BGR to RGB
    rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

    # Define the ranges for different colors
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

    return closest_color

# Define the colors dictionary
colors = {
    "Black": ["co89", "co88", "co87"],
    "Brown": ["co90", "co91", "co92"],
    "Pink": ["co93", "co94", "co95"]
}

# Get the detected color
detected_color = color_detect(r'E:/AI/Extra/gitCheck/main/muzzles/co93_1c.jpg')

# Get the values associated with the detected color
if detected_color in colors:
    color_values = colors[detected_color]
    print(f"Detected Color: {detected_color}")
    print(f"Color Values: {color_values}")
else:
    print("Color not found in the dictionary.")


