import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyalgen",
    version="0.0.5",
    description="Minimal python library for genetic algorithm",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/amalshaji/pyalgen",
    author="Amal Shaji",
    author_email="amalshajid@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pyalgen"],
    include_package_data=True,
    install_requires=["numpy", "tqdm"],
)
