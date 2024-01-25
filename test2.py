import math
import cv2
import os
import numpy as np



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




# 
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

        print("Edge detection complete. Edge-detected image is saved in:", destination_folder)
        return destination_image_path

    except Exception as e:
        print(f"Error: {e}")
        return None

image_path = 'E:/AI/Extra/gitCheck/main/muzzles/co88_1c.jpg'
destination_folder = r'E:\AI\Extra\gitCheck\main\destination_folder/'
color_result = color_detect(image_path)
edge_detected = edge_detect(image_path,destination_folder)



# import math
# import cv2
# import os
# import numpy as np

# def color_detect(image_path):
#     try:
#         # Load the image
#         image = cv2.imread(image_path)

#         if image is None:
#             raise Exception(f"Error: Unable to read the image at '{image_path}'")

#         # Rest of your code...
#         return print("Color detection complete")

#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# def edge_detect(image_path):
#     try:
#         destination_folder = r'E:\AI\Extra\gitCheck\main\destination_folder/'

#         # Load the image
#         image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#         if image is None:
#             raise Exception(f"Error: Unable to read the image at '{image_path}'")

#         # Rest of your edge detection code...

#         # Construct the full path to the destination image
#         destination_image_path = os.path.join(destination_folder, os.path.basename(image_path))

#         # Save the edge-detected image to the destination folder
#         cv2.imwrite(destination_image_path, edges)

#         print("Edge detection complete. Edge-detected image is saved in:", destination_folder)
#         return destination_image_path

#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# image_path = 'E:/AI/Extra/gitCheck/main/muzzles/co88_3c.jpg'
# color_result = color_detect(image_path)

# if color_result is not None:
#     edge_result = edge_detect(image_path)
#     if edge_result is not None:
#         print(f"Edge-detected image saved at: {edge_result}")
