import cv2
import numpy as np

def calculate_distance(point1, point2, pixel_to_distance_ratio):
    distance_pixels = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    distance_units = distance_pixels * pixel_to_distance_ratio
    return distance_units

def get_clicked_point(event, x, y, flags, param):
    global clicked_points, image_copy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        cv2.circle(image_copy, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('Image with Points', image_copy)
        
        if len(clicked_points) == 2:
            distance = calculate_distance(clicked_points[0], clicked_points[1], pixel_to_distance_ratio)
            print(f"The distance between the points is {distance} units")
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# Load the image
image = cv2.imread('E:/AI/newDataIslamabad/1post/test/dis5.png')
image_copy = image.copy()
clicked_points = []

# Define the known distance in the image for conversion
known_distance_pixels = 50  # Replace with the known distance in pixels
known_distance_units = 10    # Replace with the known distance in your desired unit

# pixel_to_distance_ratio = known_distance_units / known_distance_pixels
# Calculate the pixel-to-distance ratio in centimeters per pixel
pixel_to_distance_ratio = known_distance_units / known_distance_pixels

cv2.imshow('Image with Points', image)
cv2.setMouseCallback('Image with Points', get_clicked_point)

cv2.waitKey(0)
cv2.destroyAllWindows()
