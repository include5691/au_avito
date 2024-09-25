from setuptools import setup, find_packages

setup(
    name='au_avito',
    version='0.1.0',
    author='Andrey Pshenitsyn',
    description='Avito automatization library',
    packages=find_packages(),
    install_requires=[
        'requests',
        "python-dotenv"
    ],
)