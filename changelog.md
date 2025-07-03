# differint changelog (parent package)

## 0.1

2017-11-22

### Added

  - 'GL' - calculate GL differintegral

## 0.2

2017-11-24

### Added

  - 'RLtrap' - calculate RL differintegral using trapezoid rule
  - 'RLcoeff' - calculate coefficients for use in 'RLtrap'
  - 'checkvalues' - check for valid inputs for algorithms

### Modified

  - 'GL' - now works with 'checkvalues' to validate inputs

2018-01-29

### Added

  - 'GLI' - calculate improved GL differintegral
  - Unit tests for all core and auxiliary functions
  - 'GLIinterpolat' calculate interpolation coefficients for GLI algorithm
  - 'isInteger' for integer typechecking
  - 'functionCheck' for checking function input
  - 'test_func' for unittesting
  - 'RL' for calculating RL algorithm over array of function values
  - 'GL' for calculating GL algorithm over array of function values

### Modified

  - 'GL' now uses DFT for faster computation
  - 'GL' changed to 'GLpoint'
  - 'RLtrap' now called 'RLpoint'

2018-05-03

### Added

  - 'CRONE' - calcualte GL differintegral operator using CRONE

2019-12-13

### Added

  - Added readme to github repository
  - Include future print function support

2022-11-13

### Added

  - 'isPositiveInteger' - check if a number is and integer and positive
  - 'PCsolver' - solve initial value fractional ODEs using the predictor-corrector method
  - Caputo differintegral using the L1, L2, and L2C methods

### Modified

 - Changed the way `isInteger` checks the given value
 - resolved bug in 'CRONE' method
 - updated Pochhammer symbol implementation to support a larger domain of inputs
 - 'checkValues' now supports numpy data types
 - 'Gamma' now uses `math.gamma` for real values to speed up computation


# differintP Changelog

### 0.0.2 (7/3/2025)

- Optimized core functions: `GL`, `GLpoint`, `RL`, and `RLpoint`
- Added GPU-accelerated `GL` (`GL_gpu`) via [CuPy](https://cupy.dev/) (optional dependency)
- Modernized package setup and build system
