from libcove.lib.common import common_checks_context, get_additional_codelist_values, get_field_coverage
from libcoveocds.lib.additional_checks import flatten_dict

from libcoveoc4ids.additional_checks import ADDITIONAL_CHECKS, CONFORMANCE_CHECKS


def common_checks_oc4ids(context, upload_dir, json_data, schema_obj, *, cache=True):
    common_checks = common_checks_context(upload_dir, json_data, schema_obj, "schema.json", context, cache=cache)
    context.update(common_checks["context"])

    flat = dict(flatten_dict(json_data))
    context["conformance_checks"] = [result for function in CONFORMANCE_CHECKS for result in function(json_data, flat)]
    context["additional_checks"] = [result for function in ADDITIONAL_CHECKS for result in function(json_data, flat)]

    additional_codelist_values = get_additional_codelist_values(schema_obj, json_data)
    closed_codelist_values = {key: value for key, value in additional_codelist_values.items() if not value["isopen"]}
    open_codelist_values = {key: value for key, value in additional_codelist_values.items() if value["isopen"]}
    context.update(
        {
            "additional_closed_codelist_values": closed_codelist_values,
            "additional_open_codelist_values": open_codelist_values,
            "field_coverage": get_field_coverage(schema_obj, json_data.get("projects")),
        }
    )

    return context
