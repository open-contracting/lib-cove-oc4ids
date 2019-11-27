import json
import subprocess

import tests.utils as utils


def test_cli_runs():
    """ Test the cli tool runs as expected """
    fixture_path = utils.get_path_for_fixture("example-data.json")

    # If non-zeo exit status this will raise CalledProcessError
    output = subprocess.check_output(['libcoveoc4ids', fixture_path])

    # Decode to str from bytes for older python (3.5) which doesn't support
    # byte input to loads.
    # output json should be parseable
    json.loads(output.decode("utf-8"))
