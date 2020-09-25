
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="notebookc",
    version="0.0.1",
    author="Adam Hearn",
    author_email="adam.hearn@collegetransitions.com",
    description="Matches institutions to retreive IPEDS UnitIds",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/get_unitids/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)