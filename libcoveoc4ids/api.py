from libcoveocds.util import json

from libcoveoc4ids.common_checks import common_checks_oc4ids
from libcoveoc4ids.config import LibCoveOC4IDSConfig
from libcoveoc4ids.schema import SchemaOC4IDS


def oc4ids_json_output(
    output_dir: str = "",
    file=None,  # : str | None
    json_data=None,  # : dict | None
    lib_cove_oc4ids_config=None,  # : LibCoveOC4IDSConfig | None
):
    if not lib_cove_oc4ids_config:
        lib_cove_oc4ids_config = LibCoveOC4IDSConfig()

    if not json_data:
        with open(file, "rb") as f:
            json_data = json.loads(f.read())

    return common_checks_oc4ids(
        {"file_type": "json"},
        output_dir,
        json_data,
        SchemaOC4IDS(lib_cove_oc4ids_config),
        # common_checks_context(cache=True) caches the results to a file, which is not needed in API context.
        cache=False,
    )
