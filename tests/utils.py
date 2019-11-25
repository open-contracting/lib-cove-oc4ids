import json
import os
import tempfile

from libcoveoc4ids.api import oc4ids_json_output

FIXTURE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'fixtures')

TEST_TEMP_DIR = tempfile.mkdtemp(prefix='lib-cove-oc4ids-tests',
                                 dir=tempfile.gettempdir())


def get_validation_errors(tempdir):
    """ returns the validation errors for the last run check """
    validation_json_path = os.path.join(tempdir,
                                        "validation_errors-3.json")

    with open(validation_json_path) as fp:
        raw_data = fp.read()
        return json.loads(raw_data)


def get_path_for_fixture(fixture_name):
    """ Returns the full file system path for a given fixture_name """
    return os.path.join(FIXTURE_PATH, fixture_name)


def test_fixture(fixture_name):
    with tempfile.TemporaryDirectory() as tmpdirname:

        context = oc4ids_json_output(tmpdirname,
                                     get_path_for_fixture(fixture_name),
                                     "json")

        errors = get_validation_errors(tmpdirname)
        return errors, context
