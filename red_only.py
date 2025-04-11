import image

# Create image from a file
file_name = "chapel.gif"
chapel = image.Image(file_name)

width = chapel.getWidth()
height = chapel.getHeight()

# Remove blue and green from the image
for col in range(width):
    for row in range(height):
        current_pixel = chapel.getPixel(col, row)  # get current pixel pos
        current_pixel.setBlue(0)
        current_pixel.setGreen(0)
        chapel.setPixel(col, row, current_pixel)

# Create a window
scr = image.ImageWin("Chapel Red", width=width, height=height)
chapel.draw(scr)
scr.exitOnClick()