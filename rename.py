import os


def rename_images(input_folder):
    """
    Rename image files in the input folder by replacing '_v1' with '_2000' in the file name.

    Args:
        input_folder (str): Path to the folder containing input images.
    """
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".tiff")) and "_v1" in file_name:
            old_file_path = os.path.join(input_folder, file_name)
            new_file_name = file_name.replace("_v1", "_2000")
            new_file_path = os.path.join(input_folder, new_file_name)

            if os.path.exists(old_file_path):
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} to {new_file_path}")
            else:
                print(f"File not found: {old_file_path}")


if __name__ == "__main__":
    # Define input folder
    input_folder = "/Volumes/Media/Temp/Aaron/Accent-Products-2000"  # Replace with the path to your input folder

    # Run the renaming function
    rename_images(input_folder)