from PIL import Image, ImageDraw, ImageFont
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

# Title area at 2/16 of page height; music lines at 7/16 of page height each
TITLE_AREA = (WIDTH, int(HEIGHT * 2 / 20))
MUSIC_LINE = (WIDTH, int(HEIGHT * 9 / 20))

# Create the images
partition = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
title_area = Image.new("RGBA", TITLE_AREA, (0, 0, 0, 0))
line_one = Image.new("RGBA", MUSIC_LINE, (0,0,0,0))
line_two = Image.new("RGBA", MUSIC_LINE, (0,0,0,0))

# First, let's write the title
title = ImageDraw.Draw(title_area)
title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", size=120)
title.text((int(WIDTH / 2), 6), "Melody", fill="black", font=title_font, anchor="mt", align="center")


# Now the music bars
# I need eight bubbles for notes and seven spacers, with the spacers at 1/4 the size of the bubbles
BUBBLE = 180
SPACE = BUBBLE/4
# This gives me 180 * 8 + 45 * 7 = 1755 width, leaving 27px

# Each music bar should get a thin black line along its top in addition to any note bubbles


# First, line_one_bubbles
line_one_draw = ImageDraw.Draw(line_one)
line_one_tune = ["c", "g", "c", "g", "a", "g", "f", "e"]
line_one_tune = [NOTES[note] for note in line_one_tune]

for i, note in enumerate(line_one_tune):
    start_x = 12 + i * (BUBBLE + SPACE)
    start_y = 381 - ((note.pos-1) * 55)
    end_x, end_y = start_x + BUBBLE, start_y + BUBBLE
    line_one_draw.ellipse((start_x, start_y, end_x, end_y), fill=note.colour)

line_one_draw.line((0,0,WIDTH,0), fill="black", width=12)

# And now line_two_bubbles
line_two_draw = ImageDraw.Draw(line_two)
line_two_tune = ["d", "b", "g", "e", "d", "e", "c"]
line_two_tune = [NOTES[note] for note in line_two_tune]

for i, note in enumerate(line_two_tune):
    start_x = 12 + i * (BUBBLE + SPACE)
    start_y = 381 - ((note.pos-1) * 55)
    end_x, end_y = start_x + BUBBLE, start_y + BUBBLE
    line_two_draw.ellipse((start_x, start_y, end_x, end_y), fill=note.colour)

line_two_draw.line((0,0,WIDTH,0), fill="black", width=12)

# Paste the three elements into the partition, then show the partition
partition.paste(title_area, (0, 0))
partition.paste(line_one, (0, int(HEIGHT * 2 / 20)))
partition.paste(line_two, (0, int(HEIGHT * 11 / 20)))
partition.show()
