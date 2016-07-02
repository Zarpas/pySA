from setuptools import find_packages,setup

requirements = open('requirements.txt')

setup(

    name = "py_SA",
    version = "1.0",
    author = "Sri Sanketh Uppalapati",
    author_email = "iamjustice443@gmail.com",
    description = ("Structural Analysis in python"),
    keywords = "Shear force Bending moment",
    url = "https://github.com/pySA-dev/pySA",
    license = "MIT",
    packages = find_packages(exclude=["build.*"]),
    install_requires = requirements.read().splitlines(),
    entry_points = {
        "console_scripts": [ "pySA = tools.main:main"]
        }
)
