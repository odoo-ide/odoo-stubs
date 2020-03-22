import os
from setuptools import setup


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for f in files:
            stubs.append(os.path.relpath(os.path.join(root, f), package))
    return {package: stubs}


setup(
    name="odoo12-stubs",
    url="https://github.com/trinhanhngoc/odoo-stubs",
    author="Trinh Anh Ngoc",
    author_email="atw1990@gmail.com",
    version="0.0.1",
    package_data=find_stubs("odoo-stubs"),
    packages=["odoo-stubs"]
)
