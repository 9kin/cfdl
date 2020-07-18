#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "rich",
    "jinja2",
    "lxml",
    "peewee",
    "tqdm",
    "aiohttp==3.6.2",
    "pdfkit",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="@9kin",
    author_email="cf2html.github@mail.ru",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="download task (tutorials) with asyncio",
    entry_points={"console_scripts": ["kiq = codeforcesdl.cli:main",],},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="codeforces-dl",
    name="codeforces-dlqq",
    packages=find_packages(include=["codeforces-dl"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/9kin/codeforces-dl",
    version="0.1.0",
    zip_safe=False,
)


__all__ = [
    "history",
    "readme",
    "requirements",
    "setup_requirements",
    "test_requirements",
]
