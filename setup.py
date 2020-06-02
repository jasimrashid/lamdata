# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lamdata-jasim-rashid", # the name that you will install via pip
    version="1.0",
    author="Jasim Rashid",
    author_email="jasim.rashid@gmail.com",
    description="My first package installation",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jasimrashid/lamdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)

