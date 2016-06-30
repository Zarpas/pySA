from setuptools import find_packages,setup

requirements = open('requirements.txt')

setup(

    name = "pySA",
    version = "0.0.1",
    author = "Sri Sanketh Uppalapati",
    author_email = "iamjustice443@gmail.com",
    description = ("Structural Analysis in python"),
    keywords = "Shear force Bending moment",
    url = "https://github.com/pySA-dev/pySA",
    packages = find_packages(),
    install_requires = requirements.read().splitlines(),
    entry_points = {
        "console_scripts": [ "pySA = tools.main:main"]
        }
)
