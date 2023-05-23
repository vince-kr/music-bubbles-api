from typing import Iterator

COLORS = {
    "c": "#ee0000",
    "d": "#ff860d",
    "e": "#ffff38",
    "f": "#069a2e",
    "g": "#0000ee",
    "a": "#e84473",
    "b": "#000060",
}

VERTICAL = {
    "c": 0,
    "d": 1,
    "e": 2,
    "f": 3,
    "g": 4,
    "a": 5,
    "b": 6,
}


def _calculate_bubble_size(number_of_notes: int, canvas_width: int) -> float:
    if number_of_notes < 4:
        number_of_notes = 4
    number_of_spacers = number_of_notes - 1
    return canvas_width / (number_of_notes + number_of_spacers / 3)


def _calculate_xpos(number_of_notes: int, bubble_size: float) -> Iterator[float]:
    return ((bubble_size + bubble_size / 3) * i for i in range(number_of_notes))


def _calculate_ypos(canvas_height: int, note: dict) -> float:
    lowest_ypos = canvas_height - note["diameter"]
    note_y_val = VERTICAL[note["name"]]
    return lowest_ypos - note_y_val * (lowest_ypos / 6)


def parse_notes_list(
    tune: list[str], canvas_width: int = 1, canvas_height: int = 1
) -> list[dict]:
    number_of_notes = len(tune)
    bubble_size = _calculate_bubble_size(number_of_notes, canvas_width)
    notes_as_dicts = [
        {
            "name": note,
            "diameter": bubble_size,
            "color": COLORS[note],
        }
        for note in tune
    ]
    x_positions = _calculate_xpos(number_of_notes, bubble_size)
    for note, xpos in zip(notes_as_dicts, x_positions):
        note["x"] = xpos
    for note in notes_as_dicts:
        note["y"] = _calculate_ypos(canvas_height, note)
    return notes_as_dicts
