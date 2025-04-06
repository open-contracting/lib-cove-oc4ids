import json
import subprocess

from tests import utils


def test_cli_runs():
    """Test the cli tool runs as expected"""
    # If non-zeo exit status this will raise CalledProcessError
    output = subprocess.check_output(["libcoveoc4ids", utils.get_path_for_fixture("example-data.json")])

    # output json should be parseable
    json.loads(output)
