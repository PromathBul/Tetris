import cell
from constants import *
from pygame import *

class Grid():
    def __init__(self):
        self.field = []
        self.score = 0

    def fill_field(self):
        y = 0
        for i in range(AMOUNT_HEIGHT):
            x = 0
            self.field.append(list())
            for _ in range(AMOUNT_WIDTH):
                c = cell.Cell(x, y)
                self.field[i].append(c)
                x += c.size
            y += c.size

    def fill_by_figure(self, figure):
        for coor in figure.structure:
            self.field[figure.row + coor[0]][figure.column + coor[1]].is_fill = True

    def refill_field(self, figure, coord):
        for c in figure.prev_structure:
            self.field[coord[0] + c[0]][coord[1] + c[1]].is_fill = False

        self.fill_by_figure(figure)

    def one_line(self):
        i = len(self.field) - 1
        while i >= 0:
            line = True
            for k in range(len(self.field[i])):
                line = line and self.field[i][k].is_fill
            if line:
                self.score += 1
                for p in range(i, 0, -1):
                    for q in range(len(self.field[p])):
                        self.field[p][q].is_fill = self.field[p - 1][q].is_fill
                for column in self.field[0]:
                    column.is_fill = False
                i += 1
            i -= 1
        return self.score
                

                