from PIL import Image
import os

path = "D:/test/"
os.chdir("d:/test")
for file in os.listdir(path):
	if os.path.exists(file):
		img=Image.open(file)
		#print(img.size)
		if img.size[0]>img.size[1]:
			img.close()
			os.remove(file)
			print(file)
