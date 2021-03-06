# -*- coding: utf-8 -*-
# This file is part of atgmlogger-plugins
# https://github.com/DynamicGravitySystems/atgmlogger-plugins
# Licensed under the MIT License
# (c) Zachery Brady, Dynamic Gravity Systems, 2018-2019

from setuptools import setup

__version__ = '0.1.0b1'
requirements = [
    # 'RPi.GPIO >= 0.6.3',
    'requests'
]

setup(
    name='atgmlogger-plugins',
    version=__version__,
    packages=['atgmlogger_plugins'],
    url='',
    license='',
    author='Zachery Brady',
    author_email='bradyzp@dynamicgravitysystems.com',
    description='Plugins for ATGMlogger data recording application',
    long_description='',
    install_requires=requirements,
    python_requires='>=3.5.*',
    include_package_data=False,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha'
    ]
)
