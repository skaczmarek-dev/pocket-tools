from setuptools import setup, find_packages

setup(
    name='pocket-tools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    description='A Python toolkit to manage and organize Pocket API data',
    author='Your Name',
    license='MIT',
    python_requires='>=3.6',
)