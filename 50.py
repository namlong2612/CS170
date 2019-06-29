from PIL import Image

im = Image.open("tower.jpg")
(w, h) = im.size
photo = im.copy()



for y in range(h):
    for x in range (w):
        pixel = photo.getpixel((x,y))
        (r,g,b) = pixel
        newPixel = (r + 100, g, b)
        photo.putpixel((x,y), newPixel)

photo.save("tower1.jpg")
photo.show()


for y in range(h):
    for x in range (w):
        pixel = photo.getpixel((x,y))
        (r,g,b) = pixel
        newPixel = (r - 100, g+100, b-100)
        photo.putpixel((x,y), newPixel)

photo.save("tower2.jpg")
photo.show()


for y in range(h):
    for x in range (w):
        pixel = photo.getpixel((x,y))
        (r,g,b) = pixel
        newPixel = (r - 100, g-250, b)
        photo.putpixel((x,y), newPixel)

photo.save("tower3.jpg")
photo.show()
