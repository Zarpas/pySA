from setuptools import find_packages,setup

requirements = open('requirements.txt')

setup(

    name = "pySA",
    version = "0.1",
    author = "Sri Sanketh Uppalapati",
    description = ("Structural Analysis in python"),
    platform = 'any',
    packages = find_packages(),
    install_requires = requirements.read().splitlines(),
    entry_points = {
        "console_scripts": [ "pySA = project.main:main"]
        }
)
