import unittest
import json
from music_bubbles import tune_to_coords


class TestTuneToCoords(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_givenEmptyTune_ttcReturnsEmptyList(self):
        expected = list()
        actual = tune_to_coords.tune_to_coords([], 12, 12)
        self.assertEqual(expected, actual)

    def test_givenOneNote_ttcReturnsDictOfLengthOne(self):
        expected = 1
        actual = len(tune_to_coords.tune_to_coords(["e"], 12, 12))
        self.assertEqual(expected, actual)

    def test_notesReceiveColorAttributes(self):
        coordinates = tune_to_coords.tune_to_coords(["c", "e"], 12, 12)
        expected = "#ee0000"
        actual = coordinates[0]["color"]
        self.assertEqual(expected, actual)
        expected = "#ffff38"
        actual = coordinates[1]["color"]
        self.assertEqual(expected, actual)

    def test_notesHaveXAxisAttribute(self):
        tune = ["c", "e", "g", "b"]
        canvas_size = (60, 40)
        coordinates = tune_to_coords.tune_to_coords(tune, *canvas_size)
        expected = (0, 16, 32, 48)
        actual = tuple(coord["x"] for coord in coordinates)
        self.assertEqual(expected, actual)

    def test_tuneWithMoreThanFourNotesHaveXAxisAttributes(self):
        tune = ["c", "d", "e", "f", "g", "a", "b", "c"]
        canvas_size = (2970, 963)
        coordinates = tune_to_coords.tune_to_coords(tune, *canvas_size)
        expected = (12, 392, 772, 1152, 1532, 1912, 2292, 2672)
        actual = tuple(coord["x"] for coord in coordinates)
        self.assertEqual(expected, actual)

    def test_notesHaveSizeAttribute(self):
        tune = ["c", "d", "e", "f", "g", "a", "b", "c"]
        canvas_size = (2970, 963)
        coordinates = tune_to_coords.tune_to_coords(tune, *canvas_size)
        expected = 285
        actual = coordinates[0]["diameter"]
        self.assertEqual(expected, actual)

    def test_notesHaveYAxisAttribute(self):
        tune = ["c", "e"]
        canvas_size = (2970, 963)
        coordinates = tune_to_coords.tune_to_coords(tune, *canvas_size)
        expected = (369, 247)
        actual = (coordinates[0]["y"], coordinates[1]["y"])
        self.assertEqual(expected, actual)
