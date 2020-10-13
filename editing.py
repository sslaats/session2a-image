from PIL import Image
from PIL import ImageFilter
import os

# load an image
img_folder = "C:\\Users\\sopsla\\Desktop\\session2a-image\\raw"

img_path = os.path.join(img_folder, "bird.jpg")
img = Image.open(img_path)

# let's take a look at the properties of the image
print(img.size)
print(img.tile)

# cropping an image
# coordinates: (left upper / right lower)
reg = (0, 100, 200, 300)  # random square, in pixels
img_crop = img.crop(reg)
img_crop.show()

# now you can save this if you want
img_crop.save(os.path.join(img_folder, "test.png"))

# we could also flip it and paste it back
img_crop = img_crop.transpose(Image.ROTATE_180)
img.paste(img_crop, reg) # this directly edits the img variable!

# what if you wanted to crop the image such that it is the largest square it can be?
width = img.width
height = img.height

# to create a square
distance_from_center = min([width, height])/2
center = (width/2, height/2)

(left1, left2) = (number - distance_from_center for number in center)
(right1, right2) = (number + distance_from_center for number in center)

img_square = img.crop((left1, left2, right1, right2))
img_square.show()

# now this is a copy from a part of the image.
# we can edit it and paste it back.

# resizing the image
new_size = (100, 100)
img_rsz = img_square.resize(new_size)
print(img_rsz.size)
print(img_square.size)

# converting between modes: black & white
blw = img.convert("L")
blw.show()

# Applying filters
# pre-defined filters (find more on pillow.readthedocs.io/en/stable/reference/ImageFilter.html)
img_enh = img.filter(ImageFilter.EDGE_ENHANCE)

# Point transforms: can be used to translate the pixel values of an image. Recall that a bitmap
# image is basically an array. In this operation, each pixel is processed according to that function.
# It is also possible to do this per band (red/green/blue)

# multiply each pixel by 1.3
img_contrast = img.point(lambda i: i * 1.3)
img_contrast.show()
