import os
from PIL import Image

# where are the images?
old_folder = "C:\\Users\\sopsla\\Desktop\\session2a-image\\raw"  # path here

# make a new folder
new_folder = "C:\\Users\\sopsla\\Desktop\\test"  # path here
os.mkdir(new_folder)

# list all images in the old folder
img_list = os.listdir(old_folder)

# let's see what we have just done
print(img_list)

# save the images in the new folder
for img in img_list:
    img_path = os.path.join(old_folder, img)
    img_open = Image.open(img_path)       # why am I calling this "img_open" and not just "img"?
    img_open.save(os.path.join(new_folder, img))

# N.B. If you want to COPY a file, you can consider using the package Shutil.
