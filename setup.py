from setuptools import setup, find_packages

from our_package import __version__

setup(
    name="our_package",
    version=__version__,
    description="Toy package for Programming for Life Sciences course",
    url="https://github.com/zavolanlab/programming-for-life-sciences",
    author="Zavolan Lab, Biozentrum, University of Basel",
    author_email="zavolab-biozentrum@unibas.ch",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="teaching demo example",
    packages=find_packages(),
    setup_requires=[
        "setuptools_git == 1.2",
    ],
)
