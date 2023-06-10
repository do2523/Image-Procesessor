from PIL import Image, ImageFilter

img = Image.open('./astro.jpg') # current size (5611, 5339)
img.thumbnail((400, 400)) # Match aspect ratio so picture still looks good with thumbnail
img.save("thumbnail.jpg")
print(img.size) # (400,381)