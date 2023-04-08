import glob
import os
import sys
from setuptools import find_packages, setup

additional_files = []
for filename in glob.iglob('./pwtdata/**', recursive=True):
    if '.dta.gz' in filename:
        additional_files.append(filename.replace('./pwtdata/', ''))


setup(
    name='pwtdata',
    version='0.3.2',
    author=['Tetsu Haruyama', 'Kenji Sato'],
    author_email=['haruyama@econ.kobe-u.ac.jp', 'kenji@kenjisato.jp'],
    packages=find_packages(),
    package_dir={'pwtdata': './pwtdata'},
    include_package_data=True,
    package_data={'pwtdata': additional_files},
    install_requires=['pandas'],
    url='https://github.com/kenjisato/pwtdata',
    license='LICENSE',
    description='Python package containing the Penn World Table dataset.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['data', 'Penn World Table']
)
