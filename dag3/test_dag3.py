import unittest

from dag3 import EngineSchematic


class TestDag3(unittest.TestCase):
    def test_find_parts(self):
        schema = EngineSchematic()
        schema._lines = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.3"
        ]
        self.assertEqual(11, len(schema.get_candidates()))
        firstpart = schema.get_candidates()[0]
        self.assertEqual("467", firstpart.number)
        self.assertEqual(0, firstpart._startx)
        self.assertEqual(0, firstpart._starty)
        self.assertEqual("755", schema.get_candidates()[7].number)
        apart = schema.get_candidates()[9]
        self.assertEqual("598", apart.number)
        self.assertEqual(5, apart.startx)
        self.assertEqual(9, apart.starty)
        lastpart = schema.get_candidates()[10]
        self.assertEqual("3", lastpart.number)
        self.assertEqual(9, lastpart.startx)
        self.assertEqual(9, lastpart.starty)

        self.assertEqual(9, schema._max_x)
        self.assertEqual(9, schema._max_y)
        self.assertEqual(0, schema._min_x)
        self.assertEqual(0, schema._min_y)

        self.assertEqual(3, firstpart.get_buur_right())
        self.assertEqual(-1, firstpart.get_buur_left())
        self.assertEqual([], firstpart.get_buur_up())
        self.assertEqual([0, 1, 2, 3], firstpart.get_buur_down())

        self.assertEqual(8, apart.get_buur_right())
        self.assertEqual(4, apart.get_buur_left())
        self.assertEqual([4, 5, 6, 7, 8], apart.get_buur_up())
        self.assertEqual([], apart.get_buur_down())

        self.assertEqual(-1, lastpart.get_buur_right())
        self.assertEqual(8, lastpart.get_buur_left())
        self.assertEqual([8, 9], lastpart.get_buur_up())
        self.assertEqual([], lastpart.get_buur_down())

        seventhpart = schema.get_candidates()[6]
        self.assertEqual("592", seventhpart.number)
        self.assertEqual(2, seventhpart.startx)
        self.assertEqual(6, seventhpart.starty)
        self.assertEqual(5, seventhpart.get_buur_right())
        self.assertEqual(1, seventhpart.get_buur_left())
        self.assertEqual([1, 2, 3, 4, 5], seventhpart.get_buur_up())
        self.assertEqual([1, 2, 3, 4, 5], seventhpart.get_buur_down())

        partnumbers = []
        for part in schema.valid_parts():
            partnumbers.append(part.number)
        self.assertEqual(["467", "35", "633", "617", "592", "755", "664", "598"], partnumbers)

        self.assertEqual(4361, schema.sum_valid_parts())
        partnumbers = []
        for part in schema.gear_ratio_parts():
            partnumbers.append((part.number, part.gearx, part.geary))
        self.assertEqual([("467", 3, 1), ("35", 3, 1), ("617", 3, 4), ("755", 5, 8), ("598", 5, 8)], partnumbers)

        self.assertEqual(467835, schema.sum_gear_ratio())


if __name__ == '__main__':
    unittest.main()
