import image

# Create image from a file
file_name = "chapel.gif"
chapel = image.Image(file_name)

width = chapel.getWidth()
height = chapel.getHeight()

# Set gray scale
for col in range(width):
    for row in range(height):
        # get current pixel position
        current_pixel = chapel.getPixel(col, row)

        # Calculate average of RGB
        avg = int((current_pixel.getRed() + current_pixel.getGreen() + current_pixel.getBlue())/3)

        # Set RGB to avg value
        current_pixel.setRed(avg)
        current_pixel.setBlue(avg)
        current_pixel.setGreen(avg)

        # Set current image
        chapel.setPixel(col, row, current_pixel)

# Create a window
scr = image.ImageWin("Chapel Gray Tone", width=width, height=height)
chapel.draw(scr)
scr.exitOnClick()
