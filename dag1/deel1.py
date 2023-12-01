LITERAL = ['one','two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
LITERAL_REV = ['eno','owt','eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

def get_first_digit(line):
    for c in line:
        if c.isdigit():
            return c

def get_last_digit(line):
    for c in reversed(line):
        if c.isdigit():
            return c


def get_last_literal(line):
    parsed = ""
    for c in reversed(line):
        parsed += c
        for lit in range(0, 9):
            if LITERAL_REV[lit] in parsed:
                return str(lit + 1)
        if c.isdigit():
            return c

def get_first_literal(line):
    parsed = ""
    for c in line:
        parsed += c
        for lit in range(0, 9):
            if LITERAL[lit] in parsed:
                return str(lit + 1)
        if c.isdigit():
            return c

class CalibrationDocument:
    def __int__(self):
        self._lines = []

    def readinput(self):
        input = open('input.txt', 'r')
        self._lines = input.readlines()

    def get_calibration_values(self):
        cals = []
        for line in self._lines:
            cals.append(self.get_calibration_value(line))
        return cals

    def get_calibration_value(self, line):
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        return int(first_digit + last_digit)

    def sum_calibration_values(self):
        total = 0
        for cv in self.get_calibration_values():
            total += cv
        return total

    def get_calibration_value_literal(self, line):
        first_digit = get_first_literal(line)
        last_digit = get_last_literal(line)
        return int(first_digit + last_digit)

    def get_calibration_values_literal(self):
        cals = []
        for line in self._lines:
            cals.append(self.get_calibration_value_literal(line))
        return cals

    def sum_calibration_values_literal(self):
        total = 0
        for cv in self.get_calibration_values_literal():
            total += cv
        return total


cd = CalibrationDocument()
cd.readinput()
print("Part 1: " + str(cd.sum_calibration_values()))
print("Part 2: " + str(cd.sum_calibration_values_literal()))