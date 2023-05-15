from dataclasses import dataclass
import json


NOTE_ATTRIBUTES = {
    "c": {
        "color": "#ee0000",
        "vertical": 369,
    },
    "d": {
        "color": "#ff860d",
        "vertical": 308,
    },
    "e": {
        "color": "#ffff38",
        "vertical": 247,
    },
    "f": {
        "color": "#069a2e",
        "vertical": 186,
    },
    "g": {
        "color": "#0000ee",
        "vertical": 125,
    },
    "a": {
        "color": "#e84473",
        "vertical": 64,
    },
    "b": {
        "color": "#000060",
        "vertical": 3,
    },
}


def _calculate_spatials(canvas_width: int, number_of_notes: int):
    number_of_spacers = number_of_notes - 1
    bubble_size = int(canvas_width / (number_of_notes + number_of_spacers / 3))
    bubble_size -= bubble_size % 3
    bubbles_sum = bubble_size * number_of_notes
    spacer_size = int(bubble_size / 3)
    spacers_sum = spacer_size * number_of_spacers
    offset = int((canvas_width - (bubbles_sum + spacers_sum)) / 2)
    xpos = (offset + i * (bubble_size + spacer_size) for i in range(number_of_notes))
    return bubble_size, xpos


def tune_to_coords(
    tune: list[str], canvas_width: int, canvas_height: int
) -> list[dict]:
    tune_data = [
        {
            "name": note,
            "color": NOTE_ATTRIBUTES[note]["color"],
            "y": NOTE_ATTRIBUTES[note]["vertical"],
        }
        for note in tune
    ]
    if len(tune) <= 4:
        diameter, x_positions = _calculate_spatials(canvas_width, 4)
    else:
        diameter, x_positions = _calculate_spatials(canvas_width, len(tune))
    for note, pos in zip(tune_data, x_positions):
        note["x"] = pos
        note["diameter"] = diameter
    return tune_data

    # Highest note has y=0; lowest note has y=height-bubble_size (963-594)=369
    # But find x <= 369 where x % (len(NOTES)-1) == 0
    # vertical_step_size = int((963-594) / 6)
    # vertical_step_size -= vertical_step_size % 6
