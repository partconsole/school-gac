import image

# Create image from a file
file_name = "chapel.gif"
chapel = image.Image(file_name)

# Constants
width = chapel.getWidth()
height = chapel.getHeight()

# Create an empty image
img = image.EmptyImage(cols=width, rows=height)

# FLIP
for col in range(width):
    for row in range(height):
        current_pixel = chapel.getPixel(col, row)
        img.setPixel(col, height - row - 1, current_pixel)

# Display the image on a window
win = image.ImageWin("Flipped", width, height)
img.draw(win)
win.exitOnClick()
