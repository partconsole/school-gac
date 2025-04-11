import image

# Create image from a file
file_name = "chapel.gif"
chapel = image.Image(file_name)

width = chapel.getWidth()
height = chapel.getHeight()


# Set sepia
for col in range(width):
    for row in range(height):
        current_pixel = chapel.getPixel(col, row)

        red = current_pixel.getRed()
        green = current_pixel.getGreen()
        blue = current_pixel.getBlue()

        new_red = int((red * .393) + (green * .769) + (blue * .189))
        if new_red > 255:
            new_red = 255
        new_green = int((red * .349) + (green * .686) + (blue * .168))
        if new_green > 255:
            new_green = 255
        new_blue = int((red * .272) + (green * .534) + (blue * .131))
        if new_blue > 255:
            new_blue = 255

#
        current_pixel.setRed(new_red)
        current_pixel.setBlue(new_blue)
        current_pixel.setGreen(new_green)

        chapel.setPixel(col, row, current_pixel)


# Create a window
scr = image.ImageWin("Chapel Sepia", width=width, height=height)
chapel.draw(scr)
scr.exitOnClick()
