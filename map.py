import os
import shutil

def copy_txt_files_with_structure(source_dir, target_dir):
    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file is a .txt file
            if file.endswith('.txt'):
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Create a subfolder structure in the target directory
                relative_path = os.path.relpath(root, source_dir)
                target_subfolder = os.path.join(target_dir, relative_path)
                if not os.path.exists(target_subfolder):
                    os.makedirs(target_subfolder)
                # Copy file to the corresponding subfolder in the target directory
                shutil.copy(file_path, target_subfolder)

# Example usage
source_directory = 'Oulu/Dev_files'
target_directory = '/home/yangliu/Documents/CDCN/Oulu/IJCB_re/OULUdev_images'
copy_txt_files_with_structure(source_directory, target_directory)
