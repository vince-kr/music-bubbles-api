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

TITLE_AREA = (WIDTH, int(HEIGHT * 2 / 20))
MUSIC_LINE = (WIDTH, int(HEIGHT * 9 / 20))

# Create the canvas
partition = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))

# First, let's write the title
title_area = Image.new("RGBA", TITLE_AREA, (0, 0, 0, 0))
title = ImageDraw.Draw(title_area)
title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", size=120)
title.text((int(WIDTH / 2), 0), "Melody", fill="black", font=title_font, anchor="mt", align="center")


# Now the music bars
def calculate_sizes(canvas_width: int, notes_per_line: int = 8) -> tuple[int, int, int]:
    """Calculate bubble diameter and spacer width"""
    spacers_per_line = notes_per_line - 1
    bubble_diameter = int(canvas_width / (notes_per_line + spacers_per_line / 3))
    bubble_diameter = int(bubble_diameter) - (bubble_diameter % 3)
    spacer_width = int(bubble_diameter / 3)
    offset_in_px = int((canvas_width - bubble_diameter * notes_per_line - spacer_width * spacers_per_line) / 2)
    return bubble_diameter, spacer_width, offset_in_px

bubble, spacer, offset = calculate_sizes(WIDTH)

# Each music bar should get a thin black line along its top in addition to any note bubbles


# Function takes a line object and a list of notes to draw in it
def draw_bubbles(line: Image, notes: list[str]) -> Image:
    line_draw = ImageDraw.Draw(line)
    line_tune = [NOTES[note] for note in notes]

    for i, note in enumerate(line_tune):
        start_x = offset + i * (bubble + spacer)
        start_y = 381 - ((note.pos-1) * 55)
        end_x, end_y = start_x + bubble, start_y + bubble
        line_draw.ellipse((start_x, start_y, end_x, end_y), fill=note.colour)

    line_draw.line((0,0,WIDTH,0), fill="black", width=12)
    return line

tune = [
    ["c", "g", "c", "g", "a", "g", "f", "e"],
    ["d", "b", "g", "e", "d", "e", "c", "R"],
]

lines = [draw_bubbles(Image.new("RGBA", MUSIC_LINE, (0,0,0,0)), line) for line in tune]

# Paste the elements into the partition, then show the partition
partition.paste(title_area, (0, 0))
for which, line in enumerate(lines):
    partition.paste(line, (0, int(HEIGHT * (2 + which * 9) / 20)))
partition.show()