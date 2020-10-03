import argparse
import shutil
import tempfile

from libcoveoc4ids.api import jsonlib, oc4ids_json_output, using_orjson


def main():
    parser = argparse.ArgumentParser(description='Lib Cove OC4IDS CLI')
    parser.add_argument("filename")
    parser.add_argument("-c", "--compact", action="store_true", help="compact instead of pretty-printed output")
    parser.add_argument("-o", "--output", help="write output to the given file instead of standard output")

    args = parser.parse_args()

    cove_temp_folder = tempfile.mkdtemp(prefix='lib-cove-oc4ids-cli-', dir=tempfile.gettempdir())
    try:
        result = oc4ids_json_output(
            cove_temp_folder,
            args.filename,
            file_type='json',
            cache=False,
        )
    finally:
        shutil.rmtree(cove_temp_folder)

    kwargs = {}

    if using_orjson:
        kwargs['option'] = 0
        if not args.compact:
            kwargs['option'] |= jsonlib.OPT_INDENT_2
        if args.output:
            kwargs['option'] |= jsonlib.OPT_APPEND_NEWLINE

        output = jsonlib.dumps(result, **kwargs)
        if args.output:
            with open(args.output, 'wb') as f:
                f.write(output)
        else:
            print(output.decode())
    else:
        if args.compact:
            kwargs['separators'] = (',', ':')
        else:
            kwargs['indent'] = 2

        if args.output:
            with open(args.output, 'w') as f:
                jsonlib.dump(result, f, **kwargs)
        else:
            print(jsonlib.dumps(result, **kwargs))


if __name__ == '__main__':
    main()
