from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.EMBOSS) # You can look at the documentation for more types
filtered_img.save("emboss.png", "png")  



# filtered_img = img.convert("L")
# filtered_img.save("blacknwhite.png", "png")

# Creating new images from original
# img.filter(ImageFilter.SHARPEN) # You can look at the documentation for more types
# filtered_img = filtered_img.save("sharpen.png", "png")  

# A few Properties
# print(img.format)
# print(img.size)
# print(img.mode)

