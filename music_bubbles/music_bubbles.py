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


def _calculate_bubble_size(number_of_notes: int) -> float:
    if number_of_notes < 4:
        number_of_notes = 4
    number_of_spacers = number_of_notes - 1
    return 1 / (number_of_notes + number_of_spacers / 3)


def _calculate_xpos(number_of_notes: int, bubble_size: float) -> Iterator[float]:
    return ((bubble_size + bubble_size / 3) * i for i in range(number_of_notes))


def parse_notes_list(tune: list[str]) -> list[dict]:
    number_of_notes = len(tune)
    bubble_size = _calculate_bubble_size(number_of_notes)
    notes_as_dicts = [
        {
            "name": note,
            "diameter": bubble_size,
            "y": VERTICAL[note],
            "color": COLORS[note],
        }
        for note in tune
    ]
    for note, xpos in zip(
        notes_as_dicts, _calculate_xpos(number_of_notes, bubble_size)
    ):
        note["x"] = xpos
    return notes_as_dicts
