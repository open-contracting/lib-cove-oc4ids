import json

from libcove.lib.tools import get_file_type

from libcoveoc4ids.common_checks import common_checks_oc4ids
from libcoveoc4ids.config import LibCoveOC4IDSConfig
from libcoveoc4ids.schema import SchemaOC4IDS


class APIException(Exception):
    pass


def oc4ids_json_output(output_dir, file, file_type=None, json_data=None,
                       lib_cove_oc4ids_config=None):

    if not lib_cove_oc4ids_config:
        lib_cove_oc4ids_config = LibCoveOC4IDSConfig()

    if not file_type:
        file_type = get_file_type(file)
    context = {"file_type": file_type}

    if file_type == 'json':
        if not json_data:
            with open(file, encoding='utf-8') as fp:
                try:
                    json_data = json.load(fp)
                except ValueError:
                    raise APIException('The file looks like invalid json')

        schema_oc4ids = SchemaOC4IDS(lib_cove_oc4ids_config=lib_cove_oc4ids_config)

    else:

        raise Exception("JSON only for now, sorry!")

    context = common_checks_oc4ids(
        context,
        output_dir,
        json_data,
        schema_oc4ids,
        lib_cove_oc4ids_config=lib_cove_oc4ids_config)

    return context
