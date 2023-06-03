from setuptools import setup
import sys

classifiers = [
  "Operating System :: OS Independent",
  "License :: OSI Approved :: Apache Software License",
  "Programming Language :: Python :: 3",
]

CURRENT_VERSION = sys.version_info[:2]
REQUIRED_VERSION = (3, 7)

if CURRENT_VERSION < REQUIRED_VERSION:
    sys.stderr.write(
        f"""Current python version ({CURRENT_VERSION[0]}.{CURRENT_VERSION[1]}) is lower than required ({REQUIRED_VERSION[0]}.{REQUIRED_VERSION[1]})"""
    )

setup(
    name="curtely",
    version="0.0.3",
    description="a 🧑‍💻Telegram API🧑‍💻 wrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CURVoid/curtely",
    author="VOID",
    license="APACHE 2.0", 
    keywords=["telegram", "api", "curtely", "messenger"],
    package_dir={"": "curtely"},
    py_modules=["curtely"],
    classifiers=classifiers,
)   