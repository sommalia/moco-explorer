#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'moco-wrapper']

setup_requirements = ['pytest-runner' ]

test_requirements = ['pytest>=3', ]

setup(
    author="sommalia",
    author_email='sommalia@tuta.io',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Command line to for exporting data over the moco api",
    entry_points={
        'console_scripts': [
            'moco_explorer=moco_explorer.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='moco_explorer',
    name='moco_explorer',
    packages=find_packages(include=['moco_explorer', 'moco_explorer.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sommalia/moco_explorer',
    version='0.2.0',
    zip_safe=False,
)
