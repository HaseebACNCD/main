import math
import cv2
import os
import numpy as np



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

    # print(f"The closest color to the rgb_color {rgb_color} is {closest_color}.")
    
    return print(closest_color)




# MAKING EDGE DETECTING FILES
def edge_detect(image_path, destination_folder):
    try:
        # Specify the filename of the image you want to process
        filename_to_process = os.path.basename(image_path)

        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            raise Exception(f"Error: Unable to read the image at '{image_path}'")

        # Apply median filter for noise removal
        image_filtered = cv2.medianBlur(image, 5)  # Adjust kernel size as needed

        # Perform Canny edge detection on the filtered image
        edges = cv2.Canny(image_filtered, threshold1=5, threshold2=10)

        # Construct the full path to the destination image
        destination_image_path = os.path.join(destination_folder, filename_to_process)

        # Save the edge-detected image to the destination folder    
        cv2.imwrite(destination_image_path, edges)

        # print("Edge detection complete. Edge-detected image is saved in:", destination_folder)
        return destination_image_path

    except Exception as e:
        print(f"Error: {e}")
        return None

colors = {
    "Black": ["co89", "co88", "co87"],
    "Brown": ["co90", "co91", "co92"],
    "Pink": ["co93", "co94", "co95"]}

# pattern matching algorithm
# def match_pattern_and_remove(root_directory, destination_folder, threshold=0.85):
#     # List to store matched image paths
#     matched_images = []

#     # Iterate through images in the template directory
#     for template_filename in os.listdir(destination_folder):
#         if template_filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
#             template_path = os.path.join(destination_folder, template_filename)

#             # Read the template image
#             template = cv2.imread(template_path)

#             if template is not None:
#                 # Convert the template to grayscale
#                 template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

#                 # Iterate through folders in the root directory
#                 for folder_name in os.listdir(root_directory):
#                     folder_path = os.path.join(root_directory, folder_name)

#                     if os.path.isdir(folder_path):
#                         # Iterate through images in the folder
#                         for filename in os.listdir(folder_path):
#                             if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
#                                 image_path = os.path.join(folder_path, filename)

#                                 # Read the main image
#                                 main_image = cv2.imread(image_path)

#                                 if main_image is not None:
#                                     # Resize the template to match the dimensions of the main image
#                                     template_resized = cv2.resize(template_gray, (main_image.shape[1], main_image.shape[0]))

#                                     # Convert the main image to grayscale
#                                     main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

#                                     # Match the resized template using cv2.matchTemplate
#                                     result = cv2.matchTemplate(main_gray, template_resized, cv2.TM_CCOEFF_NORMED)

#                                     # Get the maximum correlation coefficient
#                                     max_val = np.max(result)

#                                     # If match is found above the threshold, remove the matched image
#                                     if max_val >= threshold:
#                                         matched_images.append(image_path)
#                                         print(f"Pattern matched (Image: {filename}, Match Percentage: {max_val * 100}%)")


#     # Check if there are matched images
#     if not matched_images:
#         print("No matching images found in the specified folders.")


# pattern matching algorithm
def match_pattern_and_remove(root_directory, destination_folder, threshold=0.85, color=None):
    # List to store matched image paths
    matched_images = []

    # Check if color parameter is provided
    if color is not None:
        color_folders = colors.get(color)
        if color_folders is None:
            print(f"Invalid color: {color}")
            return
    else:
        # If color is not provided, match patterns in all color folders
        color_folders = [folder for folders in colors.values() for folder in folders]

    # Iterate through color folders
    for folder_name in color_folders:
        folder_path = os.path.join(destination_folder, folder_name)

        if os.path.exists(folder_path):
            # Iterate through images in the template directory
            for template_filename in os.listdir(folder_path):
                if template_filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
                    template_path = os.path.join(folder_path, template_filename)

                    # Read the template image
                    template = cv2.imread(template_path)

                    if template is not None:
                        # Convert the template to grayscale
                        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

                        # Iterate through folders in the root directory
                        for root_folder_name in os.listdir(root_directory):
                            root_folder_path = os.path.join(root_directory, root_folder_name)

                            if os.path.isdir(root_folder_path):
                                # Iterate through images in the folder
                                for filename in os.listdir(root_folder_path):
                                    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
                                        image_path = os.path.join(root_folder_path, filename)

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

                                            # If match is found above the threshold, remove the matched image
                                            if max_val >= threshold:
                                                matched_images.append(image_path)
                                                print(f"Pattern matched (Image: {filename}, Color: {folder_name}, Match Percentage: {max_val * 100}%)")


    # Check if there are matched images
    if not matched_images:
        print("No matching images found in the specified folders.")




def delete_data(destination_folder):

    # Get a list of all files in the folder
    files = os.listdir(destination_folder)

    # Iterate through the list and remove each file
    for file in files:
        file_path = os.path.join(destination_folder, file)
        os.remove(file_path)
        return print('delete done')


# color=color_result
# # Example usage
# root_directory = r"E:\AI\Extra\gitCheck\main\muzzles\destination_folder/"
# image_path = r'E:/AI/Extra/gitCheck/main/muzzles/co88_1c.jpg'
# destination_folder = r'E:\AI\Extra\gitCheck\main\testfolder/'
# color_result = color_detect(image_path)
# color=str(color_result)
# edge_detected = edge_detect(image_path,destination_folder)
# # match_pattern_and_remove(root_directory, destination_folder)
# match_pattern_and_remove(root_directory, destination_folder, color)
# delete_data (destination_folder)



# Example usage
root_directory = r"E:\AI\Extra\gitCheck\main\muzzles\destination_folder/"
image_path = r'E:/AI/Extra/gitCheck/main/muzzles/co88_1c.jpg'
destination_folder = r'E:\AI\Extra\gitCheck\main\testfolder/'
color_result = color_detect(image_path)
color = color_result  # Assign the value of color_result to color
edge_detected = edge_detect(image_path, destination_folder)
match_pattern_and_remove(root_directory, destination_folder, color)
# delete_data(destination_folder)
