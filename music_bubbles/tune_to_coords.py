from dataclasses import dataclass
import json


@dataclass
class Note:
    color: str
    pos: int


NOTES = {
    "c": Note("#ee0000", 1),
    "d": Note("#ff860d", 2),
    "e": Note("#ffff38", 3),
    "f": Note("#069a2e", 4),
    "g": Note("#0000ee", 5),
    "a": Note("#e84473", 6),
    "b": Note("#000060", 7),
    "R": Note("#00000000", 0),  # rest
}


def tune_to_coords(
    tune: list[str], canvas_width: int, canvas_height: int
) -> list[Note]:
    coordinates = [NOTES[note] for note in tune]
    if len(tune) <= 4:
        bubble_size = int(canvas_width / 5)
        bubble_size -= bubble_size % 3
        spacer_size = int(bubble_size / 3)
        offset = int((canvas_width - (bubble_size + spacer_size)) / 2)
        fixed_xpos = (
            offset + i * (bubble_size + spacer_size) for i in range(len(tune))
        )
        for i, xpos in enumerate(fixed_xpos):
            coordinates[i].x = xpos
    return coordinates
