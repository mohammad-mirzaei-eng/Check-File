import os
import shutil
from PIL import Image
import argparse

def check_resolution(file_path):
    """Check if an image file has both horizontal and vertical resolution of 96 DPI."""
    try:
        with Image.open(file_path) as img:
            # Get DPI information
            if 'dpi' in img.info:
                dpi = img.info['dpi']
                horizontal_dpi, vertical_dpi = dpi
                print(f"File: {file_path} - Resolution: {horizontal_dpi}x{vertical_dpi} DPI")
                # Check if both horizontal and vertical resolution are 96 DPI
                return horizontal_dpi == 72 and vertical_dpi == 72
            else:
                print(f"No DPI information found for {file_path}")
                return False
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def process_files():
    """
    Process files in source_dir and its subdirectories.
    Copy files with 96 DPI resolution (both horizontal and vertical) 
    to dest_dir in a folder named after their parent folder.
    """
    source_dir="D:\\image"
    dest_dir="D:\\test\\Image"
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Keep track of processed files
    processed_count = 0
    
    # Walk through all directories and files in source_dir
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip files that aren't images
            if not file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                continue
            
            # Check resolution
            if check_resolution(file_path):
                # Get parent folder name
                parent_folder = os.path.basename(root)
                
                # Create destination folder if it doesn't exist
                dest_folder = os.path.join(dest_dir, parent_folder)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                # Copy file to destination
                dest_file = os.path.join(dest_folder, file)
                shutil.copy2(file_path, dest_file)
                
                print(f"Copied {file_path} to {dest_file}")
                processed_count += 1
    
    print(f"Finished processing. Copied {processed_count} files with 96 DPI resolution.")

def main():
    # Setup command line arguments
    #parser = argparse.ArgumentParser(description='Copy files with 96-bit depth to specified destination.')
    #parser.add_argument('source_dir', help='Source directory to search for files')
    #parser.add_argument('dest_dir', help='Destination directory to copy files to')
    
    #args = parser.parse_args()
    
    # Process files
    process_files()
    #process_files(args.source_dir, args.dest_dir)

if __name__ == "__main__":
    main()
