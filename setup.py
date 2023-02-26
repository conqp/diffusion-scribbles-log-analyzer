#! /usr/bin/env python3
"""Installation script."""


from setuptools import setup


setup(
    name='dsla',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Richard Neumann',
    author_email='mail@richard-neumann.de',
    python_requires='>=3.8',
    packages=[
        'dsla',
        'dsla.datastructures',
        'dsla.plots',
        'dsla.statistics'
    ],
    install_requires=[
        'matplotlib'
    ],
    entry_points={'console_scripts': ['dsla = dsla.main:main']},
    url='https://github.com/conqp/speculum',
    license='GPLv3',
    description='DiffusionScribbles log analyzer.'
)
