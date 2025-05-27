from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    description='Classer for å sammenligne plot og plotte tidsserieplot',
    python_requires='>=3.6',

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)