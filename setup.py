# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup

_NAME = "hcat"


if len(sys.argv) >= 2 and sys.argv[1] == "sdist":
    os.system('cd man/ && gzip -9c hcat.1 > hcat.1.gz')


setup(
        name=_NAME,
        description="Highlighted cat command line",
        long_description=open("README").read(),
        version='0.1.0',
        author=u"Stéphane Blondon",
        author_email="stephane.blondon@gmail.com",
        url="https://github.com/sblondon/" + _NAME,
        packages=[_NAME],
        data_files=[("share/man/man1", ["man/hcat.1.gz"])],
        install_requires=[
            "pygments",
        ],
        entry_points={'console_scripts': ['hcat=hcat.__main__:main']},
        classifiers=[
            "Intended Audience :: End Users/Desktop",
            "Environment :: Console :: Curses",
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Topic :: Terminals",
        ],      


)

