#!/usr/bin/env python

from distutils.core import setup

long_description = """pyEdgeworthBox calculates concepts of the pure exchange economy
(subject to microeconomics) and draws the Edgeworth box
"""

setup(name='pyEdgeworthBox',
    version='0.1.1',
    description='Python Library to draw the Edgeworth box and calculate equilibrium, core, pareto efficient allocations etc',
    author='Maxim Litvak',
    author_email='maxim@litvak.eu',
    url='http://github.com/maxlit/pyEdgeworthBox',
    test_suite='test',
    packages=['pyEdgeworthBox'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Scientific/Engineering'
        ],
                                         )
