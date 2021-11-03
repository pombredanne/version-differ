#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Nasif Imtiaz",
    author_email="nasifimtiaz88@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Accurate diffing between two versions of a package",
    entry_points={
        "console_scripts": [
            "version_differ=version_differ.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="version_differ",
    name="version_differ",
    packages=find_packages(include=["version_differ", "version_differ.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/nasifimtiazohi/version_differ",
    version="version='0.7.1'",
    zip_safe=False,
)
