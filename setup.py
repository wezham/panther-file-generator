from setuptools import setup, find_packages

setup(
    name="panther-file-generator",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["panther-generate=panther.run:main"],
    },
    package_data={"panther": ["data/*.yml", "data/*.py"]},
    include_package_data=True,
)
