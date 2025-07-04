import unittest
import numpy as np

# Import from sibling directory.
import sys
import os

# Add the parent directory (containing differintP) to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from differintP.core import *
from differintP.functions import MittagLeffler

from .__init__ import test_N

# Define constants to be used in tests.
size_coefficient_array = 20
sqrtpi2 = 0.88622692545275794
truevaluepoly = 0.94031597258
truevaluepoly_caputo = 1.50450555  # 8 / (3 * np.sqrt(np.pi))
truevaluepoly_caputo_higher = 2 / Gamma(1.5)


# Get SQRT results for checking accuracy.
GL_r = GL(0.5, lambda x: np.sqrt(x), 0, 1, test_N)
GL_result = GL_r[-1]
GL_length = len(GL_r)

GLI_r = GLI(0.5, lambda x: np.sqrt(x), 0, 1, test_N)
GLI_result = GLI_r[-1]
GLI_length = len(GLI_r)

RL_r = RL(0.5, lambda x: np.sqrt(x), 0, 1, test_N)
RL_result = RL_r[-1]
RL_length = len(RL_r)


# --- Exponential function ---
# For f(x) = exp(x), the fractional derivative of order alpha at x = 1:
# D^{alpha} e^{x} |_{x=1} = exp(1) / Gamma(1 - alpha)
alpha_exp = 0.5
groundtruth_exp_expr = "exp(1) * sum_{k=0}^∞ 1^k / Gamma(k + 1 - 0.5)"
groundtruth_exp = MittagLeffler(1, 1 - 0.5, np.array([1]))[0]


# --- Sine function ---
# D^{alpha} sin(x) = sin(x + alpha * pi/2)
# For alpha=0.5, x=1:
# Analytical: sin(1 + 0.5 * pi/2)
alpha_sin = 0.5
groundtruth_sin_expr = "sin(1 + alpha_sin * pi/2)"
groundtruth_sin = np.sin(1 + alpha_sin * np.pi / 2)






