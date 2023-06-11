import sys
import os  # alternative would be the pathlib module
from PIL import Image

# Grab first and second argument
dir1 = sys.argv[1]
dir2 = sys.argv[2]

# Check if new\ exists if not then create it
if not os.path.exists(dir2):
    os.makedirs(dir2)

# Loop through Pokedex and convert images to png
for filename in os.listdir(dir1):
    img = Image.open(f'{dir1}{filename}')
    tempTuple = os.path.splitext(filename)
    img.save(f'{dir2}{tempTuple[0]}.png', 'png')
    print("Done")

# Save to the new folder
# try:
#     if os.path.exists("./info.txt"):
#         print("True")
# except:
#     print("false")