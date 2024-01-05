# import cv2

# # Load the image
# image = cv2.imread('E:/AI/Extra/gitCheck/main/B1.png')

# # Get the color of a specific pixel (for example, at position x=100, y=100)
# x, y = 100, 100
# pixel_color = image[y, x]  # OpenCV uses BGR ordering

# # Display the color values
# print(f"Color of pixel at ({x}, {y}): BGR {pixel_color}")

# # Display the color values as separate BGR channels
# blue, green, red = pixel_color
# print(f"Blue: {blue}, Green: {green}, Red: {red}")
# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('E:/AI/Extra/gitCheck/main/B1.png')

# # Define the coordinates of the pixel you want to sample
# x, y = 500, 100

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


# import cv2
# import webcolors
# import numpy as np

# # Load the image
# image = cv2.imread('E:/AI/Extra/gitCheck/main/B1-sun.png')

# # Define the coordinates of the pixel you want to sample
# x, y = 500, 500

# # Get the BGR color of the specified pixel
# pixel_color = image[y, x]

# # Convert BGR to RGB
# rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

# # Function to find the closest predefined color
# def find_nearest_color(rgb_val):
#     min_distance = float('inf')
#     closest_color = None
#     for color_name, color_rgb in webcolors.CSS3_NAMES_TO_HEX.items():
#         # Convert predefined color RGB to numpy array for calculations
#         predefined_rgb = np.array(webcolors.hex_to_rgb(color_rgb))
#         # Calculate Euclidean distance between provided RGB and predefined color
#         distance = np.linalg.norm(np.array(rgb_val) - predefined_rgb)
#         if distance < min_distance:
#             min_distance = distance
#             closest_color = color_name
#     return closest_color

# # Get the nearest predefined color name
# nearest_color = find_nearest_color(rgb_color)

# # Mark the spot on the image
# marked_image = image.copy()
# cv2.circle(marked_image, (x, y), 5, (0, 255, 0), -1)  # Draw a green circle at the pixel location

# # Display the marked image
# cv2.imshow('Image with Marked Pixel', marked_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Display the nearest color name
# print(f"Nearest predefined color for pixel at ({x}, {y}): {nearest_color}")

# =====================================================================================




# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('E:/AI/Extra/gitCheck/main/B1.png')

# # Define the coordinates of the pixel you want to sample
# x, y = 500, 500

# # Get the BGR color of the specified pixel
# pixel_color = image[y, x]

# # Convert BGR to RGB
# rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])


# print(rgb_color,'rgb valiue -----------------')
# # Function to find the closest predefined color based on specific ranges
# def find_nearest_color(rgb_val):
#     # Define color ranges
#     color_ranges = {
#         'Red': ((200, 0, 0), (255, 50, 50)),
#         'Green': ((0, 100, 0), (0, 200, 0)),
#         'Blue': ((0, 0, 200), (50, 50, 255)),
#         'Yellow': ((200, 200, 0), (255, 255, 50)),
#         'Purple': ((80, 0, 80), (180, 0, 180)),
#         'Cyan': ((0, 180, 180), (80, 255, 255)),
#         'White': ((0, 0, 0), (255, 255, 255)),
#         'Black': ((0, 0, 0), (0, 0, 0)),
#         'Gray': ((100, 100, 100), (180, 180, 180)),
#         'Orange': ((200, 100, 0), (255, 180, 50)),
#         'Pink': ((220, 150, 150), (255, 210, 210))
#     }

#     min_distance = float('inf')
#     closest_color = None

#     for color_name, (lower, upper) in color_ranges.items():
#         # Check if the RGB value is within the defined range
#         if all(lower[i] <= val <= upper[i] for i, val in enumerate(rgb_val)):
#             closest_color = color_name
#             break

#     return closest_color

# # Get the nearest predefined color name based on ranges
# nearest_color = find_nearest_color(rgb_color)

# # Mark the spot on the image
# marked_image = image.copy()
# cv2.circle(marked_image, (x, y), 5, (0, 255, 0), -1)  # Draw a green circle at the pixel location

# # Display the marked image
# cv2.imshow('Image with Marked Pixel', marked_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Display the nearest color name based on ranges
# print(f"Nearest predefined color for pixel at ({x}, {y}): {nearest_color}")

# ====================================================================================


# ------------------------------------------------------------------------------

import math
import cv2
import numpy as np

# Load the image
image = cv2.imread('E:/AI/Extra/gitCheck/main/B1-sun.png')

# Define the coordinates of the pixel you want to sample
x, y = 500, 500

# Get the BGR color of the specified pixel
pixel_color = image[y, x]

# Convert BGR to RGB
rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

# Define your value
# value = (125, 90, 70)

# Define the ranges for different colors
color_ranges = {
    'Red': ((200, 0, 0), (255, 50, 50)),
    'Green': ((0, 100, 0), (0, 200, 0)),
    'Blue': ((0, 0, 200), (50, 50, 255)),
    'Yellow': ((200, 200, 0), (255, 255, 50)),
    'Purple': ((80, 0, 80), (180, 0, 180)),
    'Cyan': ((0, 180, 180), (80, 255, 255)),
    'Black': ((0, 0, 0), (0, 0, 0)),
    'Gray': ((100, 100, 100), (180, 180, 180)),
    'Orange': ((200, 100, 0), (255, 180, 50)),
    'Pink': ((220, 150, 150), (255, 210, 210))
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

