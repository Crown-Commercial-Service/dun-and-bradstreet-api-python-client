"""
A python client for D&B Direct+ API.
"""
import re
import ast
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('dnbclient/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='dun-and-bradstreet-api-python-client',
    version=version,
    url='https://github.com/alphagov/dun-and-bradstreet-api-python-client',
    license='MIT',
    author='GDS Developers',
    description='A python client for D&B Direct+ API.',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires="~=3.6",
)
