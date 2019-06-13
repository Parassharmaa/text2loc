from setuptools import setup
import os

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md').read()

setup(name='text2loc',
      version='0.0.3',
      description='Extract countries, regions and cities from text',
      long_description=long_description,
      author='Paras Sharma',
      author_email='',
      license='MIT',
      packages=['text2loc'],
      install_requires=[
          'numpy', 'nltk', 'newspaper3k', 'jellyfish', 'pycountry'
      ],
      scripts=['text2loc/bin/geograpy-nltk'],
      package_data={
          'text2loc': ['data/*.csv'],
      },
      zip_safe=False)