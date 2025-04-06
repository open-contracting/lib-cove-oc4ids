import argparse
import copy
import json
import random
import string


def random_project_id():
    chars = string.ascii_lowercase + string.digits
    code = "".join(random.choice(chars) for _ in range(6))

    return f"oc4ids-{code}-test"


def generate_data(num_projects):
    with open("fixtures/example-additional-checks.json") as fp:
        data = json.load(fp)

        # Use first project as a "template"
        project_template = data["projects"][0]

        i = 0
        while i != num_projects:
            project = copy.deepcopy(project_template)
            project["id"] = random_project_id()
            data["projects"].append(project)
            i += 1

        with open(f"example-generated-data-{num_projects}-projects.json", "w") as out_fp:
            json.dump(data, out_fp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(type=int, action="store", dest="num_projects", help="The number of projects to generate")

    args = parser.parse_args()

    generate_data(args.num_projects)
