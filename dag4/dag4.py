import re


def line_to_list_of_numbers(line):
    nrs = []
    for nr in line.split(' '):
        if nr:
            nrs.append(int(nr))
    return nrs


class Card:
    def __init__(self, number):
        self._number = int(number)
        self._winning_numbers = []
        self._own_numbers = []
        self._cardnumbers = []
        self.nrofcopies = 0

    @property
    def number(self):
        return self._number

    @property
    def winning_numbers(self):
        return self._winning_numbers

    @winning_numbers.setter
    def winning_numbers(self, line):
        self._winning_numbers = line_to_list_of_numbers(line)

    @property
    def own_numbers(self):
        return self._own_numbers

    @own_numbers.setter
    def own_numbers(self, line):
        self._own_numbers = line_to_list_of_numbers(line)

    def get_own_winning_numbers(self):
        nrs = []
        for nr in self.own_numbers:
            if nr in self.winning_numbers:
                nrs.append(nr)
        return nrs

    def get_points(self):
        points = 0
        for nr in range(0, len(self.get_own_winning_numbers())):
            if points == 0:
                points = 1
            else:
                points = points * 2
        return points

    @property
    def cardnumbers(self):
        if len(self._cardnumbers) == 0:
            for nr in range(1, len(self.get_own_winning_numbers()) + 1):
                cardcopy = nr + self._number
                self._cardnumbers.append(cardcopy)
        return self._cardnumbers


class CardsTable:
    def __init__(self):
        self._lines = []
        self._cards = []

    @property
    def cards(self):
        if len(self._cards) == 0:
            self.processtable()
        return self._cards

    def readinput(self):
        inputfile = open('input.txt', 'r')
        for line in inputfile.readlines():
            self._lines.append(line.strip())

    def processtable(self):
        if len(self._lines) == 0:
            self.readinput()
        for line in self._lines:
            result = re.match(r"Card\s+(\d+): (.+) \| (.+)", line)
            card = Card(result.group(1))
            card.winning_numbers = result.group(2)
            card.own_numbers = result.group(3)
            self._cards.append(card)

    def get_totalpoints(self):
        total = 0
        for card in self.cards:
            total += card.get_points()
        return total

    def get_totalcards(self):
        total = 0
        cardinstances = []
        for card in self.cards:
            cardinstances.append(card.number)
        for card in self.cards:
            for cardcopy in card.cardnumbers:
                if cardcopy != card.number:
                    self.cards[cardcopy - 1].cardnumbers.append(cardcopy)
        for card in self.cards:
            total += len(card.cardnumbers)

        return total


if __name__ == '__main__':
    ct = CardsTable()
    print(ct.get_totalpoints())
