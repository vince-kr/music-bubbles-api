from dataclasses import dataclass
import json


@dataclass
class Note:
    color: str


COLORS = {
    "c": "#ee0000",
    "d": "#ff860d",
    "e": "#ffff38",
    "f": "#069a2e",
    "g": "#0000ee",
    "a": "#e84473",
    "b": "#000060",
}


def _calculate_xpos(canvas_width: int, number_of_notes: int = 4):
    number_of_spacers = number_of_notes - 1
    bubble_size = int(canvas_width / (number_of_notes + number_of_spacers / 3))
    bubble_size -= bubble_size % 3
    bubbles_sum = bubble_size * number_of_notes
    spacer_size = int(bubble_size / 3)
    spacers_sum = spacer_size * number_of_spacers
    offset = int((canvas_width - (bubbles_sum + spacers_sum)) / 2)
    xpos = (offset + i * (bubble_size + spacer_size) for i in range(number_of_notes))
    return xpos


def tune_to_coords(
    tune: list[str], canvas_width: int, canvas_height: int
) -> list[dict]:
    tune_data = [{"name": note, "color": COLORS[note]} for note in tune]
    if len(tune) <= 4:
        x_positions = _calculate_xpos(canvas_width, 4)
    else:
        x_positions = _calculate_xpos(canvas_width, len(tune))
    for note, pos in zip(tune_data, x_positions):
        note["x"] = pos
    return tune_data

    # Highest note has y=0; lowest note has y=height-bubble_size (963-594)=369
    # But find x <= 369 where x % (len(NOTES)-1) == 0
    # vertical_step_size = int((963-594) / 6)
    # vertical_step_size -= vertical_step_size % 6
