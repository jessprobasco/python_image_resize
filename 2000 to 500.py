import os
from PIL import Image, UnidentifiedImageError

def resize_images(input_folder, output_folder, target_size=500):
    """
    Resize all 2000x2000 images in the input folder to 500x500 and save them in the output folder
    with '_v1' replaced by '_500' in the file name.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder to save resized images.
        target_size (int): Target size for the square image (default: 500).
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".tiff")) and "_v1" in file_name:
            file_path = os.path.join(input_folder, file_name)
            try:
                image = Image.open(file_path)

                if image.size == (2000, 2000):
                    resized_image = image.resize((target_size, target_size), Image.Resampling.LANCZOS)

                    # Replace '_v1' with '_500' in the file name
                    output_file_name = file_name.replace("_v1", "_500")
                    output_file_path = os.path.join(output_folder, output_file_name)
                    resized_image.save(output_file_path, quality=100, subsampling=0)
            except UnidentifiedImageError:
                print(f"Error: Cannot identify image file {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    # Define input and output folders
    input_folder = "/Volumes/Media/Temp/Aaron/Accent-Products-2000"  # Replace with the path to your input folder
    output_folder = "/Volumes/Media/Temp/Aaron/Accent-Products-500"  # Replace with the path to your output folder

    # Run the resizing function
    resize_images(input_folder, output_folder)