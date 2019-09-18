from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='libcoveoc4ids',
    version='0.1.1',
    author='Open Data Services',
    author_email='data@open-contracting.org',
    url='https://github.com/open-contracting/lib-cove-oc4ids',
    description='A data review library for the Open Contracting for Infrastructure Data Standards (OC4IDS)',
    license='AGPLv3',
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'bleach',
        'cached-property',
        'CommonMark',
        'Django',
        'json-merge-patch',
        'jsonref',
        'jsonschema<2.7',
        'python-dateutil',
        'requests',
        'rfc3987',
        'strict-rfc3339',
        # The following are in .travis.yml instead.
        # 'flatten-tool',
        # 'lib-cove',
    ],
    extras_require={
        'test': [
            'coveralls',
            'pytest',
            'pytest-cov',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'coveoc4ids-tool = libcoveoc4ids.cli.__main__:main',
        ],
    },
)
