import unittest
import json
import music_bubbles


class TestTuneToCoords(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_givenEmptyTune_ReturnsEmptyList(self):
        expected = []
        actual = music_bubbles.parse_notes_list([])
        self.assertEqual(expected, actual)

    def test_givenOneNote_ReturnsNoteName(self):
        expected = "c"
        tune_as_list = music_bubbles.parse_notes_list(["c"])
        actual = tune_as_list[0]["name"]
        self.assertEqual(expected, actual)

    def test_notesReceiveColorAttributes(self):
        tune_as_list = music_bubbles.parse_notes_list(["c", "e"])
        expected = "#ee0000"
        actual = tune_as_list[0]["color"]
        self.assertEqual(expected, actual)
        expected = "#ffff38"
        actual = tune_as_list[1]["color"]
        self.assertEqual(expected, actual)

    def test_notesHaveSizeAttribute(self):
        tune = ["c", "d", "e", "f"]
        tune_as_list = music_bubbles.parse_notes_list(tune)
        expected = 0.2
        actual = tune_as_list[0]["diameter"]
        self.assertEqual(expected, actual)

    def test_shortTuneHasXAxisAttributes(self):
        tune = ["c", "e"]
        tune_as_list = music_bubbles.parse_notes_list(tune)
        expected = tuple((0.2 + 0.2 / 3) * i for i in range(2))
        actual = tuple(note["x"] for note in tune_as_list)
        self.assertEqual(expected, actual)

    def test_longTuneHasXAxisAttributes(self):
        tune = ["c", "d", "e", "f", "g", "a", "b"]
        tune_as_list = music_bubbles.parse_notes_list(tune)
        expected = tuple((1 / 9 + 1 / 9 / 3) * i for i in range(7))
        actual = tuple(note["x"] for note in tune_as_list)
        self.assertEqual(expected, actual)

    def test_notesHaveYAxisAttribute(self):
        tune = ["c", "e"]
        tune_as_list = music_bubbles.parse_notes_list(tune)
        expected = (0, 2)
        actual = tuple(note["y"] for note in tune_as_list)
        self.assertEqual(expected, actual)
