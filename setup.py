#! /usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


DESCRIPTION = """\
dbfpy is a python-only module for reading and writing DBF-files.
It was created by Jeff Kunce and then modified by Hans Fiby
and Yaroslav Samchuk.

dbfpy can read and write simple DBF-files.  The `DBF-format
<http://www.clicketyclick.dk/databases/xbase/format/>`_
was developed about 30 years ago and was used by a number
of simple database applications (dBase, Foxpro, Clipper, ...).
The basic datatypes numbers, short text, and dates are available.
Many different extensions have been used; dbfpy can read and write
only simple DBF-files.
"""


setup(name="dbfpy",
        version="2.2.6",
        description="Access .DBF (dBase) files from python",
        url="http://dbfpy.sourceforge.net/",
        license="public domain",
        author="Jeff Kunce",
        maintainer_email="dbfpy-users@lists.sourceforge.net,190810401@qq.com",
        packages=["dbfpy"],
        package_dir={'dbfpy': 'dbfpy'},
        include_package_data=True,
        zip_safe=True,
        install_requires=[],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: Public Domain",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Database",
            "Topic :: Software Development :: Libraries :: Python Modules",
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
        ],
)


# vim: set et sts=4 sw=4 :
