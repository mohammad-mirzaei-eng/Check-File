import os
import shutil
from PIL import Image
import argparse

def get_bit_depth(file_path):
    """Get the bit depth of an image file."""
    try:
        with Image.open(file_path) as img:
            # Check the bit depth based on image mode and bit depth
            if img.mode == 'RGB' and getattr(img, 'bits', 8) == 32:
                return 96  # RGB with 32 bits per channel = 96 bit depth
            elif img.mode == 'RGBA' and getattr(img, 'bits', 8) == 24:
                return 96  # RGBA with 24 bits per channel = 96 bit depth
            elif hasattr(img, 'bit_depth'):
                return img.bit_depth
            else:
                # Common bit depths per channel based on mode
                mode_to_bits = {
                    '1': 1,     # 1-bit per pixel
                    'L': 8,     # 8-bit grayscale
                    'P': 8,     # 8-bit palette
                    'RGB': 24,  # 3x8-bit RGB
                    'RGBA': 32, # 4x8-bit RGBA
                    'CMYK': 32, # 4x8-bit CMYK
                    'YCbCr': 24,# 3x8-bit YCbCr
                    'I': 32,    # 32-bit integer
                    'F': 32,    # 32-bit float
                }
                return mode_to_bits.get(img.mode, 0)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def process_files(source_dir, dest_dir):
    """
    Process files in source_dir and its subdirectories.
    Copy files with bit depth 96 to dest_dir in a folder named after their parent folder.
    """
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
            
            # Check bit depth
            bit_depth = get_bit_depth(file_path)
            
            if bit_depth == 96:
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
    
    print(f"Finished processing. Copied {processed_count} files with 96-bit depth.")

def main():
    # Setup command line arguments
    parser = argparse.ArgumentParser(description='Copy files with 96-bit depth to specified destination.')
    parser.add_argument('source_dir', help='Source directory to search for files')
    parser.add_argument('dest_dir', help='Destination directory to copy files to')
    
    args = parser.parse_args()
    
    # Process files
    process_files(args.source_dir, args.dest_dir)

if __name__ == "__main__":
    main()