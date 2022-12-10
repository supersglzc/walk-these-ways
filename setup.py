from setuptools import find_packages
from distutils.core import setup

setup(
    name='go1_gym',
    version='1.0.0',
    author='Gabriel Margolis',
    license="BSD-3-Clause",
    packages=find_packages(),
    author_email='gmargo@mit.edu',
    description='Toolkit for deployment of sim-to-real RL on the Unitree Go1.',
    install_requires=['ml_logger==0.8.71',
                      'jaynes==0.8.11',
                      'gym',
                      'tqdm',
                      'matplotlib',
                      ]
)
