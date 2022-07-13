from importlib.metadata import entry_points
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
  name="cli-notes",
  version='1.0.0',
  description='Quick way of taking notes inside the terminal',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="HashedDev",
  author_email="notexistent@example.com",
  classifiers=[
    "Programming Language :: Python :: 3.10",
  ],
  packages=find_packages(where="src"),
  python_required=">=3.8, <4",
  entry_points={
    "console_scripts": [
      "note=note:main"
    ]
  }
)