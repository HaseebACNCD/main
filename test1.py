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



import os
import numpy as np
import cv2
import math

# DETECTING COLOUR FROM THE IMAGE
def color_detect(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return None

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

    return closest_color  # Return the detected color instead of printing

# Define the colors dictionary
colors = {
    "Black": ["co89", "co88", "co87"],
    "Brown": ["co90", "co91", "co92"],
    "Pink": ["co93", "co94", "co95"]
}

def match_pattern_in_folders(root_directory, color_system, threshold=0.85, template_path=None):
    # Get the detected color for the template
    detected_color = color_detect(template_path)  # Pass the template_path here

    if detected_color is None or detected_color not in color_system:
        print("Detected color not found in the color system.")
        return

    # Get the folders associated with the detected color
    color_folders = color_system[detected_color]

    # Iterate through folders in the root directory
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)

        if os.path.isdir(folder_path) and folder_name in color_folders:
            # Iterate through images in the folder
            for filename in os.listdir(folder_path):
                if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
                    image_path = os.path.join(folder_path, filename)

                    # Read the main image
                    main_image = cv2.imread(image_path)

                    if main_image is not None:
                        # Resize the template to match the dimensions of the main image
                        template_resized = cv2.resize(template_gray, (main_image.shape[1], main_image.shape[0]))

                        # Convert the main image to grayscale
                        main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

                        # Match the resized template using cv2.matchTemplate
                        result = cv2.matchTemplate(main_gray, template_resized, cv2.TM_CCOEFF_NORMED)

                        # Get the maximum correlation coefficient
                        max_val = np.max(result)

                        # If match is found above the threshold, print the folder name
                        if max_val >= threshold:
                            print(f"Pattern matched in folder: {folder_name} (Image: {filename}, Match Percentage: {max_val * 100}%)")

# Example usage
image_path = r'E:/AI/Extra/gitCheck/main/muzzles/co88_1c.jpg'
root_directory = r'E:/AI/Extra/gitCheck/main/muzzles/destination_folder/'  # Use consistent slashes
template_path = r'E:/AI/Extra/gitCheck/main/muzzles/co93_1c.jpg'  # Use consistent slashes
detected_color = color_detect(image_path)
if detected_color:
    print(f"Detected Color: {detected_color}")
    match_pattern_in_folders(root_directory, colors, template_path=template_path)
