import cv2
import os
import numpy as np

def match_pattern_in_folders(root_directory, template_folder_path, color, threshold=0.85):
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
            # Check if the provided template folder path exists
            template_folder = os.path.join(template_folder_path, folder_name.replace("/", os.path.sep))
            print(template_folder)
            if not os.path.exists(template_folder):
                print(f"Error: Template folder '{template_folder}' does not exist.")
                continue  # Skip to the next folder

            # Iterate through images in the template folder
            for filename in os.listdir(template_folder):
                print(filename)
                if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
                    template_path = os.path.join(template_folder, filename)
                    print(f"Template path: {template_path}")

                    # Read the template
                    template = cv2.imread(template_path)
                    print(f"Template image: {template}")
                    if template is None:
                        print(f"Error: Unable to read the template image.")
                        continue  # Skip to the next image

                    # Iterate through folders in the root directory
                    for root_folder_name in os.listdir(root_directory):
                        root_folder_path = os.path.join(root_directory, root_folder_name)

                        if os.path.isdir(root_folder_path):
                            print(root_folder_path)
                            # Iterate through images in the folder
                            for img_filename in os.listdir(root_folder_path):
                                if img_filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
                                    image_path = os.path.join(root_folder_path, img_filename)
                                    print(f"Main image path: {image_path}")

                                    # Read the main image
                                    main_image = cv2.imread(image_path)
                                    if main_image is None:
                                        print(f"Error: Unable to read the main image.")
                                        continue  # Skip to the next image

                                    # Resize the template to match the dimensions of the main image
                                    template_resized = cv2.resize(template, (main_image.shape[1], main_image.shape[0]))

                                    # Convert the main image to grayscale
                                    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

                                    # Match the resized template using cv2.matchTemplate
                                    result = cv2.matchTemplate(main_gray, template_resized, cv2.TM_CCOEFF_NORMED)

                                    # Get the maximum correlation coefficient
                                    max_val = np.max(result)

                                    # If match is found above the threshold, print the folder name
                                    if max_val >= threshold:
                                        print(f"Pattern matched in folder: {root_folder_name} (Image: {img_filename}, Match Percentage: {max_val * 100}%)")

# Example usage
root_directory = r'E:/AI/Extra/gitCheck/main/muzzles/destination_folder/'  # Replace with the actual path
template_folder_path = r'E:/AI/Extra/gitCheck/main/destination_folder/'  # Replace with the actual path
color_to_search = "Pink"  # Replace with the desired color

# Dictionary of color patterns
colors = {
    "Black": ["co89", "co88", "co87"],
    "Brown": ["co90", "co91", "co92"],
    "Pink": ["co93", "co94", "co95"]
}

match_pattern_in_folders(root_directory, template_folder_path, color_to_search)
