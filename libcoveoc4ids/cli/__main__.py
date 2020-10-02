import argparse
import shutil
import tempfile

from libcoveoc4ids.api import jsonlib, oc4ids_json_output, using_orjson


def main():
    parser = argparse.ArgumentParser(description='Lib Cove OC4IDS CLI')
    parser.add_argument("filename")
    parser.add_argument("-c", "--compact", action="store_true", help="compact instead of pretty-printed output")

    args = parser.parse_args()

    cove_temp_folder = tempfile.mkdtemp(prefix='lib-cove-oc4ids-cli-', dir=tempfile.gettempdir())
    try:
        result = oc4ids_json_output(
            cove_temp_folder,
            args.filename,
            file_type='json'
        )
    finally:
        shutil.rmtree(cove_temp_folder)

    kwargs = {}
    if not args.compact:
        if using_orjson:
            kwargs['option'] = jsonlib.OPT_INDENT_2
        else:
            kwargs['indent'] = 2

    output = jsonlib.dumps(result, **kwargs)

    if using_orjson:
        output = output.decode('utf-8')

    print(output)


if __name__ == '__main__':
    main()
