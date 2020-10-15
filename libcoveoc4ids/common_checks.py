from libcove.lib.common import common_checks_context
from libcoveocds.lib.additional_checks import flatten_dict

from libcoveoc4ids.additional_checks import additional_checks
from libcoveoc4ids.config import LibCoveOC4IDSConfig


def common_checks_oc4ids(context, upload_dir, json_data, schema_obj, lib_cove_oc4ids_config=None, cache=True):
    additional_checks_results = []

    if not lib_cove_oc4ids_config:
        lib_cove_oc4ids_config = LibCoveOC4IDSConfig()

    common_checks = common_checks_context(upload_dir, json_data, schema_obj,
                                          'schema.json', context, cache=cache)

    context.update(common_checks["context"])

    flattened_data = dict(flatten_dict(json_data))

    for additional_check in additional_checks():
        check_result = additional_check.process(json_data, flattened_data)
        # Check passed, continue
        if check_result is True:
            continue

        additional_checks_results.append(check_result)

    context.update({"additional_checks": additional_checks_results})

    return context
