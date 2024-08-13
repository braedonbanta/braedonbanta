import os
from PIL import Image

# Define the directory containing the PNG images
input_dir = "C:/Users/bbant/Downloads/new samples"
output_dir = "C:/Users/bbant/Downloads/converted samples"

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created output directory: {output_dir}")
else:
    print(f"Output directory already exists: {output_dir}")

# Set JPEG quality (0-95, where higher is better quality and lower is more compression)
jpeg_quality = 95  # Adjust this value as needed

# Set the amounts to exclude from each side after centering on the left half
exclude_top = 300  # Adjust this value as needed
exclude_bottom = 250 # Adjust this value as needed
exclude_left = 700  # Adjust this value as needed
exclude_right = 400  # Adjust this value as needed


def crop_exclude(img, exclude_top, exclude_bottom, exclude_left, exclude_right):
    """Crop the image to exclude specified amounts from top, bottom, left, and right."""
    img_width, img_height = img.size
    # Center on the left half
    crop_left = 0
    crop_top = 0
    crop_right = img_width // 2
    crop_bottom = img_height

    # Apply additional cropping
    crop_left = max(crop_left + exclude_left, 0)
    crop_top = max(crop_top + exclude_top, 0)
    crop_right = min(crop_right - exclude_right, img_width // 2)
    crop_bottom = min(crop_bottom - exclude_bottom, img_height)

    return img.crop((crop_left, crop_top, crop_right, crop_bottom))



# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        print(f"Processing file: {filename}")
        # Open the image file
        img = Image.open(os.path.join(input_dir, filename))
        # Convert image to RGB (PNG might be RGBA)
        rgb_img = img.convert('RGB')

        # Crop the image excluding specified amounts from each side after centering on the left half
        cropped_img = crop_exclude(rgb_img, exclude_top, exclude_bottom, exclude_left, exclude_right)

        # Save the image in JPG format in the output directory with compression
        output_filename = os.path.splitext(filename)[0] + ".jpg"
        cropped_img.save(os.path.join(output_dir, output_filename), format="JPEG", quality=jpeg_quality)
        print(f"Saved file as: {output_filename} with quality {jpeg_quality}")

print("Conversion, cropping, and compression completed!")