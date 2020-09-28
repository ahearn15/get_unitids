import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.95'
PACKAGE_NAME = 'unitids'
AUTHOR = 'Adam Hearn'
AUTHOR_EMAIL = 'adam.hearn@collegetransitions.com'
URL = 'https://github.com/ahearn15/get_unitids'

LICENSE = 'MIT License'
DESCRIPTION = 'Python module to imputate IPEDS unitids from non-matching institution names'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'nltk',
      'textblob',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
