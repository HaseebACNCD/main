import math
import cv2
import os
import numpy as np
from flask import Flask, request, jsonify


app = Flask(__name__)



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
    # color_ranges = {
    #     'Black': ((0, 0, 0), (85, 85, 85)),
    #     'Brown': ((86, 86, 86), (170, 170, 170)),
    #     'Pink': ((171, 171, 171), (255, 255, 255))
    # }

    color_ranges = {
        'Black': ((0, 0, 0), (150, 150, 150)),
        # 'Brown': ((86, 86, 86), (170, 170, 170)),
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
            # print(closest_color)
    # print(f"The closest color to the rgb_color {rgb_color} is {closest_color}.")
    
    return closest_color



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



def match_template_in_folders(root_folder, destination_folder, color_result, threshold=0.85):
    matched_info=[]
    # Check if the color is in the colors dictionary
    if color_result is None or color_result not in colors:
        print(f"Error: Invalid or unknown color result.")
        return

    # Get the list of folders for the specified color
    folders_for_color = colors[color_result]

    # Get the template image path from the provided template folder path
    template_image_path = None
    for filename in os.listdir(destination_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
            template_image_path = os.path.join(destination_folder, filename)
            break

    if template_image_path is None:
        print(f"Error: No template image found in the provided template folder.")
        return

    # Read the template image
    template = cv2.imread(template_image_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"Error: Unable to read the template image.")
        return

    # Iterate through folders in the root directory
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        if os.path.isdir(folder_path) and folder_name in folders_for_color:
            # print(f"Processing folder: {folder_name}")

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
                        # print(f"Pattern matched in folder: {folder_name} (Image: {img_filename}, Match Percentage: {max_val * 100}%)")
                        match_info = {
                            "folder_name": folder_name,
                            "image_name": img_filename,
                            "match_percentage": max_val * 100
                        }
                        matched_info.append(match_info)
                        # print(match_info)

    return matched_info

# Dictionary of color patterns
colors = {
    "Black": ["co89", "co88", "co90", "co91", "co92", "co93"],
    # "Brown": ["co90", "co91", "co92"],
    "Pink": ["co94"]
}

def delete_data(folder_path):

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Iterate through the list and remove each file
    for file in files:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
        return 


@app.route('/match-template', methods=['GET', 'POST'])
def api_match_template():
    try:
        # Get image_path from the request (support both POST and GET methods)
        image_path = request.args.get('image_path') or request.json.get('image_path')

        # Specify the root_folder_path and destination_folder
        root_folder_path = "./muzzles/destination_folder"
        destination_folder = "./testfolder/"

        # Get the color result from color_detect
        color_to_search = color_detect(image_path)

        # Perform edge detection
        edge_image_path = edge_detect(image_path, destination_folder)

        # Call the function to match template in folders of the specified color result
        # match_template_in_folders(root_folder_path, destination_folder, color_to_search)
        matched_info = match_template_in_folders(root_folder_path, destination_folder, color_to_search)
        # Deleting data
        delete_data(destination_folder)

        # Check if there are matches before returning the response
        if matched_info:
            return jsonify({"matches": matched_info})
        else:
            return jsonify({"message": "No pattern matches found"})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)