
# # from PIL import Image

# # # Define the color ranges
# # color_ranges = {
# #     'Black': ((0, 0, 0), (85, 85, 85)),
# #     'Brown': ((86, 86, 86), (170, 170, 170)),
# #     'Pink': ((171, 171, 171), (255, 255, 255))
# # }

# # # Load the image
# # image_path = 'E:/AI/Extra/gitCheck/main/muz.jpg'  # Replace this with the path to your image
# # image = Image.open(image_path)
# # pixel_data = image.load()

# # # Function to check if a pixel falls within a specified range
# # def is_within_range(pixel, color_range):
# #     return all(color_range[0][i] <= pixel[i] <= color_range[1][i] for i in range(3))

# # # Count the number of pixels within each color range
# # color_counts = {color_name: 0 for color_name in color_ranges}

# # # Get width and height of the image
# # width, height = image.size

# # # Iterate through pixels and count the occurrence of each color
# # for y in range(height):
# #     for x in range(width):
# #         pixel = pixel_data[x, y]
# #         for color_name, rgb_range in color_ranges.items():
# #             if is_within_range(pixel, rgb_range):
# #                 color_counts[color_name] += 1
# #                 break  # No need to check other color ranges if this pixel matches one

# # # Find the dominant color(s)
# # dominant_colors = [color_name for color_name, count in color_counts.items() if count == max(color_counts.values())]

# # # Print the dominant color(s)
# # if len(dominant_colors) == 1:
# #     print(f"The image is primarily in {dominant_colors[0]} color.")
# # else:
# #     print(f"The image contains multiple dominant colors: {', '.join(dominant_colors)}")

# # ---------------------------------------------------------------------------------------------------


# # ---------------=============================================================-----------------------
# import numpy as np
# from PIL import Image
# from sklearn.cluster import KMeans

# # Load the image
# # image_path = 'E:/AI/Extra/gitCheck/main/c2_1.jpg'  # Replace this with the path to your image
# image_path = 'E:/AI/ProductionData/7cattles/c6/c6_17.jpg'
# image = Image.open(image_path)

# # Convert the image to a NumPy array
# img_array = np.array(image)

# # Flatten the array to fit the KMeans model
# reshaped_array = img_array.reshape(-1, 3)

# # Define the color ranges
# color_ranges = {
#     'Black': ((0, 0, 0), (85, 85, 85)),
#     'Brown': ((86, 86, 86), (170, 170, 170)),
#     'Pink': ((171, 171, 171), (255, 255, 255))
# }

# # Define the number of colors you want to detect with KMeans
# num_colors = 5  # Adjust this number as needed

# # Apply KMeans clustering to the image pixels
# kmeans = KMeans(n_clusters=num_colors, random_state=42)
# kmeans.fit(reshaped_array)

# # Retrieve the cluster centers (representative colors)
# kmeans_colors = kmeans.cluster_centers_.astype(int)

# # Initialize a set to hold detected color names
# detected_colors = set()

# # Map KMeans colors to defined color ranges and identify the colors found in the image
# for color in kmeans_colors:
#     for color_name, (lower, upper) in color_ranges.items():
#         if all(lower[i] <= color[i] <= upper[i] for i in range(3)):
#             detected_colors.add(color_name)
#             break

# # Print the colors found in the image within the specified ranges
# print("Colors found in the image within the specified ranges:")
# for color in detected_colors:
#     print(color)
# ==================================================================================================================



from PIL import Image
import numpy as np

# Load the image
image_path = 'E:/AI/Extra/gitCheck/main/muzzles/co94_1c.jpg'  # Replace this with the path to your image
image = Image.open(image_path)

# Convert the image to a NumPy array
img_array = np.array(image)

# Define the color ranges
color_ranges = {
    'Black': ((0, 0, 0), (95, 95, 95)),
    'Brown': ((96, 96, 96), (170, 170, 170)),
    'Pink': ((171, 171, 171), (255, 255, 255))
}

# Initialize counts for each color
color_counts = {color: 0 for color in color_ranges}

# Iterate through each pixel and count colors within ranges
for y in range(img_array.shape[0]):
    for x in range(img_array.shape[1]):
        pixel = img_array[y, x]
        for color, (lower, upper) in color_ranges.items():
            if all(lower[i] <= pixel[i] <= upper[i] for i in range(3)):
                color_counts[color] += 1
                break  # No need to check other color ranges if this pixel matches one

# Find the dominant color(s)
dominant_colors = [color for color, count in color_counts.items() if count == max(color_counts.values())]

# Print the dominant color(s)
if len(dominant_colors) == 1:
    print(f"The dominant color of the image is: {dominant_colors[0]}")
else:
    print(f"The dominant colors of the image are: {', '.join(dominant_colors)}")
