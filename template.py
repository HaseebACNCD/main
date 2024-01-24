import cv2
import os
import numpy as np

def match_pattern_in_folders(root_directory, template_path, threshold=0.85):
    # Read the template
    template = cv2.imread(template_path)

    if template is None:
        print("Error: Unable to read the template image.")
        return None

    # Convert the template to grayscale
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Iterate through folders in the root directory
    for folder_name in os.listdir(root_directory):
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

                        else:
                            print('no match found')

# Example usage
# root_directory = r'E:\AI\Extra\gitCheck\main\muzzles\destination_folder/'  # Replace with the actual path
root_directory = r'E:\AI\Extra\gitCheck\main\noseDist/'  # Replace with the actual path
template_path = r'E:\AI\Extra\gitCheck\main\noseDist\extra/co93_11.jpg'  # Replace with the actual path

match_pattern_in_folders(root_directory, template_path)
