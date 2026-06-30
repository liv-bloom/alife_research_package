# Limitations

## Scope limitations
This package claims structural deformation in the Physarum model based on traces, but does not claim biological accuracy to real slime mold.

## Computational limitations
Can be run on a standard CPU. Runs are limited to 1000 steps for quick reproduction.

## Reproducibility limitations
Due to floating-point order of operations in parallel/vectorized updates, the exact hash (R5D) may vary across architectures. Statistical reproduction (R5S) is required for the trace overlap metrics.

## Data limitations
The full 1.05M traces are not included to save space; a statistically representative sample (1000 traces) is used for the reproduction package.
