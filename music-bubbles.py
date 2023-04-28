from PIL import Image, ImageDraw

# Landscape A4 aspect ratio
WIDTH = 1782
HEIGHT = 1260

# Title area at 1/6 of the page
TITLE_AREA = (0, 0, WIDTH, int(HEIGHT/6))

# Two lines for music bubbles at 5/12 each
TOP_LINE = (0, int(HEIGHT/6), WIDTH, int(HEIGHT*5/12) + int(HEIGHT/6))
BOTTOM_LINE = (0, int(HEIGHT*5/12) + int(HEIGHT/6), WIDTH, HEIGHT)

partition = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(partition)
draw.rectangle(TITLE_AREA, outline="blue", width=8)
draw.rectangle(TOP_LINE, outline="green", width=8)
draw.rectangle(BOTTOM_LINE, outline="purple", width=8)

partition.show()
