import image

# Load mario
file_name = "mario.gif"
mario = image.Image(file_name)

# Prompt
color_input = input(f'Please choose between the colors red, green, yellow, orange, or purple: ')

# Set RGB colors
red_pixel = image.Pixel(255, 0, 0)
green_pixel = image.Pixel(0, 255, 0)
blue_pixel = image.Pixel(0, 0, 255)
yellow_pixel = image.Pixel(255, 255, 0)
orange_pixel = image.Pixel(255, 128, 0)
purple_pixel = image.Pixel(140, 0, 191)

# Width and height
width = mario.getWidth()
height = mario.getHeight()

# for loop
for col in range(width):
    for row in range(height):

        current_pixel = mario.getPixel(col, row)
        red = current_pixel.getRed()
        green = current_pixel.getGreen()
        blue = current_pixel.getBlue()

        # Conditions
        if red > 254 and green < 1 and blue < 1:
            if color_input == "green":
                mario.setPixel(col, row, green_pixel)
            elif color_input == "blue":
                mario.setPixel(col, row, blue_pixel)
            elif color_input == "yellow":
                mario.setPixel(col, row, yellow_pixel)
            elif color_input == "purple":
                mario.setPixel(col, row, purple_pixel)
            else:
                mario.setPixel(col, row, red_pixel)


# Display the image on a window
win = image.ImageWin("Mario", width, height)
mario.draw(win)
win.exitOnClick()
