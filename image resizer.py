import os
from PIL import Image

def process_images(input_folder, output_folder, target_size=2000, product_fill_ratio=0.85):
    """
    Process all images in the input folder to:
    - Resize them to fit a 2000x2000 square canvas
    - Ensure the product fills at least 85% of the frame
    - Save the processed images in the output folder

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder to save processed images.
        target_size (int): Target size for the square image (default: 2000).
        product_fill_ratio (float): The ratio of the product coverage (default: 0.85).
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".tiff")):
            file_path = os.path.join(input_folder, file_name)
            image = Image.open(file_path)

            # Calculate the scaled dimensions
            product_target_size = int(product_fill_ratio * target_size)
            scaled_width = int(image.size[0] * (product_target_size / max(image.size)))
            scaled_height = int(image.size[1] * (product_target_size / max(image.size)))
            resized_image = image.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)

            # Create a square canvas
            square_image = Image.new("RGB", (target_size, target_size), (255, 255, 255))
            square_image.paste(resized_image, ((target_size - scaled_width) // 2, (target_size - scaled_height) // 2))

            # Save the optimized image with "_v1" added to the name
            output_file_name = f"{os.path.splitext(file_name)[0]}_v1.jpg"
            output_file_path = os.path.join(output_folder, output_file_name)
            square_image.save(output_file_path, quality=100, subsampling=0)

if __name__ == "__main__":
    # Define input and output folders
    # input_folder = "path/to/your/input/folder"  # Replace with the path to your input folder
    # output_folder = "path/to/your/output/folder"  # Replace with the path to your output folder
    input_folder = "/Volumes/Media/Temp/Aaron/Accent-Products"  # Replace with the path to your input folder
    output_folder = "/Volumes/Media/Temp/Aaron/Accent-Products-V1"  # Replace with the path to your output folder

    # Run the processing function
    process_images(input_folder, output_folder)