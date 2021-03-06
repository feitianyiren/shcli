#!/usr/bin/env python
from setuptools import setup, find_packages


description = long_description = "Python client for Socialhome."


setup(
    name="shcli",
    version="0.1.4",
    description=description,
    long_description=long_description,
    author="Jason Robinson",
    author_email="mail@jasonrobinson.me",
    maintainer="Jason Robinson",
    maintainer_email="mail@jasonrobinson.me",
    url="https://github.com/jaywink/shcli",
    download_url="https://github.com/jaywink/shcli/releases",
    packages=find_packages(exclude=["tests"]),
    license="MIT",
    install_requires=[
        "requests>=2.8.0,<3",
        "click>=6,<7",
    ],
    python_requires=">=3.4",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "shcli = shcli.cli:shcli",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Communications",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="socialhome federation",
)
