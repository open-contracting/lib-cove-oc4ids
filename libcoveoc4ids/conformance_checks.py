import gettext
import re

from libcoveoc4ids.check_classes import ConformanceCheck

_ = gettext.gettext


class ProjectPrefixCheck(ConformanceCheck):
    def process(self, data, flat_data):

        # matches /projects/10/id
        project_path = re.compile(r".*\/projects\/[0-9]+\/id$")
        # matches oc4ids-abc123-anything
        valid_project_id = re.compile(r"oc4ids\-[a-z0-9]{6}.+$")

        invalid_project_id_paths = []

        for path, value in flat_data.items():
            if project_path.match(path):
                # Note if there is no value the regex can't match we leave it to
                # the other checks to expose this error.
                if value and valid_project_id.match(value) is None:
                    invalid_project_id_paths.append({"path": path, "value": value})

        if len(invalid_project_id_paths) == 0:
            return True

        return self.result(
            "invalid-project-ids",
            _(
                "%(count)d of your project id fields has a problem: "
                "There is no prefix or the prefix format is not recognised."
            )
            % {"count": len(invalid_project_id_paths)},
            invalid_project_id_paths,
        )


def conformance_checks():
    return [
        ProjectPrefixCheck(),
    ]
