
import cv2
import webcolors
import numpy as np

# Load the image
image = cv2.imread('E:/AI/Extra/gitCheck/main/dis1_1.png')

# Define the coordinates of the pixel you want to sample
x, y = 80, 140

# Get the BGR color of the specified pixel
pixel_color = image[y, x]

# Convert BGR to RGB
rgb_color = (pixel_color[2], pixel_color[1], pixel_color[0])

# Function to find the closest predefined color
def find_nearest_color(rgb_val):
    min_distance = float('inf')
    closest_color = None
    for color_name, color_rgb in webcolors.CSS3_NAMES_TO_HEX.items():
        # Convert predefined color RGB to numpy array for calculations
        predefined_rgb = np.array(webcolors.hex_to_rgb(color_rgb))
        # Calculate Euclidean distance between provided RGB and predefined color
        distance = np.linalg.norm(np.array(rgb_val) - predefined_rgb)
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name
    return closest_color

# Get the nearest predefined color name
nearest_color = find_nearest_color(rgb_color)

# Mark the spot on the image
marked_image = image.copy()
cv2.circle(marked_image, (x, y), 5, (0, 255, 0), -1)  # Draw a green circle at the pixel location

# Display the marked image
cv2.imshow('Image with Marked Pixel', marked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Display the nearest color name
print(f"Nearest predefined color for pixel at ({x}, {y}): {nearest_color}")