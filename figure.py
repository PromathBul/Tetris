from constants import *
from pygame import *

class Figure():
    def __init__(self, row, column, speed):
        self.structure = []
        self.max_indeces = []
        self.column = column
        self.row = row
        self.width = 0
        self.height = 0
        self.speed = speed

    def move_down(self, field):
        key_pressed = key.get_pressed()
        if not self.stop(field):
            self.prev_structure = self.structure
            self.row += 1
            if key_pressed[DOWN]:
                self.speed = FPS
        return self.speed


    def update(self, field):
        row = self.row
        column = self.column
        key_pressed = key.get_pressed()

        if self.row != AMOUNT_HEIGHT - self.height:
            if key_pressed[LEFT] and not self.is_left_occupied(field):
                self.prev_structure = self.structure
                self.column -= 1
            if key_pressed[RIGHT] and not self.is_right_occupied(field):
                self.prev_structure = self.structure
                self.column += 1

        if key_pressed[ROTATION]:
            self.rotation()

        return (row, column)
    
    def stop(self, field):
        if self.row >= AMOUNT_HEIGHT - self.height:
            return True

        for i in range(self.column, self.column + self.width):
            if field.field[self.row + self.max_indeces[i - self.column] + 1][i].is_fill:
                return True
        return False
    
    def is_right_occupied(self, field):
        is_border = self.column == AMOUNT_WIDTH - self.width
        is_figure = False
        if not is_border:
            for i in range(self.row, self.row + self.height):
                if field.field[i][self.column + self.width].is_fill:
                    is_figure = True
        return is_border or is_figure
    
    def is_left_occupied(self, field):
        is_border = self.column == 0
        is_figure = False
        if not is_border:
            for i in range(self.row, self.row + self.height):
                if field.field[i][self.column - 1].is_fill:
                    is_figure = True
        return is_border or is_figure
