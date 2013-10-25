#!/usr/bin/env python

from setuptools import setup

setup(
    name='tornado_chat',
    version='0.0.1',
    description='Yet another simple chat example on tornado framework.',
    author='Pyotr Ermishkin',
    author_email='quasiyoke@gmail.com',
    url='https://github.com/quasiyoke/tornado-chat',
    packages=['chat', ],
    package_data={
        'chat': ['templates/*.html', ],
    },
    install_requires=['tornado', ],
)
