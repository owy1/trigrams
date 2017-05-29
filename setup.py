"""This is the Setup."""
from setuptools import setup


setup(
    name='trigrams',
    description='This takes a text file and outputs similar text but random',
    version='0.1',
    author='Ely and Ophelia',
    license='MIT',
    py_modules=['trigrams'],
    package_dir={'': 'src'},
    extras_require={'testing': ['pytest', 'tox']}
)
