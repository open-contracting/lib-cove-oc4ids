import json
import shutil
import tempfile

import click

from libcoveoc4ids.api import oc4ids_json_output


@click.command()
@click.argument("filename")
def main(filename):
    output_dir = tempfile.mkdtemp(prefix="lib-cove-oc4ids-cli-", dir=tempfile.gettempdir())

    try:
        result = oc4ids_json_output(output_dir, filename)
    finally:
        shutil.rmtree(output_dir)

    output = json.dumps(result, indent=2)
    click.echo(output)


if __name__ == "__main__":
    main()
