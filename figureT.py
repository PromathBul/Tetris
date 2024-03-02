import figure

class FigureT(figure.Figure):
    def __init__(self, row, column, speed, config):
        super().__init__(row, column, speed)
        self.width = 3
        self.height = 2
        self.structure = [(0, 1), (1, 0), (1, 1), (1, 2)]
        self.prev_structure = [(0, 1), (1, 0), (1, 1), (1, 2)]
        self.max_indeces = [1, 1, 1]
        self.config = config

    def rotation(self):
        self.prev_structure = self.structure
        if not self.config % 2:
            self.width = 2
            self.height = 3
            if self.config == 0:
                self.structure = [(0, 1), (1, 0), (1, 1), (2, 1)]
                self.max_indeces = [1, 2]
            else:
                self.structure = [(0, 0), (1, 0), (1, 1), (2, 0)]
                self.max_indeces = [2, 1]
        else:
            self.width = 3
            self.height = 2
            if self.config == 1:
                self.structure = [(0, 0), (0, 1), (0, 2), (1, 1)]
                self.max_indeces = [0, 1, 0]
            else:
                self.structure = [(0, 1), (1, 0), (1, 1), (1, 2)]
                self.max_indeces = [1, 1, 1]
        
        self.config = (self.config + 1) % 4
