from PIL import Image, ImageDraw
from dataclasses import dataclass

@dataclass
class Note:
    colour: str
    pos: int

NOTES = {
    "c": Note("#ee0000", 1),
    "d": Note("#ff860d", 2),
    "e": Note("#ffff38", 3),
    "f": Note("#069a2e", 4),
    "g": Note("#0000ee", 5),
    "a": Note("#e84473", 6),
    "b": Note("#000060", 7),
    "R": Note("#00000000", 0), # rest
}

# Landscape A4 aspect ratio
WIDTH = 1782
HEIGHT = 1260

# Title area at 1/8 of page height
TITLE_AREA = (0, 0, WIDTH, int(HEIGHT/8))

# One line of music is half of the remaining height
LINE = (0, 0, WIDTH, int(HEIGHT*7/16))

# I need eight bubbles for notes and seven spacers, with the spacers at 1/4 the size of the bubbles
BUBBLE = 180
SPACE = BUBBLE/4

# I have 550px of height and need to divide 8 bubbles - keeping in mind they all need to fit inside
# so the vertical offset is 58px for each bubble

partition = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(partition)

tune = ["e", "d", "c", "d", "e", "R", "d", "d"]

for i, note in enumerate(tune):
    start_x = 12 + i * (BUBBLE + SPACE)
    start_y = 58 * (7 - NOTES[note].pos)
    end_x, end_y = start_x + BUBBLE, start_y + BUBBLE
    draw.ellipse((start_x, start_y, end_x, end_y), fill=NOTES[note].colour)

partition.show()
