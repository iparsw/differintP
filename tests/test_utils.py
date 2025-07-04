import unittest
import numpy as np

# Import from sibling directory.
import sys
import os

# Add the parent directory (containing differintP) to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from differintP.utils import * # type: ignore
from .__init__ import test_N




stepsize = 1 / (test_N - 1)

# Testing if callable functions and arrays of function values will work.
checked_function1, test_stepsize1 = functionCheck(
    lambda x: 2 * np.exp(3 * x) * x - x**2 + x - 5, 0, 1, test_N
)
checked_function2, test_stepsize2 = functionCheck(np.ones(test_N), 0, 1, test_N)


class UtilsTestCases(unittest.TestCase):
    def test_isInteger(self):
        self.assertTrue(isInteger(1))
        self.assertTrue(isInteger(1.0))
        self.assertTrue(isInteger(1 + 0j))
        self.assertFalse(isInteger(1.1))
        self.assertFalse(isInteger(1.1 + 0j))
        self.assertFalse(isInteger(1 + 1j))

    def test_isPositiveInteger(self):
        self.assertTrue(isPositiveInteger(1))
        self.assertFalse(isPositiveInteger(1.1))
        self.assertFalse(isPositiveInteger(-1))

    def test_functionCheck(self):
        self.assertEqual(len(checked_function1), test_N)
        self.assertEqual(len(checked_function2), test_N)

        # Make sure it treats defined functions and arrays of function values the same.
        self.assertEqual(len(checked_function1), len(checked_function2))
        self.assertEqual(test_stepsize1, stepsize)
        self.assertEqual(test_stepsize2, stepsize)
        self.assertEqual(test_stepsize1, test_stepsize2)


    def test_checkValues(self):
        with self.assertRaises(AssertionError):
            checkValues(0.1, 0, 1, 1.1) # type: ignore
        with self.assertRaises(AssertionError):
            checkValues(0.1, 1j, 2, 100) # type: ignore
        with self.assertRaises(AssertionError):
            checkValues(0.1, 1, 2j, 100) # type: ignore
        with self.assertRaises(AssertionError):
            checkValues(0.1, 0, 1, -100)
        with self.assertRaises(AssertionError):
            checkValues(1 + 1j, 0, 1, 100) # type: ignore
        checkValues(0.5, 0, 1, 100, support_complex_alpha=True)
        checkValues(1 + 1j, 0, 1, 100, support_complex_alpha=True) # type: ignore
        alpha_vals = np.array([0.1, 0.2])
        domain_vals = np.array([0.1, 1, 2.0, -1])
        num_vals = np.array([1.0, 100.0])
        [
            [
                [
                    [
                        checkValues(alpha, domain_start, domain_end, num_points)
                        for alpha in alpha_vals
                    ]
                    for domain_start in domain_vals
                ]
                for domain_end in domain_vals
            ]
            for num_points in num_vals
        ]