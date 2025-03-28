 # File Bit Depth Checker and Copier

This Python script checks image files in a directory structure for 96-bit depth and copies matching files to a destination directory, organized by their parent folder names.

## Requirements

- Python 3.6+
- Pillow library

Install the required Pillow library:
```bash
pip install Pillow
```

## Usage

Run the script from the command line with two arguments:
1. Source directory (the directory to search for image files)
2. Destination directory (where to copy matching files)

```bash
python file_checker.py SOURCE_DIRECTORY DESTINATION_DIRECTORY
```

Example:
```bash
python file_checker.py D:\Photos D:\FilteredPhotos
```

## How It Works

The script will:
1. Recursively search through all subdirectories of the source directory
2. Identify image files with 96-bit depth
3. For each matching file, create a folder in the destination directory with the same name as the file's parent folder
4. Copy the file to the corresponding folder in the destination directory