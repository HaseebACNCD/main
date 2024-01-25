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

    # Return the closest color instead of printing it
    return print(closest_color)

# pattern matching algorithm
def match_pattern_in_folders(root_directory, destination_folder, colors, threshold=0.85):
    # Read the template
    template_folder_path = os.path.join(root_directory, destination_folder)

    if not os.path.exists(template_folder_path) or not os.path.isdir(template_folder_path):
        print(f"Error: Template folder '{destination_folder}' not found.")
        return None

    # Find the template image in the template folder
    template_image_name = next((filename for filename in os.listdir(template_folder_path) if filename.endswith(('.jpg', '.jpeg', '.png'))), None)

    if template_image_name is None:
        print("Error: No template image found in the specified template folder.")
        return None

    template_path = os.path.join(template_folder_path, template_image_name)
    template = cv2.imread(template_path)

    if template is None:
        print("Error: Unable to read the template image.")
        return print('edge done')

    # Convert the template to grayscale
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Call color_detect to get the color result
    color_result = color_detect(template_path)

    # Check if color_result is not None before proceeding
    if color_result is not None:
        # Extract the color from the result
        template_color = color_result

        # Iterate through folders in the root directory
        for folder_name in os.listdir(root_directory):
            folder_path = os.path.join(root_directory, folder_name)

            if os.path.isdir(folder_path):
                # Iterate through images in the folder
                for filename in os.listdir(folder_path):
                    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed

                        # Check if the filename contains any color code for the specified color
                        color_to_check = next((color for color, color_codes in colors.items() if any(code in filename for code in color_codes)), None)

                        if color_to_check == template_color:
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
                                    print(f"Pattern matched in folder: {folder_name} (Image: {filename}, Match Percentage: {max_val * 100}%, Color: {color_to_check})")

    else:
        print("Error: Unable to detect color.")






image_path = r'E:/AI/Extra/gitCheck/main/muzzles/co93_1c.jpg'
root_directory = r'E:\AI\Extra\gitCheck\main\muzzles\destination_folder/'  # Replace with the actual path
destination_folder = r'E:\AI\Extra\gitCheck\main\testfolder/'  # Replace with the folder name where the template image is located

colors = {
    "Black": ["co89", "co88", "co87"],
    "Brown": ["co90", "co91", "co92"],
    "Pink": ["co93", "co94", "co95"]
}

color_detect(image_path)
# edge_detect(image_path,destination_folder)


match_pattern_in_folders(root_directory, destination_folder, colors)
