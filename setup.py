#!/usr/bin/env python

from setuptools import setup

import os
SETUP_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(SETUP_DIR, 'chat'))

import platform
if 'Windows' == platform.system():
    command = 'compass.bat compile'
else:
    command = 'compass compile'

import subprocess
try:
    subprocess.check_call(command.split())
except (subprocess.CalledProcessError, OSError):
    print 'ERROR: problems with compiling Sass. Is Compass installed?'
    raise SystemExit
os.chdir(SETUP_DIR)
    
setup(
    name='tornado_chat',
    version='0.0.1',
    description='Yet another simple chat example on tornado framework.',
    author='Pyotr Ermishkin',
    author_email='quasiyoke@gmail.com',
    url='https://github.com/quasiyoke/tornado-chat',
    packages=['chat', ],
    package_data={
        'chat': ['templates/*.html', 'static/css/*.css', 'static/js/*.js', ],
    },
    install_requires=['tornado', ],
)
