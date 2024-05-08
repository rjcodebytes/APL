from PIL import Image 

img=Image.open("cap.jpg")

img.show()

width, height=img.size

print (width, height)

print (img.format) 

print (img.info)

img1=img.save("abc.png")

img2=img.rotate (90)

img2.show()

size=(250,250,750, 750) 

img3=img.crop(size) 

img3=img.show()

RE_SIZE=(300,300)

img4=img.resize (RE_SIZE) 

img4.show()
