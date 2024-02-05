# Copyright (c) 2019, <NAME>
# All rights reserved.
from setuptools import setup, find_packages

setup(
    name='reconciler',
    version='0.1.0',
    description='reconciler',
    url='https://github.com/muathendirangu/reconcile',
    author='muathe ndirangu',
    author_email='muathe.ndirangu@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'reconciler=reconciler.reconciler:main'
        ],
    },
    long_description_content_type='text/markdown'
)
