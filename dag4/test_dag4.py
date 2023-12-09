import unittest

from dag4 import CardsTable


class TestcardTable(unittest.TestCase):
    def test_winning(self):
        ct = CardsTable()
        ct._lines = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        ]
        self.assertEqual([41, 48, 83, 86, 17], ct.cards[0].winning_numbers)
        self.assertEqual([83, 86, 6, 31, 17, 9, 48, 53], ct.cards[0].own_numbers)
        self.assertEqual(6, len(ct.cards))
        self.assertEqual([61, 32], ct.cards[1].get_own_winning_numbers())
        self.assertEqual([21, 1], ct.cards[2].get_own_winning_numbers())
        self.assertEqual([84], ct.cards[3].get_own_winning_numbers())
        self.assertEqual([], ct.cards[4].get_own_winning_numbers())
        self.assertEqual([], ct.cards[5].get_own_winning_numbers())
        self.assertEqual(8, ct.cards[0].get_points())
        self.assertEqual(2, ct.cards[1].get_points())
        self.assertEqual(2, ct.cards[2].get_points())
        self.assertEqual(1, ct.cards[3].get_points())
        self.assertEqual(0, ct.cards[4].get_points())
        self.assertEqual(13, ct.get_totalpoints())

        self.assertEqual([2, 3, 4, 5], ct.cards[0].cardnumbers)
        self.assertEqual([3, 4], ct.cards[1].cardnumbers)
        self.assertEqual([4, 5], ct.cards[2].cardnumbers)
        self.assertEqual([5], ct.cards[3].cardnumbers)
        self.assertEqual([], ct.cards[4].cardnumbers)
        self.assertEqual([], ct.cards[5].cardnumbers)

        self.assertEqual(30, ct.get_totalcards())


if __name__ == '__main__':
    unittest.main()
