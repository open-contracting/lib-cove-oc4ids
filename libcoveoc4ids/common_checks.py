from libcove.lib.common import common_checks_context
from libcoveocds.lib.additional_checks import EmptyFieldCheck
from libcoveocds.lib.additional_checks import run_additional_checks as libcoveocds_run_additional_checks

from libcoveoc4ids.config import LibCoveOC4IDSConfig


def common_checks_oc4ids(context, upload_dir, json_data, schema_obj, lib_cove_oc4ids_config=None, cache=True):

    if not lib_cove_oc4ids_config:
        lib_cove_oc4ids_config = LibCoveOC4IDSConfig()

    common_checks = common_checks_context(upload_dir, json_data, schema_obj,
                                          'schema.json', context, cache=cache)

    context.update(common_checks["context"])

    additional_checks = libcoveocds_run_additional_checks(
        json_data, [EmptyFieldCheck], ignore_errors=True, return_on_error=None
    )

    context.update({"additional_checks": additional_checks})

    return context
