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


class CanvasCoords:
    def _calculate_bubble_diameter(number_of_notes: int, canvas_width: int) -> float:
        if number_of_notes < 4:
            number_of_notes = 4
        number_of_spacers = number_of_notes - 1
        return canvas_width / (number_of_notes + number_of_spacers / 3)

    def _calculate_xpos(enumerated: int, note: dict) -> float:
        radius = note["radius"]
        diameter = note["diameter"]
        return (diameter + diameter / 3) * enumerated + radius

    def _calculate_ypos(canvas_height: int, note: dict) -> float:
        lowest_ypos = canvas_height - note["diameter"]
        note_y_val = VERTICAL[note["name"]]
        return lowest_ypos - note_y_val * (lowest_ypos / 6) + note["radius"]

    def parse_notes_list(
        tune: list[str], canvas_width: int = 1, canvas_height: int = 1
    ) -> list[dict]:
        # print(tune)
        number_of_notes = len(tune)
        bubble_diameter = CanvasCoords._calculate_bubble_diameter(
            number_of_notes, canvas_width
        )
        notes_as_dicts = []
        for note in tune:
            note_as_dict = {
                "name": note,
                "diameter": bubble_diameter,
                "radius": bubble_diameter / 2,
                "color": COLORS[note],
            }
            notes_as_dicts.append(note_as_dict)
        for i, note in enumerate(notes_as_dicts):
            note["x"] = CanvasCoords._calculate_xpos(i, note)
            note["y"] = CanvasCoords._calculate_ypos(canvas_height, note)
        return notes_as_dicts


class PillowCoords:
    def _calculate_bubble_size(number_of_notes: int, canvas_width: int) -> float:
        if number_of_notes < 4:
            number_of_notes = 4
        number_of_spacers = number_of_notes - 1
        return canvas_width / (number_of_notes + number_of_spacers / 3)

    def _calculate_xpos(enumerated: int, note: dict) -> float:
        bubble_size = note["diameter"]
        return (bubble_size + bubble_size / 3) * enumerated

    def _calculate_ypos(canvas_height: int, note: dict) -> float:
        lowest_ypos = canvas_height - note["diameter"]
        note_y_val = VERTICAL[note["name"]]
        return lowest_ypos - note_y_val * (lowest_ypos / 6)

    def parse_notes_list(
        tune: list[str], canvas_width: int = 1, canvas_height: int = 1
    ) -> list[dict]:
        # print(tune)
        number_of_notes = len(tune)
        bubble_size = PillowCoords._calculate_bubble_size(number_of_notes, canvas_width)
        notes_as_dicts = []
        for note in tune:
            note_as_dict = {
                "name": note,
                "diameter": bubble_size,
                "radius": bubble_size / 2,
                "color": COLORS[note],
            }
            notes_as_dicts.append(note_as_dict)
        for i, note in enumerate(notes_as_dicts):
            note["x"] = PillowCoords._calculate_xpos(i, note)
            note["y"] = PillowCoords._calculate_ypos(canvas_height, note)
        return notes_as_dicts


class Tune(list):
    def __init__(self, notes: list) -> None:
        note_attributes = self._generate_note_attributes(notes)
        super().__init__(note_attributes)

    def _generate_note_attributes(self, notes):
        return [{"name": note, "color": COLORS[note]} for note in notes]

    def generate_canvas_coords(self, width: int, height: int) -> None:
        print(self)

    def generate_pillow_coords(self, width: int, height: int) -> None:
        pass
