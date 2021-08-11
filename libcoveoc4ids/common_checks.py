from libcove.lib.common import common_checks_context, get_additional_codelist_values, get_field_coverage
from libcoveocds.lib.additional_checks import flatten_dict
from libcoveocds.lib.common_checks import get_releases_aggregates

from libcoveoc4ids.additional_checks import additional_checks
from libcoveoc4ids.config import LibCoveOC4IDSConfig
from libcoveoc4ids.conformance_checks import conformance_checks


def common_checks_oc4ids(context, upload_dir, json_data, schema_obj, lib_cove_oc4ids_config=None, cache=True):
    additional_checks_results = []

    if not lib_cove_oc4ids_config:
        lib_cove_oc4ids_config = LibCoveOC4IDSConfig()

    # Common schema checks
    common_checks = common_checks_context(upload_dir, json_data, schema_obj,
                                          'schema.json', context, cache=cache)

    context.update(common_checks["context"])

    flattened_data = dict(flatten_dict(json_data))

    # end Common checks

    # Conformance checks
    conformance_checks_results = []

    for conformance_check in conformance_checks():
        check_result = conformance_check.process(json_data, flattened_data)
        # Check passed, continue
        if check_result is True:
            continue

        conformance_checks_results.append(check_result)

    context.update({"conformance_checks": conformance_checks_results})
    # end conformance checks

    # Additional checks

    for additional_check in additional_checks():
        check_result = additional_check.process(json_data, flattened_data)
        # Check passed, continue
        if check_result is True:
            continue

        additional_checks_results.append(check_result)

    context.update({"additional_checks": additional_checks_results})
    # end Additional checks

    # codelist checks
    validation_errors = common_checks["context"]["validation_errors"]

    additional_codelist_values = get_additional_codelist_values(schema_obj, json_data)
    closed_codelist_values = {
        key: value for key, value in additional_codelist_values.items() if not value["isopen"]
    }
    open_codelist_values = {key: value for key, value in additional_codelist_values.items() if value["isopen"]}

    context.update(
        {
            "releases_aggregates": get_releases_aggregates(json_data, ignore_errors=bool(validation_errors)),
            "additional_closed_codelist_values": closed_codelist_values,
            "additional_open_codelist_values": open_codelist_values,
            "field_coverage": get_field_coverage(schema_obj, json_data.get("projects")),
        }
    )
    # end codelist check

    return context
