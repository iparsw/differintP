import unittest
import numpy as np

# Import from sibling directory.
import sys
import os

# Add the parent directory (containing differintP) to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from differintP.functions import *

# Define constants to be used in tests.
poch_first_argument = 1
poch_second_argument = 5
poch_true_answer = 120


class HelperTestCases(unittest.TestCase):
    """Tests for helper functions."""

    def test_pochhammer(self):
        self.assertEqual(
            poch(poch_first_argument, poch_second_argument), poch_true_answer
        )
        self.assertEqual(poch(-1, 3), 0)
        # self.assertEqual(poch(-1.5, 0.5), np.inf)
        self.assertEqual(np.round(poch(1j, 1), 3), 0.000 + 1.000j)
        self.assertEqual(poch(-10, 2), 90)


    """ Unit tests for Mittag-Leffler function. """

    def test_ML_cosh_root(self):
        xs = np.arange(10, 0.1)
        self.assertTrue(
            (
                np.abs(
                    MittagLeffler(2, 1, xs, ignore_special_cases=True)
                    - np.cosh(np.sqrt(xs))
                )
                <= 1e-3
            ).all()
        )

    def test_ML_exp(self):
        xs = np.arange(10, 0.1)
        self.assertTrue(
            (
                np.abs(MittagLeffler(1, 1, xs, ignore_special_cases=True) - np.exp(xs))
                <= 1e-3
            ).all()
        )

    def test_ML_geometric(self):
        xs = np.arange(1, 0.05)
        self.assertTrue(
            (
                np.abs(
                    MittagLeffler(0, 1, xs, ignore_special_cases=True) - 1 / (1 - xs)
                )
                <= 1e-3
            ).all()
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

    # Ensure all docstring examples work.
    import doctest

    doctest.testmod()
