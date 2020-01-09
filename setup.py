"""
A python client for D&B Direct+ API.
"""
import re
import ast
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('direct_plus_python_client/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

requires = [
    'requests<3,>=2.22.0',
]
test_requirements = [
    'coveralls==1.8.1',
    'flake8==3.7.7',
    'pytest==4.6.3',
    'pytest-cov==2.8.1',
]

setup(
    name='direct-plus-python-client',
    version=version,
    url='https://github.com/alphagov/direct-plus-python-client',
    license='MIT',
    author='GDS Developers',
    description='A python client for D&B Direct+ API.',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    tests_require=test_requirements,
    extras_require={
        'test': test_requirements,
    },
    setup_requires=['pytest-runner'],
    python_requires='~=3.6',
)
