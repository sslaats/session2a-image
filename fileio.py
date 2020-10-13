import os
from PIL import Image

# Use the os module. Works for UNIX, Windows, MacOs...
# e.g, to get working directory
os.getcwd()

# where are the images?
old_folder = "C:\\Users\\sopsla\\Desktop\\session2a-image\\raw"

# load an image from file
img_path = os.path.join(old_folder, "bird.jpg")
img = Image.open(img_path)

# because of using 'Image', the variable 'img' is now of class 'Image'.
# what a class is, we will discuss later. For now, it is only necessary to know
# that a class has ATTRIBUTES. 'Image' has attributes like 'format', 'size', and 'mode'.
# Let's see what that means.
print(img.size)

# If you want to access all of them in one line
# Size: size in pixels
# Format: is it JPEG, PNG, ...?
# Mode: depth of a pixel. E.g. 1 (1-bit pixel, black & white); RGB (3x8 pixels, true color)
print(img.size, img.format, img.mode)

# important to know is that "size" is of dta type "tuple". A tuple is like a list, but it cannot be changed.
# you can access the elements in the tuple in the same way as you would in a list.
# you can use a

# display the image
img.show()

# save the image to a new file extension: PNG to JPG
# first: split the extension and the name using os.path.splitext
# N.B.: the function os.path.split() splits the path to the folder from the filename.
filename, extension = os.path.splitext(img_path)

# now we're generating the filename with .jpg extension
outfile = filename + ".png"

# save the file
img.save(outfile, "PNG")

# note that you can also change the name and save the file again.
new_img_path = os.path.join(img_path, "a_Python_will_eat_this_bird.png")
img.save(new_img_path)

# delete the files again
os.remove(outfile + ".png")
os.remove(new_img_path)

# now let's save an image to a new folder
# make a new folder
new_folder = "C:\\Users\\sopsla\\Desktop\\session2a-image\\tmp"
os.mkdir(new_folder)

# save the file
img.save(os.path.join(new_folder, "copy.jpg"))

# this demonstrates that everything you do to the image in Python, is done to the data loaded onto the variable
# in Python. Only when you save it, it will become part of the actual file.

# how to get all files in a folder? os.listdir
print(os.listdir(old_folder))

# EXERCISE: COPY ALL THE FILES TO THE NEW FOLDER
