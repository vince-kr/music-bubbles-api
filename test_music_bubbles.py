import unittest
import music_bubbles as mb


class TestParseNotesList(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_givenEmptyTune_ReturnsEmptyList(self):
        expected = []
        actual = mb.parse_notes_list([])
        self.assertEqual(expected, actual)

    def test_givenOneNote_ReturnsNoteName(self):
        expected = "c"
        notes_as_dicts = mb.parse_notes_list(["c"])
        actual = notes_as_dicts[0]["name"]
        self.assertEqual(expected, actual)

    def test_notesReceiveColorAttributes(self):
        notes_as_dicts = mb.parse_notes_list(["c", "e"])
        expected = "#ee0000"
        actual = notes_as_dicts[0]["color"]
        self.assertEqual(expected, actual)
        expected = "#ffff38"
        actual = notes_as_dicts[1]["color"]
        self.assertEqual(expected, actual)

    def test_notesHaveSizeAttribute(self):
        tune = ["c", "d", "e", "f"]
        notes_as_dicts = mb.parse_notes_list(tune)
        expected = 0.2
        actual = notes_as_dicts[0]["diameter"]
        self.assertEqual(expected, actual)

    def test_shortTuneHasXAxisAttributes(self):
        tune = ["c", "e"]
        notes_as_dicts = mb.parse_notes_list(tune)
        expected = tuple((0.2 + 0.2 / 3) * i for i in range(2))
        actual = tuple(note["x"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)

    def test_longTuneHasXAxisAttributes(self):
        tune = ["c", "d", "e", "f", "g", "a", "b"]
        notes_as_dicts = mb.parse_notes_list(tune)
        bubble_size = 1 / 9  # Divisor is 7 notes + (7 - 1) * 1 / 3 spacers
        spacer_size = bubble_size / 3
        expected = tuple((bubble_size + spacer_size) * i for i in range(7))
        actual = tuple(note["x"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)

    def test_notesHaveYAxisAttribute(self):
        tune = ["c", "e"]
        notes_as_dicts = mb.parse_notes_list(tune)
        c_ypos = 0.8 - 0 * (0.8 / 6)  # C offset 0
        e_ypos = 0.8 - 2 * (0.8 / 6)  # E offset 2
        expected = (c_ypos, e_ypos)
        actual = tuple(note["y"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)


class TestCoordinates(unittest.TestCase):
    def test_NoteXPositionDependsOnCanvasWidth(self):
        canvas_width = 60
        notes_as_dicts = mb.parse_notes_list(["c", "d", "e", "f"], canvas_width)
        expected = (0, 16, 32, 48)
        actual = tuple(note["x"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)

    def test_NoteYPositionDependsOnCanvasHeight(self):
        canvas_width = 60  # Bubble diameter 12
        canvas_height = 42  # Lowest note at 30; each subsequent note 5 up
        tune = ["c", "d", "e", "f"]
        notes_as_dicts = mb.parse_notes_list(tune, canvas_width, canvas_height)
        expected = (30, 25, 20, 15)
        actual = tuple(note["y"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)
