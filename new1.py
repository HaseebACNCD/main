# import cv2
# import os
# import numpy as np


# def match_template_in_folders(root_folder, template_path, threshold=0.85):
#     # Read the template image
#     template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
#     if template is None:
#         print("Error: Unable to read the template image.")
#         return

#     # Iterate through folders in the root directory
#     for folder_name in os.listdir(root_folder):
#         folder_path = os.path.join(root_folder, folder_name)

#         if os.path.isdir(folder_path):
#             print(f"Processing folder: {folder_name}")

#             # Iterate through images in the folder
#             for img_filename in os.listdir(folder_path):
#                 if img_filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
#                     image_path = os.path.join(folder_path, img_filename)

#                     # Read the main image
#                     main_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#                     if main_image is None:
#                         print(f"Error: Unable to read the main image {image_path}")
#                         continue  # Skip to the next image

#                     # Resize the template to match the dimensions of the main image
#                     template_resized = cv2.resize(template, (main_image.shape[1], main_image.shape[0]))

#                     # Convert the main image to CV_32F for matching
#                     main_image = main_image.astype(np.float32)

#                     # Convert the template to CV_32F for matching
#                     template_resized = template_resized.astype(np.float32)

#                     # Match the resized template using cv2.matchTemplate
#                     result = cv2.matchTemplate(main_image, template_resized, cv2.TM_CCOEFF_NORMED)

#                     # Get the maximum correlation coefficient
#                     max_val = np.max(result)

#                     # If match is found above the threshold, print the result
#                     if max_val >= threshold:
#                         print(f"Pattern matched in folder: {folder_name} (Image: {img_filename}, Match Percentage: {max_val * 100}%)")




# # Example usage
# root_folder_path = r"E:\AI\Extra\gitCheck\main\muzzles\destination_folder/"  # Replace with the actual path
# template_image_path = r"E:\AI\Extra\gitCheck\main\destination_folder/co88_1c.jpg"  # Replace with the actual path

# # Specify the matching threshold (adjust as needed)
# matching_threshold = 0.85

# # Call the function to match template in all folders
# match_template_in_folders(root_folder_path, template_image_path, matching_threshold)



import cv2
import os
import numpy as np

def match_template_in_folders(root_folder, template_path, color, threshold=0.85):
    # Read the template image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print("Error: Unable to read the template image.")
        return

    # Check if the color is in the colors dictionary
    if color not in colors:
        print(f"Error: Color '{color}' not found in the colors dictionary.")
        return

    # Get the list of folders for the specified color
    folders_for_color = colors[color]

    # Iterate through folders in the root directory
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        if os.path.isdir(folder_path) and folder_name in folders_for_color:
            print(f"Processing folder: {folder_name}")

            # Iterate through images in the folder
            for img_filename in os.listdir(folder_path):
                if img_filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
                    image_path = os.path.join(folder_path, img_filename)

                    # Read the main image
                    main_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    if main_image is None:
                        print(f"Error: Unable to read the main image {image_path}")
                        continue  # Skip to the next image

                    # Resize the template to match the dimensions of the main image
                    template_resized = cv2.resize(template, (main_image.shape[1], main_image.shape[0]))

                    # Convert the main image to CV_32F for matching
                    main_image = main_image.astype(np.float32)

                    # Convert the template to CV_32F for matching
                    template_resized = template_resized.astype(np.float32)

                    # Match the resized template using cv2.matchTemplate
                    result = cv2.matchTemplate(main_image, template_resized, cv2.TM_CCOEFF_NORMED)

                    # Get the maximum correlation coefficient
                    max_val = np.max(result)

                    # If match is found above the threshold, print the result
                    if max_val >= threshold:
                        print(f"Pattern matched in folder: {folder_name} (Image: {img_filename}, Match Percentage: {max_val * 100}%)")

# Example usage
root_folder_path = r"E:\AI\Extra\gitCheck\main\muzzles\destination_folder/"  # Replace with the actual path
template_image_path = r"E:\AI\Extra\gitCheck\main\destination_folder/co94_1c.jpg"  # Replace with the actual path
color_to_search = "Pink"  # Replace with the desired color

# Dictionary of color patterns
colors = {
    "Black": ["co89", "co88", "co87"],
    "Brown": ["co90", "co91", "co92"],
    "Pink": ["co93", "co94", "co95"]
}

# Specify the matching threshold (adjust as needed)
matching_threshold = 0.85

# Call the function to match template in folders of the specified color
match_template_in_folders(root_folder_path, template_image_path, color_to_search, matching_threshold)
