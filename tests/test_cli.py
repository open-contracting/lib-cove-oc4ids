import json
import platform
import subprocess

import pytest

import tests.utils as utils

# https://github.com/pypy/pypy/issues/4009
pytestmark = pytest.mark.skipif(
    platform.system() == "Darwin" and platform.python_implementation() == "PyPy",
    reason="CI outputs .../lib/pypy3.9/site-packages/certifi/cacert.pem None",
)


def test_cli_runs():
    """ Test the cli tool runs as expected """
    fixture_path = utils.get_path_for_fixture("example-data.json")

    # If non-zeo exit status this will raise CalledProcessError
    output = subprocess.check_output(['libcoveoc4ids', fixture_path])

    # output json should be parseable
    json.loads(output)


def test_compact():
    fixture_path = utils.get_path_for_fixture("example-data.json")

    output = subprocess.check_output(['libcoveoc4ids', '--compact', fixture_path])

    assert output[:21] == b'{"file_type":"json","'


def test_output(tmpdir):
    fixture_path = utils.get_path_for_fixture("example-data.json")
    output_path = tmpdir.join("result.json")

    output = subprocess.check_output(['libcoveoc4ids', '--output', str(output_path), fixture_path])

    with open(output_path) as f:
        json.load(f)

    assert output == b''
