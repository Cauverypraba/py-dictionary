from setuptools import find_packages, setup

setup(
    name='PyStore',
    # packages = find_packages(include=['PyLibrary']),
    packages=['lib'],
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    test_suite='tests',
)