class TestAlgorithmsAccuray(unittest.TestCase):
    """Tests for algorithm accuracy."""

    #######################
    # GLpoint
    #######################

    # sqrt
    def test_GLpoint_sqrt_accuracy(self):
        self.assertTrue(
            abs(GLpoint(0.5, lambda x: x**0.5, 0.0, 1.0, 1024) - sqrtpi2) <= 1e-3
        )

    # x**2 - 1
    def test_GLpoint_accuracy_polynomial(self):
        self.assertTrue(
            abs(GLpoint(0.5, lambda x: x**2 - 1, 0.0, 1.0, 1024) - truevaluepoly)
            <= 1e-3
        )

    # exp
    def test_GLpoint_accuracy_exp(self):
        """Test GLpoint on f(x) = exp(x), alpha=0.5. Analytical: exp(1)/Gamma(0.5)"""
        val = GLpoint(alpha_exp, np.exp, 0, 1, 1024)
        self.assertTrue(abs(val - groundtruth_exp) < 1e-3)


    #######################
    # GL
    #######################

    # sqrt
    def test_GL_accuracy_sqrt(self):
        self.assertTrue(abs(GL_result - sqrtpi2) <= 1e-4)

    # x**2 - 1
    def test_GL_accuracy_polynomial(self):
        self.assertTrue(
            abs(GL(0.5, lambda x: x**2 - 1, 0.0, 1.0, 1024)[-1] - truevaluepoly)
            <= 1e-3
        )

    # exp
    def test_GL_accuracy_exp(self):
        """Test GL on f(x) = exp(x), alpha=0.5. Analytical: exp(1)/Gamma(0.5)"""
        val = GL(alpha_exp, np.exp, 0, 1, 1024)[-1]
        # print(f"exp: numeric={val}, expected={groundtruth_exp}")
        self.assertTrue(abs(val - groundtruth_exp) < 1e-3)


    #######################
    # GLI
    #######################

    # sqrt
    def test_GLI_accuracy_sqrt(self):
        self.assertTrue(abs(GLI_result - sqrtpi2) <= 1e-4)

    # x**2 - 1
    def test_GLI_accuracy_polynomial(self):
        self.assertTrue(
            abs(GLI(0.5, lambda x: x**2 - 1, 0.0, 1.0, 1024)[-1] - truevaluepoly)
            <= 6e-3 # low accuracy
        )

    # exp
    def test_GLI_accuracy_exp(self):
        """Test GLI on f(x) = exp(x), alpha=0.5. Analytical: Gamma(0.5)"""
        val = GLI(alpha_exp, np.exp, 0, 1, 1024)[-1]
        # print(f"exp: numeric={val}, expected={groundtruth_exp}")
        self.assertTrue(abs(val - groundtruth_exp) < 5e-3) # low accuracy
        # Abs error: 0.00481


    #######################
    # RLpoint
    #######################

    # sqrt
    def test_RLpoint_sqrt_accuracy(self):
        self.assertTrue(
            abs(RLpoint(0.5, lambda x: x**0.5, 0.0, 1.0, 1024) - sqrtpi2) <= 1e-3
        )

    # poly x**2 - 1
    def test_RLpoint_accuracy_polynomial(self):
        self.assertTrue(
            abs(RLpoint(0.5, lambda x: x**2 - 1, 0.0, 1.0, 1024) - truevaluepoly)
            <= 1e-2
        )

    # exp
    def test_RLpoint_accuracy_exp(self):
        """Test RLpoint on f(x) = exp(x), alpha=0.5. Analytical: exp(1)/Gamma(0.5)"""
        val = RLpoint(alpha_exp, np.exp, 0, 1, 1024)
        self.assertTrue(abs(val - groundtruth_exp) < 1e-3)


    #######################
    # RL
    #######################

    # sqrt
    def test_RL_accuracy_sqrt(self):
        self.assertTrue(abs(RL_result - sqrtpi2) <= 1e-4)

    # x**2 - 1
    def test_RL_accuracy_polynomial(self):
        self.assertTrue(
            abs(RL(0.5, lambda x: x**2 - 1, 0.0, 1.0, 1024)[-1] - truevaluepoly)
            <= 1e-3
        )

    # exp
    def test_RL_accuracy_exp(self):
        """Test RL on f(x) = exp(x), alpha=0.5. Analytical: exp(1)/Gamma(0.5)"""
        val = RL(alpha_exp, np.exp, 0, 1, 1024)[-1]
        # print(f"exp: numeric={val}, expected={groundtruth_exp}")
        self.assertTrue(abs(val - groundtruth_exp) < 1e-3)

    #######################
    # Caputo 1p
    #######################

    # sqrt
    def test_CaputoL1point_accuracy_sqrt(self):
        self.assertTrue(
            abs(CaputoL1point(0.5, lambda x: x**0.5, 0, 1.0, 1024) - sqrtpi2) <= 1e-2
        )

    # x**2 - 1
    def test_CaputoL1point_accuracy_polynomial(self):
        self.assertTrue(
            abs(
                CaputoL1point(0.5, lambda x: x**2 - 1, 0, 1.0, 1024)
                - truevaluepoly_caputo
            )
            <= 1e-3
        )

    # exp
    def test_CaputoL1point_accuracy_exp(self):
        """Test RLpoint on f(x) = exp(x), alpha=0.5. Analytical: exp(1)/Gamma(0.5)"""
        val = CaputoL1point(alpha_exp, np.exp, 0, 1, 1024)
        self.assertTrue(abs(val - groundtruth_exp) < 0.6) # really bad accuracy


    #######################
    # Caputo 2p
    #######################

    # x**2 - 1
    def test_CaputoL2point_accuracy_polynomial(self):
        self.assertTrue(
            abs(
                CaputoL2point(1.5, lambda x: x**2, 0, 1.0, 1024)
                - truevaluepoly_caputo_higher
            )
            <= 1e-1
        )

    #######################
    # Caputo 2pC
    #######################

    # x**2 (a = 1.5)
    def test_CaputoL2Cpoint_accuracy_polynomial_higher(self):
        self.assertTrue(
            abs(
                CaputoL2Cpoint(1.5, lambda x: x**2, 0, 1.0, 1024)
                - truevaluepoly_caputo_higher
            )
            <= 1e-1
        )

    # x**2 - 1
    def test_CaputoL2Cpoint_accuracy_polynomial(self):
        self.assertTrue(
            abs(
                CaputoL2Cpoint(0.5, lambda x: x**2, 0, 1.0, 1024) - truevaluepoly_caputo
            )
            <= 1e-3
        )

    # exp
    def test_CaputoL2Cpoint_accuracy_exp(self):
        """Test RLpoint on f(x) = exp(x), alpha=0.5. Analytical: exp(1)/Gamma(0.5)"""
        val = CaputoL2Cpoint(alpha_exp, np.exp, 0, 1, 1024)
        self.assertTrue(abs(val - groundtruth_exp) < 2) # unusable


class TestAlgorithmsGeneral(unittest.TestCase):
    """Tests for correct size of algorithm results."""

    def test_GL_result_length(self):
        self.assertEqual(GL_length, test_N)

    def test_GLI_result_length(self):
        self.assertEqual(GLI_length, test_N)

    def test_RL_result_length(self):
        self.assertEqual(RL_length, test_N)

    def test_RL_matrix_shape(self):
        self.assertTrue(np.shape(RLmatrix(0.4, test_N)) == (test_N, test_N))

    def test_GL_binomial_coefficient_array_size(self):
        self.assertEqual(
            len(GLcoeffs(0.5, size_coefficient_array)) - 1, size_coefficient_array
        )



if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

    # Ensure all docstring examples work.
    import doctest

    doctest.testmod()
