from PIL import Image
from PIL import ImageFilter
import os

# Assignment:
# Create a new folder called "processed" where all images from "raw" are stored in .png.
# They are all cropped to ratio 4:3 (or 3:4) and resized to be all the same size.

# Notice:
# 1. There are different extensions
# 2. They are all different sizes
# 3. We have portrait and landscape orientated images

# Steps
# 0. Create a new folder
# 1. Define portrait and landscape images
# 2. Figure out on which side you have to crop the image
# 3. Crop the image
# 4. Resize the image
# 5. Save it to your new folder with the new extension. That's it!
