import json
import requests

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' 
PACKAGE_NAME = 'koios-pythion' 
AUTHOR = 'Quixote Stake Pool'
AUTHOR_EMAIL = 'quixotepool@proton.me'
URL = 'https://github.com/QuixoteSystems'

LICENSE = 'MIT'
DESCRIPTION = 'Aquí debes incluir una descripción corta de la librería' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'listado de librerias'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
