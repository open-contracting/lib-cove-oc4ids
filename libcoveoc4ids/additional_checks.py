import gettext
import re

ORG_PATHS = re.compile(
    r"""
    ^/projects/(\d+)/(
        publicAuthority|
        budget/budgetBreakdowns/\d+/budgetBreakdown/\d+/sourceParty|
        contractingProcesses/\d+/summary/(
            tender/(
                tenderers/\d+|
                procuringEntity|
                administrativeEntity
            )|
            suppliers/\d+
        )
    )/id$
    """,
    re.VERBOSE,
)

# matches oc4ids-abc123-anything
PROJECT_ID = re.compile(r"^oc4ids\-[a-z0-9]{6}.")


# See libcoveocds' empty_field.
def empty_value(_data, flat):
    missing = [
        path
        for path, value in flat.items()
        if (isinstance(value, str) and not value.strip()) or (isinstance(value, (dict, list)) and not value)
    ]

    if missing:
        yield {
            "check_id": "missing-values",
            "message": gettext.gettext(
                "The data includes fields that are empty or contain only whitespaces. "
                "Fields that are not being used, or that have no value, "
                "should be excluded in their entirety (key and value) from the data"
            ),
            "paths": missing,
        }


def currency(_data, flat):
    missing = [
        path[:-6]  # len("amount")
        for path in flat
        if path.endswith("amount") and f"{path[:-6]}currency" not in flat
    ]

    if missing:
        yield {
            "check_id": "missing-currency",
            "message": gettext.gettext(
                "There are %(count)d values without a currency. Currencies should be published for all values."
            )
            % {"count": len(missing)},
            "paths": missing,
        }


def org_references_exist(data, flat):
    missing = []

    party_ids = {}

    for path, value in flat.items():
        if match := ORG_PATHS.search(path):
            project_index = int(match.group(1))

            if project_index not in party_ids:
                parties = data["projects"][project_index].get("parties", [])
                party_ids[project_index] = [p["id"] for p in parties if "id" in p] if isinstance(parties, list) else []

            if value not in party_ids[project_index]:
                missing.append(path)

    if missing:
        yield {
            "check_id": "missing-org-refs",
            "message": gettext.gettext(
                "There are %(count)d organization references with an id that does not match the id of any parties. "
                "All organization references should have an associated entry in the parties array with a matching id."
            )
            % {"count": len(missing)},
            "paths": missing,
        }


def project_prefix(data, _flat):
    invalid = []

    if "projects" in data:
        projects = data["projects"]
        if isinstance(projects, list):
            for i, project in enumerate(projects):
                if "id" in project:
                    project_id = project["id"]
                    if isinstance(project_id, str) and not PROJECT_ID.search(project_id):
                        invalid.append({"path": f"/projects/{i}/id", "value": project["id"]})

    if invalid:
        yield {
            "check_id": "invalid-project-ids",
            "message": gettext.gettext(
                "%(count)d of your project id fields has a problem: "
                "There is no prefix or the prefix format is not recognised."
            )
            % {"count": len(invalid)},
            "path_values": invalid,
        }


ADDITIONAL_CHECKS = [empty_value, currency, org_references_exist]
CONFORMANCE_CHECKS = [project_prefix]
