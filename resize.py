from PIL import Image
import os, sys

def resize(img,filename, target_width, target_height):
	'''
	Resize PIL image keeping ratio and using white background.
	'''
	im = Image.open(img)
	target_ratio = target_height / target_width
	im_ratio = im.height / im.width
	if target_ratio > im_ratio:
		# It must be fixed by width
		resize_width = target_width
		resize_height = round(resize_width * im_ratio)
	else:
		# Fixed by height
		resize_height = target_height
		resize_width = round(resize_height / im_ratio)

	image_resize = im.resize((resize_width, resize_height), Image.ANTIALIAS)
	background = Image.new('RGB', (target_width, target_height), (255, 255, 255, 255))
	offset = (round((target_width - resize_width) / 2), round((target_height - resize_height) / 2))
	background.paste(image_resize, offset)	
	background.save(directory2 + filename, 'JPEG', quality=90)


directory = r'/home/user/dir/'
directory2 = r'/home/user/dir2/'
for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		resize(directory+filename,filename,1280,720)
		print(directory+filename)
	else:
		print(filename+" error")
		continue
	
