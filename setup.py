import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Algorithms-Python",
    version="1.0.0",
    author="Pavel Dimitrov",
    author_email="pavelsd@abv.bg",
    description=("A library that solves math related problems."),
    license="GPL",
    url="https://github.com/Pavaka/Algorithms-Python",
    # packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)