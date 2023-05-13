from dataclasses import dataclass
import json


@dataclass
class Note:
    color: str


NOTES = {
    "c": Note("#ee0000"),
    "d": Note("#ff860d"),
    "e": Note("#ffff38"),
    "f": Note("#069a2e"),
    "g": Note("#0000ee"),
    "a": Note("#e84473"),
    "b": Note("#000060"),
}


def _calculate_xpos(canvas_width: int, tune_length: int = 4):
    bubble_count = tune_length
    spacer_count = tune_length - 1
    bubble_size = int(canvas_width / (tune_length + 0.25 * tune_length))
    bubble_size -= bubble_size % 3
    spacer_size = int(bubble_size / 3)
    offset = int(
        (canvas_width - (bubble_size * bubble_count + spacer_size * spacer_count)) / 2
    )
    fixed_xpos = (offset + i * (bubble_size + spacer_size) for i in range(4))
    return fixed_xpos


def tune_to_coords(
    tune: list[str], canvas_width: int, canvas_height: int
) -> list[Note]:
    tune_data = [NOTES[note] for note in tune]
    if len(tune) <= 4:
        fixed_xpos = _calculate_xpos(canvas_width)
        for note, xpos in zip(tune_data, fixed_xpos):
            note.x = xpos
    else:
        dynamic_xpos = _calculate_xpos(canvas_width)
    return tune_data

    # Highest note has y=0; lowest note has y=height-bubble_size (963-594)=369
    # But find x <= 369 where x % (len(NOTES)-1) == 0
    # vertical_step_size = int((963-594) / 6)
    # vertical_step_size -= vertical_step_size % 6
