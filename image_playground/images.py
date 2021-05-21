from PIL import Image, ImageFilter

img = Image.open('./image_playground/pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
filtered_img.save("grey.png", "png")
filtered_img.show()