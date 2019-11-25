import argparse
import json
import shutil
import tempfile

import libcoveoc4ids.api


def main():
    parser = argparse.ArgumentParser(description='Lib Cove OC4IDS CLI')
    parser.add_argument("filename")

    args = parser.parse_args()

    cove_temp_folder = tempfile.mkdtemp(prefix='lib-cove-oc4ids-cli-', dir=tempfile.gettempdir())
    try:
        result = libcoveoc4ids.api.oc4ids_json_output(
            cove_temp_folder,
            args.filename,
            file_type='json'
        )
    finally:
        shutil.rmtree(cove_temp_folder)

    print(json.dumps(result, indent=4))


if __name__ == '__main__':
    main()
