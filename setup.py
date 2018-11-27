#!/usr/bin/env python2

from setuptools import setup
from os import path, listdir


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


def files(dirname):
    return [path.join(dirname, filename) for filename in listdir(dirname)]


setup(
    name='bgptools',
    version='0.1a1',
    description='Tools for BGP Analysis.',
    url='https://github.com/openalto/bgptools',
    author='Jensen Zhang',
    author_email='hack@jensen-zhang.site',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: Emulators",
    ],
    install_requires=read('requirements.txt').splitlines(),
    license='MIT',
    long_description=read('README.rst'),
    packages=['bgptools'],
    # scripts=files('bin'), # Uncomment it to include executable scripts
    zip_safe=False,
)
