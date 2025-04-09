# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## 0.9.1 (2025-04-08)

### Changed

- Default to OC4IDS 0.9.5.

## 0.9.0 (2024-11-25)

### Changed

- Set maximum compatible version of libcoveocds.

## 0.8.0 (2024-08-28)

### Removed

- `libcoveoc4ids.api.oc4ids_json_output` no longer accepts a `file_type` argument.
- Reduce use of libcove.

## 0.7.1 (2024-09-27)

### Fixed

- The organization reference check is robust to invalid ``parties`` data.

## 0.7.0 (2024-09-15)

### Changed

- Some arguments must be keyword arguments in:

  - `libcoveoc4ids.common_checks.common_checks_oc4ids`
  - `libcoveoc4ids.schema.SchemaOC4IDS.get_pkg_schema_obj`

- Drop support for Python 3.8.

## 0.6.0 (2024-02-27)

### Changed

- Add `flatten_tool` configuration option.

### Fixed

- Don't error if the project's `id` is not a string, in the organization reference additional check.
- Change the `root_id` configuration option from `"main"` to `"id"`.

### Removed

- `--compact` and `--output` CLI options
- `lib_cove_oc4ids_config` argument from `common_checks_oc4ids()` in `libcoveoc4ids.common_checks`
- `cache` argument from `oc4ids_json_output()` in `libcoveoc4ids.api`
- `root_is_list` configuration option
- `APIException` class in `libcoveoc4ids.api`

## 0.5.0 (2023-12-19)

### Changed

- Drop support for libcove < 0.32.

## 0.4.3 (2023-12-11)

### Added

- Support for OC4IDS 0.9.4.

### Changed

- Drop support for Python 3.6.

## 0.4.2 (2022-09-08)

### Fixed

- Don't error if `/projects/` isn't in JSON Pointer.

## 0.4.1 (2021-10-12)

### Added

- Support for OC4IDS 0.9.3.

## 0.4.0 (2021-08-18)

### Added

- Calculate field coverage using a function from lib-cove https://github.com/open-contracting/cove-oc4ids/issues/98

## 0.3.2 (2021-04-10)

### Added

- Add Python wheels distribution.

## 0.3.1 (2020-10-19)

### Changed

- The check for project id prefix has been moved into a conformance check. This required a minor bit of refactoring.

## 0.3.0 (2020-10-16)

### Added

- Codelist checks
- Additional checks for; currency specified, empty values, project prefixes and the presence of org id references.
- Translation support via gettext
- Tool for generating large test data
- Optional support for orjson for improved performance
- Command line option to write output to file `-o OUTPUT`

### Changed

- Requirements now depends on libcoveocds
- Refactored config variable names

## 0.2.0 (2020-09-03)

### Changed

- Rename schema object attributes to remove word "release", as in latest lib-cove

## 0.1.2 (2020-07-15)

### Added

- Support for OC4IDS 0.9.2.

## 0.1.1 (2019-07-05)

### Changed

- Incorrect config item removed.

## 0.1.0 (2019-06-28)

First release.
