from PIL import Image

test = Image.open("mueller.jpg") 
print(test.size)
(width, height) = test.size
testCopy = test.copy()

for verticalPixel in range(height):
    for horizontalPixel in range(width):
        pixel = testCopy.getpixel((horizontalPixel, verticalPixel))
        (r, g, b) = pixel
        newPixel = (b, r, g) 
        testCopy.putpixel((horizontalPixel,verticalPixel), newPixel)

testCopy.save("muller.jpg") 
testCopy.show()
