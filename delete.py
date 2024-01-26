
# import os

# folder_path = "path/to/your/folder"
# def delete_data():

#     # Get a list of all files in the folder
#     files = os.listdir(folder_path)

#     # Iterate through the list and remove each file
#     for file in files:
#         file_path = os.path.join(folder_path, file)
#         os.remove(file_path)
#         return print('delete done')



# import cv2
# import os
# import numpy as np

# def match_pattern_in_folders(root_directory, template_path, threshold=0.85):
#     # Read the template
#     template = cv2.imread(template_path)

#     if template is None:
#         print("Error: Unable to read the template image.")
#         return None

#     # Convert the template to grayscale
#     template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

#     # Iterate through folders in the root directory
#     for folder_name in os.listdir(root_directory):
#         folder_path = os.path.join(root_directory, folder_name)

#         if os.path.isdir(folder_path):
#             # Iterate through images in the folder
#             for filename in os.listdir(folder_path):
#                 if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
#                     image_path = os.path.join(folder_path, filename)

#                     # Read the main image
#                     main_image = cv2.imread(image_path)

#                     if main_image is not None:
#                         # Resize the template to match the dimensions of the main image
#                         template_resized = cv2.resize(template_gray, (main_image.shape[1], main_image.shape[0]))

#                         # Convert the main image to grayscale
#                         main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

#                         # Match the resized template using cv2.matchTemplate
#                         result = cv2.matchTemplate(main_gray, template_resized, cv2.TM_CCOEFF_NORMED)

#                         # Get the maximum correlation coefficient
#                         max_val = np.max(result)

#                         # If match is found above the threshold, print the folder name
#                         if max_val >= threshold:
#                             print(f"Pattern matched in folder: {folder_name} (Image: {filename}, Match Percentage: {max_val * 100}%)")

# # Example usage
# root_directory = r'E:\AI\Extra\gitCheck\main\muzzles\destination_folder/'  # Replace with the actual path
# template_path = r'E:\AI\Extra\gitCheck\main\destination_folder/co94_1c.jpg'  # Replace with the actual path

# match_pattern_in_folders(root_directory, template_path)



import cv2
import os
import numpy as np

def match_pattern_in_folders(root_directory, template_path, color, threshold=0.85):
    # Read the templategit 
    template = cv2.imread(template_path)

    if template is None:
        print("Error: Unable to read the template image.")
        return None

    # Convert the template to grayscale
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Check if the color is in the colors dictionary
    if color not in colors:
        print(f"Error: Color '{color}' not found in the colors dictionary.")
        return None

    # Get the list of folder names for the specified color
    folders_for_color = colors[color]

    # Iterate through folders for the specified color
    for folder_name in folders_for_color:
        folder_path = os.path.join(root_directory, folder_name)

        if os.path.isdir(folder_path):
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
root_directory = r'E:\AI\Extra\gitCheck\main\muzzles\destination_folder/'  # Replace with the actual path
template_path = r'E:\AI\Extra\gitCheck\main\destination_folder/co94_1c.jpg'  # Replace with the actual path
color_to_search = "Pink"  # Replace with the desired color

# Dictionary of color patterns
colors = {
    "Black": ["co89", "co88", "co87"],
    "Brown": ["co90", "co91", "co92"],
    "Pink": ["co93", "co94", "co95"]
}

match_pattern_in_folders(root_directory, template_path, color_to_search)
