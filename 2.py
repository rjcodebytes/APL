from PIL import Image

import matplotlib.pyplot as plt

img1=Image.open("cap.jpg")

img2=Image.open("rengoku1.jpeg")

img1.paste(img2,(200,250))

img1.show()

histogram=img1.histogram()

plt.hist(histogram,bins=len(histogram))

plt.xlabel("histogram")

plt.show()

transposed_img=img2.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.show()

red,green,blue=img1.split()

zero=red.point(lambda _:0)

red=Image.merge("RGB",(red,zero,zero))

green=Image.merge("RGB",(zero,green,zero))

blue=Image.merge("RGB",(zero,zero,blue))

red.show()

green.show()

blue.show()
img1.save ("new_img.bmp")
MAX_SIZE=(100,100)
img2.thumbnail(MAX_SIZE)
img2.save("thumbnail.png")
