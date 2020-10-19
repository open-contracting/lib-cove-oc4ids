from setuptools import find_packages, setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='libcoveoc4ids',
    version='0.3.1',
    author='Open Data Services',
    author_email='data@open-contracting.org',
    url='https://github.com/open-contracting/lib-cove-oc4ids',
    description='A data review library for the Open Contracting for Infrastructure Data Standards (OC4IDS)',
    license='AGPLv3',
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    install_requires=[
        'Django<2.3',
        'flattentool',
        'libcoveocds>=0.8.0',
        'libcove>=0.18.0',
        'rfc3987',
        'strict-rfc3339',
    ],
    extras_require={
        'perf': [
            'orjson>=3',
        ],
        'test': [
            'coveralls',
            'pytest',
            'pytest-cov',
            'isort',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'libcoveoc4ids = libcoveoc4ids.cli.__main__:main',
        ],
    },
)
