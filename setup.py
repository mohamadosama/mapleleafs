from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mapleleafs/__init__.py
from mapleleafs import __version__ as version

setup(
	name="mapleleafs",
	version=version,
	description="mapleleafs customizations",
	author="mosama",
	author_email="mohamaed.muslim1400@fgmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
