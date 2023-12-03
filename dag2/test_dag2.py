import unittest

from dag2 import Games


class TestDag2(unittest.TestCase):
    def test_games(self):
        g = Games()
        g._lines = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
        self.assertEqual(3, g.get_game("1").nr_of_sets())
        self.assertTrue(g.get_game("1").valid)
        self.assertTrue(g.get_game("2").valid)
        self.assertFalse(g.get_game("3").valid)
        self.assertFalse(g.get_game("4").valid)
        self.assertTrue(g.get_game("5").valid)
        self.assertEqual(8, g.sum_valid_game_ids())

        self.assertEqual((4,2,6), g.get_game("1").max_per_color())
        self.assertEqual((1,3,4), g.get_game("2").max_per_color())
        self.assertEqual((20,13,6), g.get_game("3").max_per_color())
        self.assertEqual((14,3,15), g.get_game("4").max_per_color())
        self.assertEqual((6,3,2), g.get_game("5").max_per_color())

        self.assertEqual(2286, g.get_power())


if __name__ == '__main__':
    unittest.main()
