from collections import Counter
from datetime import datetime
import numpy as np
import logging
import re

logger = logging.getLogger(__name__)
logging.basicConfig(filename='pipe_system.log', filemode='w', level=logging.DEBUG)

class PipeSystem:

    SYMBOLS = ['═', '║', '╔', '╗', '╚', '╝', '╠', '╣', '╦', '╩']
    SHAPES = ['left_right', 'top_bottom', 'bottom_right', 'bottom_left', 'top_right', 'top_left', 't_right', 't_left', 't_down', 't_up']

    SOURCE = "*" # asterisk represents waterflow origin
    SINK = re.compile('[A-Z]') # Any single uppercase letter represents a sink
    PIPES = {k: v for k, v in zip(SYMBOLS, SHAPES)} # Mapping symbols to shapes
    DATA = []

    def __init__(self) -> None: # No need to pass any arguments
        if self.DATA == []:
            logger.error(f"{datetime.now()} - No data loaded")
            raise AttributeError
        pass

    @classmethod
    def load_data(cls, filepath: str): # Class method to load data from file
        with open(filepath, 'r') as f:
            lines = f.readlines()
            data = list(map(lambda x: x.strip().split(), lines))
            pipe = list(map(lambda x: x[0], data))
            coordinates = list(map(lambda x: (x[1], x[2]), data))
            data = list(zip(pipe, coordinates))
            cls.DATA.extend(data)

            logger.info(f"{datetime.now()} - Data loaded from {filepath}")

    def grid_cell_data(self): # Returns the number of occupied cells, empty cells, and their coordinates
        coordinates_list = [y for x, y in self.DATA]
        x, y = zip(*coordinates_list)
        x, y = np.array(x, dtype=int), np.array(y, dtype=int)
        cells, coordinates = len(coordinates_list), (x, y)
        empty_cells = int(np.prod([max(coordinates[i]) for i in range(len(coordinates))])) - cells
        return cells, abs(empty_cells), coordinates

    def component_inv(self): # Returns the inventory of components
        components = ["S" if self.SINK.match(x[0]) else x[0] for x in self.DATA]
        inventory = Counter(components)
        return inventory

    def display_system_grid(self):
        coordinates = self.grid_cell_data()[2]


if __name__ == "__main__":

    PipeSystem.load_data("data.txt")
    pipe_system = PipeSystem()

    print(pipe_system.grid_cell_data())
    print(pipe_system.component_inv())

    grid = np.meshgrid(*pipe_system.grid_cell_data()[2])
    print(grid)
