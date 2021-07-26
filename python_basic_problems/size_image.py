# Python Program to Find the Size (Resolution) of a Image

from PIL import Image

image = Image.open("images/rocket.png")
print(image.size)
