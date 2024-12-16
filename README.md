The pybind version of https://w3.impa.br/~diego/software/NehEtAl05/, which implements the algorithm in the paper:

>**Efficiently Combining Positions and Normals for Precise 3D Geometry**  
Nehab, D.; Rusinkiewicz, S.; Davis, J.; Ramamoorthi, R.
ACM Transactions on Graphics - SIGGRAPH 2005  
Los Angeles, California, July 2005, Volume 24, Issue 3, pp. 536-543

## Installation:

1. Install [cholmod](https://developer.nvidia.com/cholmod).
2. Build `trimesh2` in this repo, we've modified the makefiles.
3. run `pip install .`, you may need to change lib paths in `setup.py` due to platform.

## Usage

See examples in `test`
