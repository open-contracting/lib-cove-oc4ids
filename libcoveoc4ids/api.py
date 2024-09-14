from libcove.lib.tools import get_file_type
from libcoveocds.util import json

from libcoveoc4ids.common_checks import common_checks_oc4ids
from libcoveoc4ids.config import LibCoveOC4IDSConfig
from libcoveoc4ids.schema import SchemaOC4IDS


def oc4ids_json_output(
    output_dir: str = "",
    file=None,  # : str | None
    file_type=None,  # : str | None
    json_data=None,  # : dict | None
    lib_cove_oc4ids_config=None,  # : LibCoveOC4IDSConfig | None
):
    if not lib_cove_oc4ids_config:
        lib_cove_oc4ids_config = LibCoveOC4IDSConfig()

    if not file_type:
        file_type = get_file_type(file)

    context = {"file_type": file_type}

    if file_type == "json":
        if not json_data:
            with open(file, "rb") as f:
                json_data = json.loads(f.read())

        schema_obj = SchemaOC4IDS(lib_cove_oc4ids_config)
    else:
        raise NotImplementedError

    return common_checks_oc4ids(
        context,
        output_dir,
        json_data,
        schema_obj,
        # common_checks_context(cache=True) caches the results to a file, which is not needed in API context.
        cache=False,
    )
