import board
import displayio
from adafruit_st7789 import ST7789
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon

displayio.release_displays()


grassColor = 0x008A2E
orange = 0xD38226
white = 0xFFFFFF
black = 0x000000
backgroundCol = 0x79FFEE
insideColor = 0xE26C10
red = 0xFF0000
brown = 0x753707

# Establish SPI interface
spi = board.SPI()
tft_cs = board.D5  # this is the CS pin you chose on the board
tft_dc = board.D6 # this is the DC pin you chose on the board
disp_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(disp_bus, rotation=270, width=240, height=135, rowstart=40,    colstart=53)  # this line and the one above is just a single line of code

my_group = displayio.Group()
display.show(my_group)  # clear the screen
my_bitmap = displayio.Bitmap(240, 135, 1) # width and height are your choice
my_palette = displayio.Palette(1) # number of palette colors
my_palette[0] = white # assign colors to palette list
my_tile_grid = displayio.TileGrid(my_bitmap, x=0, y=0, pixel_shader=my_palette)
my_group.append(my_tile_grid)  # updates the display with the new objects


#color outside of while true
grass = RoundRect(0, 68, 240, 67, 0, fill = grassColor, outline = None, stroke = 2)
pumpkin = Circle(120, 68, 50, fill = orange, outline = None, stroke = 2)
shadow = Circle(100, 68, 50, fill = black, outline = None, stroke = 2)
sky = RoundRect(0, 0, 240, 68, 0, fill = backgroundCol, outline = None, stroke = 2)
my_group.append(grass)
my_group.append(shadow)
my_group.append(sky)
my_group.append(pumpkin)

mouth = Circle(120, 75, 30, fill = insideColor, outline = None, stroke = 2)
mouthCover = RoundRect(90, 45, 70, 30, 0, fill = orange, outline = None, stroke = 2)
my_group.append(mouth)
my_group.append(mouthCover)

eye1 = Triangle(90, 63, 100, 45, 120, 63, fill = insideColor, outline = None)
my_group.append(eye1)
eye2 = Triangle(130, 63, 150, 45, 160, 63, fill = insideColor, outline = None)
my_group.append(eye2)

stem = RoundRect(115, 5, 10, 20, 1, fill = brown, outline = None, stroke = 2)
my_group.append(stem)



while True:
    pass
