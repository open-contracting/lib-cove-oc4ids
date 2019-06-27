from setuptools import setup, find_packages

setup(
    name='libcoveoc4ids',
    version='0.0.0',
    author='Open Data Services',
    author_email='code@opendataservices.coop',
    url='https://github.com/opendataservices/lib-cove-oc4ids',
    description='A data review library',
    packages=find_packages(),
    long_description='A data review library',
    install_requires=[
        'jsonref',
        'jsonschema<2.7',
        # Required for jsonschema to validate URIs
        'rfc3987',
        # Required for jsonschema to validate date-time
        'strict-rfc3339',
        'CommonMark',
        'Django',
        'bleach',
        'requests',
        'json-merge-patch',
        'cached-property',
        'python-dateutil',
        # TODO Should also have flatten-tool >= v0.5.0 - that is currently in requirements instead.
        # TODO Should also have lib-cove  >= v0.3.1 - that is currently in requirements instead.
    ],
    classifiers=[
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    ],
    entry_points='''[console_scripts]
coveoc4ids-tool = libcoveoc4ids.cli.__main__:main''',
)
