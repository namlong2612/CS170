from PIL import Image

#pre: factor > 0

def scalePixel(pix, factor1, factor2, factor3):
    (r,g,b) = pix
    newPixel = (min(255,int(factor1 * r)),
                min(255,int(factor2 * g)),
                min(255,int(factor3 * b) ))
    return newPixel


#pre: factor > 0

def modifyPixel(pic, pixelFunction, factor1, factor2, factor3): 
    im = pic.copy() 
    (width, height) = pic.size 
    for x in range(width): 
        for y in range(height):
            pix = pic.getpixel((x,y)) 
            newPixel = pixelFunction(pix, factor1, factor2, factor3) 
            im.putpixel((x,y),newPixel) 
    return im 



im = Image.open("degea.jpg")
im = modifyPixel(im, scalePixel, 0.1, 0.1, 2.5)
im.show()
im.save("degea1.jpg")


im = Image.open("degea.jpg")
im = modifyPixel(im, scalePixel, 1.6, 4.3, 3)
im.show()
im.save("degea2.jpg")


im = Image.open("degea.jpg")
im = modifyPixel(im, scalePixel, 2.1, 0.8, 2)
im.show()
im.save("degea3.jpg")
