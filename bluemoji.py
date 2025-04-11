import image

# Constants
width = 50
height = 50

# Create an empty image
img = image.EmptyImage(cols=width, rows=height)

# Create colored pixels
blue_pixel = image.Pixel(0, 0, 255)
black_pixel = image.Pixel(0, 0, 0)

# Fill image with blue pixels
for col in range(width):
    for row in range(height):
        img.setPixel(col, row, blue_pixel)

# Create two eyes using black pixels
for col in range(7, 20):
    for row in range(7, 20):
        img.setPixel(col, row, black_pixel)

for col in range(30, 43):
    for row in range(7, 20):
        img.setPixel(col, row, black_pixel)

# Create a mouth using black pixels
for col in range(7, 43):
    for row in range(37, 43):
        img.setPixel(col, row, black_pixel)

# Display the image on a window
window_title = "pixel head"
win = image.ImageWin(window_title, width, height)
img.draw(win)
win.exitOnClick()
