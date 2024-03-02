import figure
'''
Этот класс создает фигуру квдарат
'''
class Square(figure.Figure):
    def __init__(self, row, column, speed):
        super().__init__(row, column, speed)
        self.width = 2
        self.height = 2
        self.structure = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.prev_structure = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.max_indeces = [1, 1]
    # косяк, надо придумать как убрать отсюда пустой метод
    def rotation(self):
        pass