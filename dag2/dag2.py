import re

RED = 'red'
BLUE = 'blue'
GREEN = 'green'

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def create_set(setline):
    cube = {RED: 0, BLUE: 0, GREEN: 0}
    for cubes in setline.split(','):
        result = re.match(r"(\d+)\s(red|blue|green)", cubes.strip())
        cube[result.group(2)] += int(result.group(1))
    return cube


def is_validset(colorset):
    if colorset[BLUE] <= MAX_BLUE and colorset[RED] <= MAX_RED and colorset[GREEN] <= MAX_GREEN:
        return True
    return False


class Game:
    def __init__(self, sets):
        self._sets = []
        self.valid = True
        for setline in sets:
            colorset = create_set(setline)
            if is_validset(colorset):
                self._sets.append(colorset)
            else:
                self._sets.append(colorset)
                self.valid = False

    def nr_of_sets(self):
        return len(self._sets)

    def max_per_color(self):
        max_blue = 0
        max_red = 0
        max_green = 0
        for s in self._sets:
            if s[BLUE] > max_blue:
                max_blue = s[BLUE]
            if s[RED] > max_red:
                max_red = s[RED]
            if s[GREEN] > max_green:
                max_green = s[GREEN]
        return max_red, max_green, max_blue


class Games:

    def __init__(self):
        self._lines = []
        self._games = {}

    def readinput(self):
        inputfile = open('input.txt', 'r')
        self._lines = inputfile.readlines()

    def get_game(self, game_id):
        if self._games == {}:
            self.parse_lines()
        return self._games[game_id]

    def parse_lines(self):
        for line in self._lines:
            [ident, games] = line.split(':')
            game_id = ident[5:].strip()
            game = Game(games.split(';'))
            self._games[game_id] = game

    def sum_valid_game_ids(self):
        totalsum = 0
        if self._games == {}:
            self.parse_lines()
        for game_id in self._games.keys():
            if self._games[game_id].valid:
                totalsum += int(game_id)
        return totalsum

    def get_power(self):
        totalsum = 0
        if self._games == {}:
            self.parse_lines()
        for game_id in self._games.keys():
            power = 1
            for m in self._games[game_id].max_per_color():
                power = power * m
            totalsum += power
        return totalsum


g = Games()
g.readinput()
print(g.sum_valid_game_ids())
print(g.get_power())
