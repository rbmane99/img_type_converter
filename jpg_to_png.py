import sys
import os

from PIL import Image,ImageFilter

# grab first and second argument
img_folder=sys.argv[1]
output_folder=sys.argv[2]




# check is new folder exits ,if not create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)


# loop through img,
# list dir gives the list in folder
for filename in os.listdir(img_folder):
	img=Image.open(f"{img_folder}{filename}")
	# SPLITEXT=('itsMe','.jpg)filename[0]means only itsMe and not extension)
	clean_name=os.path.splitext(filename)[0]
	# save with extension png
	img.save(f"{output_folder}/{clean_name}.png",'png')
print("all doneeeee!!!!")


# now reize all images to the same size
# we have created the new folder with jpg converted to png files in output folder aka new in our case
for filename in os.listdir(output_folder):
	img_crop=Image.open(f"{output_folder}{filename}")
	# resize images
	img_crop.thumbnail((400,400))
	img_crop=img_crop.filter(ImageFilter.SHARPEN)

	img_crop.save(f"{output_folder}{filename}")
print("done")





# conver images to png
# save to the new folder