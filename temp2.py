# import cv2
# import os
# from skimage.metrics import structural_similarity as ssim

# def calculate_ssim(image1, image2):
#     # Convert the images to grayscale if they are not already
#     if len(image1.shape) == 3:
#         image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#     if len(image2.shape) == 3:
#         image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

#     # Resize images to the same dimensions (optional)
#     # image1 = cv2.resize(image1, (width, height))
#     # image2 = cv2.resize(image2, (width, height))

#     # Ensure the images have the same size
#     min_height = min(image1.shape[0], image2.shape[0])
#     min_width = min(image1.shape[1], image2.shape[1])

#     image1 = image1[:min_height, :min_width]
#     image2 = image2[:min_height, :min_width]

#     # Calculate the SSIM
#     similarity_index = ssim(image1, image2)

#     return similarity_index

# def process_folder(folder_path):
#     # Get a list of all files in the folder
#     files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

#     # Dictionary to store similarity indices for each pair
#     similarity_indices = {}

#     for i in range(len(files)):
#         template_image_path = os.path.join(folder_path, files[i])

#         # Skip non-image files
#         if not template_image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
#             continue

#         template_image = cv2.imread(template_image_path)
#         template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

#         for j in range(i + 1, len(files)):
#             query_image_path = os.path.join(folder_path, files[j])

#             # Skip non-image files
#             if not query_image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
#                 continue

#             query_image = cv2.imread(query_image_path)
#             query_image = cv2.cvtColor(query_image, cv2.COLOR_BGR2GRAY)

#             similarity_index = calculate_ssim(template_image, query_image)
#             print(f"Similarity index between {files[i]} and {files[j]}: {similarity_index}")

#             # Store the similarity index in the dictionary
#             pair_key = f"{files[i]} - {files[j]}"
#             similarity_indices[pair_key] = similarity_index

#     return similarity_indices

# if __name__ == "__main__":
#     folder_path = r"E:\AI\Extra\gitCheck\main\noseDist/"
#     similarity_indices = process_folder(folder_path)

#     # Print overall similarity indices
#     print("\nOverall similarity indices:")
#     for pair, similarity_index in similarity_indices.items():
#         print(f"{pair}: {similarity_index}")



import cv2
import os
import numpy as np

# pattern matching algorithm
def match_pattern_in_folder(folder_path, template_path, threshold=0.85):
    # Read the template
    template = cv2.imread(template_path)

    if template is None:
        print("Error: Unable to read the template image.")
        return None

    # Convert the template to grayscale
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # List to store matched image paths
    matched_images = []

    # Iterate through images in the specified folder
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

                # If match is found above the threshold, store the matched image path
                if max_val >= threshold:
                    matched_images.append(image_path)
                    print(f"Pattern matched in folder: {folder_path} (Image: {filename}, Match Percentage: {max_val * 100}%)")

    # Return the list of matched image paths
    return matched_images

# Example usage
folder_path = r'E:\AI\Extra\gitCheck\main\muzzles\destination_folder/'
template_path = r'E:\AI\Extra\gitCheck\main\testfolder/'
matched_images = match_pattern_in_folder(folder_path, template_path)

# Print the matched image paths
print("Matched Image Paths:")
for img_path in matched_images:
    print(img_path)
