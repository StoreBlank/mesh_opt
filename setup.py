from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext


# Define the C++ extension module
ext_modules = [
    Pybind11Extension(
        name='mesh_opt',  # Module name
        sources=['mesh_opt.cc'],  # Source file(s)
        include_dirs=['trimesh2/include'],
        library_dirs=['trimesh2/lib.Linux64', '/usr/local/lib'],
        libraries=['trimesh', 'cholmod'],
        extra_compile_args=['-fopenmp', '-fPIC', '-std=c++14', '-O3'],
    ),
]

# Call setup to build the extension
setup(
    name='mesh_opt',
    version='0.1',
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
    install_requires=[
        'numpy',
        'pybind11',
    ],
    zip_safe=False,
)
