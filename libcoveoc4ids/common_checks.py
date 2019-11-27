from libcove.lib.common import common_checks_context

from libcoveoc4ids.config import LibCoveOC4IDSConfig


def common_checks_oc4ids(context, upload_dir, json_data, schema_obj,
                         lib_cove_oc4ids_config=None):

    if not lib_cove_oc4ids_config:
        lib_cove_oc4ids_config = LibCoveOC4IDSConfig()

    common_checks = common_checks_context(upload_dir, json_data, schema_obj,
                                          'schema.json', context)

    context.update(common_checks['context'])

    return context
