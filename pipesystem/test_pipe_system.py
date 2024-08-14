from numpy.core.multiarray import empty_like
from pipe_system import PipeSystem # Import the PipeSystem class
import numpy as np # Import numpy for array operations


class TestPipeSystem:
    PipeSystem.load_data("data.txt")
    pipe_system = PipeSystem()

    def test_load_data(self):
        """
        This test checks if the DATA attribute of the pipe system module is not empty after calling load_data.
        It also checks if all elements in DATA are tuples consisting of a string and a tuple with 2 integers.
        """
        assert \
        self.pipe_system.DATA != [] and \
        all(isinstance(x, tuple) for x in self.pipe_system.DATA if len(x) == 2) and \
        all(isinstance(pipe, str) for pipe, coordinates in self.pipe_system.DATA) and \
        all(isinstance(coordinates, tuple) for pipe, coordinates in self.pipe_system.DATA if len(coordinates) == 2 and \
        all(isinstance(x, int) for x in coordinates))

    def test_grid_cell_data(self):
        """
        This test checks if the occupied_cells method returns the correct number of occupied cells and their coordinates.
        """
        occupied_cells, empty_cells, coordinates = self.pipe_system.grid_cell_data()
        assert \
        occupied_cells == len(self.pipe_system.DATA) and \
        isinstance(coordinates, tuple) and \
        all(isinstance(x, np.ndarray) for x in coordinates)

    def test_component_inv(self):
        """
        This test checks if the component_inv method returns the correct inventory of components.
        """
        inventory = self.pipe_system.component_inv()
        assert \
        isinstance(inventory, dict) and \
        len(inventory) == 12 and \
        all(isinstance(k, str) for k in inventory.keys()) and \
        all(isinstance(v, int) for v in inventory.values())

    def test_display_system_grid(self):
        pass
