import os

from libcoveoc4ids.api import oc4ids_json_output

FIXTURE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures")


def get_path_for_fixture(fixture_name):
    """Returns the full file system path for a given fixture_name"""
    return os.path.join(FIXTURE_PATH, fixture_name)


def test_fixture(fixture_name):
    context = oc4ids_json_output("", get_path_for_fixture(fixture_name))
    return context["validation_errors"], context
