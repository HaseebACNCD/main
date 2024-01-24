# # import cv2
# # import os

# # # Replace these paths with your source and destination folders
# # source_folder = r'E:\AI\restnet\DATA2/'
# # destination_folder = r'E:\AI\restnet\DATA3/'

# # # Ensure the destination folder exists, or create it if not
# # if not os.path.exists(destination_folder):
# #     os.makedirs(destination_folder)

# # # Loop through all the files in the source folder
# # for filename in os.listdir(source_folder):
# #     if filename.endswith(".jpg"):  # Assuming you're working with JPEG images
# #         # Construct the full path to the source image
# #         source_image_path = os.path.join(source_folder, filename)

# #         # Load the image
# #         image = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)

# #         # Apply median filter for noise removal
# #         image_filtered = cv2.medianBlur(image, 5)  # Adjust kernel size as needed

# #         # Perform Canny edge detection on the filtered image
# #         edges = cv2.Canny(image_filtered, threshold1=30, threshold2=70)

# #         # Construct the full path to the destination image
# #         # destination_image_path = os.path.join(destination_folder, filename)

# #         # Save the edge-detected image to the destination folder
# #         # cv2.imwrite(destination_image_path, edges)

# # print("Edge detection with noise removal complete. Edge-detected images are saved in:", destination_folder)








# # import cv2
# # import os
# # import matplotlib.pyplot as plt

# # # Replace these paths with your source and destination folders
# # source_folder = r'E:\AI\Extra\gitCheck\main\muzzles/'
# # destination_folder = r'E:\AI\Extra\gitCheck\main\muzzles/destination_folder/'

# # # Ensure the destination folder exists, or create it if not
# # if not os.path.exists(destination_folder):
# #     os.makedirs(destination_folder)

# # # Loop through all the files in the source folder
# # for filename in os.listdir(source_folder):
# #     if filename.endswith(".jpg"):  # Assuming you're working with JPEG images
# #         # Construct the full path to the source image
# #         source_image_path = os.path.join(source_folder, filename)

# #         # Load the image
# #         image = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)

# #         # Apply median filter for noise removal
# #         image_filtered = cv2.medianBlur(image, 5)  # Adjust kernel size as needed

# #         # Perform Canny edge detection on the filtered image
# #         edges = cv2.Canny(image_filtered, threshold1=5, threshold2=10)

# #         # Display the images using matplotlib
# #         plt.figure(figsize=(10, 5))

# #         plt.subplot(131), plt.imshow(image, cmap='gray')
# #         plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# #         plt.subplot(132), plt.imshow(image_filtered, cmap='gray')
# #         plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])

# #         plt.subplot(133), plt.imshow(edges, cmap='gray')
# #         plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])

# #         plt.show()

# # # print("Edge detection with noise removal complete. Edge-detected images are saved in:", destination_folder)
# # print("Edge detection with noise removal complete")



# import cv2
# import os
# import matplotlib.pyplot as plt

# # Replace these paths with your source and destination folders
# source_folder = r'E:\AI\Extra\gitCheck\main\muzzles/'
# destination_folder = r'E:\AI\Extra\gitCheck\main\muzzles/destination_folder/'

# # Ensure the destination folder exists, or create it if not
# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)

# # Loop through all the files in the source folder
# for filename in os.listdir(source_folder):
#     if filename.endswith(".jpg"):  # Assuming you're working with JPEG images
#         # Construct the full path to the source image
#         source_image_path = os.path.join(source_folder, filename)

#         # Load the image
#         image = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)

#         # Apply median filter for noise removal
#         image_filtered = cv2.medianBlur(image, 5)  # Adjust kernel size as needed

#         # Perform Canny edge detection on the filtered image
#         edges = cv2.Canny(image_filtered, threshold1=5, threshold2=10)

#         # Display the images using matplotlib
#         # plt.figure(figsize=(10, 5))

#         # plt.subplot(131), plt.imshow(image, cmap='gray')
#         # plt.title('Original Image'), plt.xticks([]), plt.yticks([])

#         # plt.subplot(132), plt.imshow(image_filtered, cmap='gray')
#         # plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])

#         # plt.subplot(133), plt.imshow(edges, cmap='gray')
#         # plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])

#         # plt.show()

#         # Construct the full path to the destination image
#         destination_image_path = os.path.join(destination_folder, filename)

#         # Save the edge-detected image to the destination folder
#         cv2.imwrite(destination_image_path, edges)

# print("Edge detection with noise removal complete. Edge-detected images are saved in:", destination_folder)


# ------------------only one image-----------------------



import cv2
import os
import matplotlib.pyplot as plt

# Replace these paths with your source and destination folders
# source_folder = r'E:\AI\Extra\gitCheck\main\muzzles/'
destination_folder = r'E:\AI\Extra\gitCheck\main\muzzles/destination_folder/'


# Specify the filename of the image you want to process
filename_to_process = 'your_image.jpg'  # Replace with the actual filename

# Construct the full path to the source image
# source_image_path = os.path.join(source_folder, filename_to_process)

# Load the image
image = cv2.imread(filename_to_process, cv2.IMREAD_GRAYSCALE)

# Apply median filter for noise removal
image_filtered = cv2.medianBlur(image, 5)  # Adjust kernel size as needed

# Perform Canny edge detection on the filtered image
edges = cv2.Canny(image_filtered, threshold1=5, threshold2=10)

# Display the images using matplotlib (optional)
# plt.figure(figsize=(10, 5))

# plt.subplot(131), plt.imshow(image, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(132), plt.imshow(image_filtered, cmap='gray')
# plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(133), plt.imshow(edges, cmap='gray')
# plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])

# plt.show()

# Construct the full path to the destination image
destination_image_path = os.path.join(destination_folder, filename_to_process)

# Save the edge-detected image to the destination folder
cv2.imwrite(destination_image_path, edges)

print("Edge detection with noise removal complete. Edge-detected image is saved in:", destination_folder)

