## Image Conversion Script

This script converts images in a specified directory to PNG format and saves them in a new directory. The script utilizes the `PIL` library for image manipulation.

### Prerequisites
- Python 3.x
- `PIL` library (`pip install pillow`)

### Usage
1. Make sure you have the required dependencies installed.
2. Run the script with the following command:
   ```
   python script.py [dir1] [dir2]
   ```
   Replace `[dir1]` with the path to the directory containing the images you want to convert, and `[dir2]` with the path to the directory where you want to save the converted images.

### Example
```
python script.py ./original_images/ ./converted_images/
```

### Details
1. Import necessary modules:
   ```python
   import sys
   import os
   from PIL import Image
   ```

2. Retrieve the source and destination directories from command-line arguments:
   ```python
   dir1 = sys.argv[1]
   dir2 = sys.argv[2]
   ```

3. Create the destination directory if it doesn't exist:
   ```python
   if not os.path.exists(dir2):
       os.makedirs(dir2)
   ```

4. Loop through the images in the source directory and convert them to PNG:
   ```python
   for filename in os.listdir(dir1):
       img = Image.open(f'{dir1}{filename}')
       tempTuple = os.path.splitext(filename)
       img.save(f'{dir2}{tempTuple[0]}.png', 'png')
       print("Done")
   ```

5. (Optional) Check if a file named `info.txt` exists in the current directory:
   ```python
   if os.path.exists("./info.txt"):
       print("True")
   else:
       print("False")
   ```

Note: The code related to checking the existence of `info.txt` file is currently commented out. If you want to use it, uncomment the relevant lines.

**Note**: Ensure that the script and the directories specified as arguments exist and have the necessary permissions for reading and writing files.
