""""""

from PIL import Image

img = Image.open("./1.png").convert('RGB')
print(img.size)
cropped = img.crop((0, 0, 2544, 3056))  # (left, upper, right, lower)
cropped.save("./2.png")

