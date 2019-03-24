from PIL import Image
import glob
import os

images_list = glob.glob('data/*/*/*')
print(len(images_list))

for fn in images_list :
    try:
        Image.open(fn)
    except:
        os.remove(fn)
        print(fn)
