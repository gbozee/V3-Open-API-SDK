#!/usr/bin/env python
from setuptools import setup

setup(
    name='okex_okcoin',
    version='0.0.0.1',
    packages=['okex','okcoin'],
    description='Unified okex and okcoin',
    url='https://github.com/gbozee/V3-Open-API-SDK',
    author='Gbozee',
    license='MIT',
    author_email='',
    install_requires=['requests', 'websockets==6.0'],
    keywords='binance exchange rest api bitcoin ethereum btc eth neo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
