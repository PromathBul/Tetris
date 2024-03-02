import figure

class Straight_line(figure.Figure):
    def __init__(self, row, column, speed, config):
        super().__init__(row, column, speed)
        self.width = 4
        self.height = 1
        self.structure = [(0, 0), (0, 1), (0, 2), (0, 3)]
        self.prev_structure = [(0, 0), (0, 1), (0, 2), (0, 3)]
        self.max_indeces = [0, 0, 0, 0]
        self.config = config

    def rotation(self):
        self.prev_structure = self.structure
        if not self.config:
            self.width = 1
            self.height = 4
            self.structure = [(0, 0), (1, 0), (2, 0), (3, 0)]
            self.max_indeces = [3]
        else:
            self.width = 4
            self.height = 1
            self.structure = [(0, 0), (0, 1), (0, 2), (0, 3)]
            self.max_indeces = [0, 0, 0, 0]

        self.config = (self.config + 1) % 2