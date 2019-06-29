from PIL import Image

def yellowPassFilter(pic):
    im = pic.copy()
    width, height = pic.size
    for x in range(width):
        for y in range(height):
            pix = pic.getpixel((x,y))
            (r,g,b) = pix
            newR = r
            newG = g
            newB = 0
            newPixel = ( newR, newG, newB)
            im.putpixel((x,y), newPixel)
    return im

nam = Image.open("vanpersie.jpg")
pf = yellowPassFilter(nam)
pf.show()
pf.save("yellowpassfilter.jpg")




def yellowBlockFilter(pic):
    im = pic.copy()
    width, height = pic.size
    for x in range(width):
        for y in range(height):
            pix = pic. getpixel((x,y))
            (r,g,b) = pix
            newR = 0
            newG = 0
            newB = b
            newPixel = (newR, newG, newB)
            im.putpixel((x,y), newPixel)
    return im

long = Image.open("vanpersie.jpg")
bf = yellowBlockFilter(long)
bf.show()
bf.save("yellowblockfilter.jpg")


