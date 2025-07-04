import unittest
import numpy as np

# Import from sibling directory.
import sys
import os

# Add the parent directory (containing differintP) to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from differintP.core import Gamma
from differintP.solvers import PCsolver
from differintP.functions import MittagLeffler


PC_x_power = np.linspace(0, 1, 100) ** 5.5

# Get FODE function for solving.
PC_func_power = lambda x, y: 1 / 24 * Gamma(5 + 1.5) * x**4 + x ** (8 + 2 * 1.5) - y**2
PC_func_ML = lambda x, y: y


class TestSolvers(unittest.TestCase):
    """Tests for the correct solution to the equations."""

    def test_PC_solution_three_halves(self):
        self.assertTrue(
            (
                np.abs(PCsolver([0, 0], 1.5, PC_func_power, 0, 1, 100) - PC_x_power)
                <= 1e-2
            ).all()
        )

    def test_PC_solution_ML(self):
        xs = np.linspace(0, 1, 100)
        ML_alpha = MittagLeffler(5.5, 1, xs**5.5)
        self.assertTrue(
            (
                np.abs(PCsolver([1, 0, 0, 0, 0, 0], 5.5, PC_func_ML) - ML_alpha) <= 1e-2
            ).all()
        )

    def test_PC_solution_linear(self):
        xs = np.linspace(0, 1, 100)
        self.assertTrue(
            (
                np.abs(PCsolver([1, 1], 1.5, lambda x, y: y - x - 1) - (xs + 1)) <= 1e-2
            ).all()
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

    # Ensure all docstring examples work.
    import doctest

    doctest.testmod()
