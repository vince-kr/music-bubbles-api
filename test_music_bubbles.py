import unittest
from music_bubbles import Tune

# Both classes have a parse_notes_list main method that takes a list of strings and
# returns a list of dicts. The values for both are:
# 1. Name       IDENTICAL
# 2. Diameter   IDENTICAL
# 3. Radius     IDENTICAL
# 4. Color      IDENTICAL
# 5. X & Y pos  DIFFERENT
#
# So I should test cases 1-4 in one test class, which calls one function (or
# instantiates one class) and test case 5 in a separate class.


class TestTuneAttributes(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_givenOneNote_ReturnsNoteName(self):
        notes_as_dicts = Tune(["c"])
        expected = "c"
        actual = notes_as_dicts[0]["name"]
        self.assertEqual(expected, actual)

    def test_notesReceiveColorAttributes(self):
        notes_as_dicts = Tune(["c", "e"])
        expected = "#ee0000"
        actual = notes_as_dicts[0]["color"]
        self.assertEqual(expected, actual)
        expected = "#ffff38"
        actual = notes_as_dicts[1]["color"]
        self.assertEqual(expected, actual)

    def test_notesHaveSizeAttributes(self):
        notes_list = ["c", "d", "e", "f"]
        notes_as_dicts = Tune(notes_list)
        expected_radius = 0.1
        actual_radius = notes_as_dicts[0]["radius"]
        self.assertEqual(expected_radius, actual_radius)


class TestCanvasAttributes(unittest.TestCase):
    def test_shortTuneHasXAxisAttributes(self):
        notes_list = ["c", "g"]
        width = 15  # radius 1.5, diameter 3, spacer 1
        height = 1  # not relevant
        notes_as_dicts = Tune(notes_list).generate_coords(width, height, True)
        expected = (1.5, 5.5)
        actual = tuple(note["x"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)

    def test_longTuneHasXAxisAttributes(self):
        notes_list = ["c", "d", "e", "f", "g", "a", "b"]
        width = 27  # radius 1.5, diameter 3, spacer 1
        height = 1  # not relevant
        notes_as_dicts = Tune(notes_list).generate_coords(width, height, True)
        expected = tuple(1.5 + i * 4 for i in range(7))
        actual = tuple(note["x"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)

    def test_notesHaveYAxisAttribute(self):
        notes_list = ["c", "g", "c", "e"]
        width = 15  # radius 1.5, diameter 3
        height = 9  # lowest y_pos 6
        notes_as_dicts = Tune(notes_list).generate_coords(width, height, True)
        expected = (7.5, 3.5, 7.5, 5.5)
        actual = tuple(note["y"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)


class TestPillowAttributes(unittest.TestCase):
    def test_shortTuneHasXAxisAttributes(self):
        notes_list = ["c", "e"]
        width = 15  # radius 1.5, diameter 3, spacer 1
        height = 1  # not relevant
        notes_as_dicts = Tune(notes_list).generate_coords(width, height)
        expected = (0, 4)
        actual = tuple(note["x"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)

    def test_longTuneHasXAxisAttributes(self):
        notes_list = ["c", "d", "e", "f", "g", "a", "b"]
        width = 27  # radius 1.5, diameter 3, spacer 1
        height = 1  # not relevant
        notes_as_dicts = Tune(notes_list).generate_coords(width, height)
        expected = tuple(4 * i for i in range(7))
        actual = tuple(note["x"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)

    def test_notesHaveYAxisAttribute(self):
        notes_list = ["c", "g", "c", "e"]
        width = 15  # radius 1.5, diameter 3
        height = 9  # lowest y_pos 6
        notes_as_dicts = Tune(notes_list).generate_coords(width, height)
        expected = (6, 2, 6, 4)
        actual = tuple(note["y"] for note in notes_as_dicts)
        self.assertEqual(expected, actual)
