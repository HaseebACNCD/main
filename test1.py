# import math
# import cv2
# import numpy as np

# # Load the image
# # image = cv2.imread('E:/AI/Extra/gitCheck/main/realdata2/co91_1.jpg')
# image = cv2.imread('E:/AI/Extra/gitCheck/main/c1_2.jpg')


# # Define the list of 8xy values representing coordinates
# # coordinates = [
# #     (555, 760),
# #     (570, 770),
# #     (550, 750),
# #     (555, 790),
# #     (570, 820),
# #     (550, 860)
# #     # Add more coordinates if needed
# # ]
# coordinates = [

    
#     (20, 40),
#     (80, 80),
#     (120, 280)
#     # Add more coordinates if needed
# ]


# # Define the ranges for different colors
# color_ranges = {
#     'Black': ((0, 0, 0), (100, 100, 100)),
#     'Brown': ((101, 101, 101), (190, 190, 190)),
#     'Pink': ((191, 191, 191), (255, 255, 255))
# }

# # Function to calculate Euclidean distance between two points in 3D space
# def euclidean_distance(point1, point2):
#     return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


# for eight_xy in coordinates:
#     # Unpack the x, y values from the tuple
#     x, y = eight_xy

#     # Get the BGR color of the specified pixel
#     pixel_color = image[y, x]

#     # Convert BGR to RGB
#     rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

# # # Loop through the list of 8xy values representing coordinates
# # for eight_xy in coordinates:
# #     # Convert 8xy values to (x, y) format
# #     x = int(str(eight_xy)[0])
# #     y = int(str(eight_xy)[1:])

# #     # Get the BGR color of the specified pixel
# #     pixel_color = image[y, x]

# #     # Convert BGR to RGB
# #     rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

#     # Initialize variables to track closest color and distance
#     closest_color = None
#     closest_distance = float('inf')

#     # Find the closest color
#     for color, (lower, upper) in color_ranges.items():
#         # Calculate the center of the color range
#         center = [(lower[i] + upper[i]) / 2 for i in range(3)]
#         # Calculate the distance between the value and the center of the color range
#         distance = euclidean_distance(rgb_color, center)
#         # Update closest color if this color is closer
#         if distance < closest_distance:
#             closest_distance = distance
#             closest_color = color

#     print(f"The closest color to the rgb_color {rgb_color} is {closest_color}.")

#     # Mark the pixel on the image
#     cv2.circle(image, (x, y), 5, (0, 255, 0), -1)  # Draws a green circle around the pixel

# # Display the image with marked pixels
# cv2.imshow('Image with Marked Pixels', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# ------------------------------------------------------------------------------------------------


from PIL import Image

# Load the image
image_path = 'E:/AI/Extra/gitCheck/main/muzzles/co94_1c.jpg'   # Replace this with the path to your image
img = Image.open(image_path)

# Get the width and height of the image
width, height = img.size

# Create a set to store unique colors
unique_colors = set()

# Iterate through each pixel to collect unique colors
for x in range(width):
    for y in range(height):
        pixel_color = img.getpixel((x, y))
        unique_colors.add(pixel_color)

# Count the number of unique colors
num_unique_colors = len(unique_colors)
print(f"Number of unique colors in the image: {num_unique_colors}")

# Define the coordinates of the region (left, upper, right, lower)
# These coordinates represent the bounding box of the color patch
patch_coordinates = (100, 100, 200, 200)  # Adjust these coordinates as needed

# Crop the image to the specified patch coordinates
color_patch = img.crop(patch_coordinates)

# Show the color patch (optional)
color_patch.show()

# Get the average color of the patch
patch_color = color_patch.getpixel((0, 0))  # Assuming the patch is 1 pixel; adjust if different
print(f"Color of the patch: {patch_color}")


