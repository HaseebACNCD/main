import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'E:/AI/Extra/gitCheck/main/muzzles/co94_1c.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(image, 50, 150)  # You can adjust the threshold values (50 and 150 in this example)

# Display the original and edge-detected images
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])

plt.show()
