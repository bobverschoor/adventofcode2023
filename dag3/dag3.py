def issymbol(c, symbol):
    if symbol:
        if c == symbol:
            return True
        else:
            return False
    if c.isalnum():
        return False
    if c == ".":
        return False
    return True


class Part:
    def __init__(self, x, y, minx, miny, maxx, maxy):
        self._startx = x
        self._starty = y
        self._minx = minx
        self._miny = miny
        self._maxx = maxx
        self._maxy = maxy
        self._number = ""
        self._gearx = -1
        self._geary = -1

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, n):
        self._number = n

    @property
    def startx(self):
        return self._startx

    @property
    def starty(self):
        return self._starty

    @property
    def gearx(self):
        return self._gearx

    @gearx.setter
    def gearx(self, x):
        self._gearx = x

    @property
    def geary(self):
        return self._geary

    @geary.setter
    def geary(self, y):
        self._geary = y

    def get_buur_left(self):
        if self._startx > self._minx:
            return self._startx - 1
        return -1

    def get_buur_right(self):
        x = self._startx + len(self._number)
        if x < self._maxx:
            return x
        return -1

    def get_buur_up(self):
        if self._starty <= self._miny:
            return []
        leftx = self.get_buur_left()
        if leftx == -1:
            leftx = self._minx
        rightx = self.get_buur_right()
        if rightx == -1:
            rightx = self._maxx
        return list(range(leftx, rightx + 1))

    def get_buur_down(self):
        if self._starty >= self._maxy:
            return []
        leftx = self.get_buur_left()
        if leftx == -1:
            leftx = self._minx
        rightx = self.get_buur_right()
        if rightx == -1:
            rightx = self._maxx
        return list(range(leftx, rightx + 1))


class EngineSchematic:
    def __init__(self):
        self._lines = []
        self._parts = []
        self._min_x = 0
        self._min_y = 0
        self._max_x = 0
        self._max_y = 0

    def readinput(self):
        inputfile = open('input.txt', 'r')
        for line in inputfile.readlines():
            self._lines.append(line.strip())

    def get_candidates(self):
        if self._parts:
            return self._parts
        y = -1
        self._max_y = len(self._lines) - 1
        self._max_x = len(self._lines[0]) - 1
        for line in self._lines:
            number = ""
            y += 1
            part = self._parse_line(line, y)
            if part:
                part.number = number
                self._parts.append(part)
        return self._parts

    def valid_parts(self, symbol=""):
        valid_parts = []
        if not self._lines:
            self.readinput()
        if not self._parts:
            self.get_candidates()
        for part in self._parts:
            valid = False
            buurleft = part.get_buur_left()
            if buurleft != -1:
                if issymbol(self._lines[part.starty][buurleft], symbol):
                    if symbol:
                        part.gearx = buurleft
                        part.geary = part.starty
                    valid = True
            buurright = part.get_buur_right()
            if buurright != -1:
                if issymbol(self._lines[part.starty][buurright], symbol):
                    if symbol:
                        part.gearx = buurright
                        part.geary = part.starty
                    valid = True
            if not valid:
                for buur in part.get_buur_up():
                    if issymbol(self._lines[part.starty - 1][buur], symbol):
                        if symbol:
                            part.gearx = buur
                            part.geary = part.starty - 1
                        valid = True
                        break
            if not valid:
                for buur in part.get_buur_down():
                    if issymbol(self._lines[part.starty + 1][buur], symbol):
                        if symbol:
                            part.gearx = buur
                            part.geary = part.starty + 1
                        valid = True
                        break
            if valid:
                valid_parts.append(part)
        return valid_parts

    def gear_ratio_parts(self):
        gear_parts = self.valid_parts(symbol="*")
        return gear_parts

    def sum_valid_parts(self):
        sumvalid = 0
        for part in self.valid_parts():
            sumvalid += int(part.number)
        return sumvalid

    def sum_gear_ratio(self):
        sumgear = 0
        parts = self.gear_ratio_parts()
        while parts:
            part = parts.pop()
            for siblingpart in parts:
                if part.gearx == siblingpart.gearx and part.geary == siblingpart.geary:
                    product = int(part.number) * int(siblingpart.number)
                    sumgear += product
        return sumgear

    def _parse_line(self, line, y):
        x = -1
        number = ""
        part = None
        for c in line:
            x += 1
            if c.isdigit():
                if number == "":
                    part = Part(x=x, y=y, minx=self._min_x, miny=self._min_y, maxx=self._max_x, maxy=self._max_y)
                    number = c
                else:
                    number += c
            else:
                if part:
                    part.number = number
                    number = ""
                    self._parts.append(part)
                    part = None
        if part:
            part.number = number
            self._parts.append(part)
            part = None
        return part


if __name__ == '__main__':
    schema = EngineSchematic()
    print(schema.sum_valid_parts())
    print(schema.sum_gear_ratio())
