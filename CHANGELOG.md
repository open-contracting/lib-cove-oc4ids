# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.4.3] - 2023-12-11

### Added

- Support for OC4IDS 0.9.4.

### Changed

- Drop support for Python 3.6 (end-of-life 2021-12-23).

## [0.4.2] - 2022-09-08

### Fixed

- Don't error if `/projects/` isn't in JSON Pointer.

## [0.4.1] - 2021-10-12

### Added

- Support for OC4IDS 0.9.3.

## [0.4.0] - 2021-08-18

### Added

- Calculate field coverage using a function from lib-cove https://github.com/open-contracting/cove-oc4ids/issues/98

## [0.3.2] - 2021-04-10

### Added

- Add Python wheels distribution.

## [0.3.1] - 2020-10-19

### Changed

- The check for project id prefix has been moved into a conformance check. This required a minor bit of refactoring.

## [0.3.0] - 2020-10-16

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

## [0.2.0] - 2020-09-03

### Changed

- Rename schema object attributes to remove word "release", as in latest lib-cove

## [0.1.2] - 2020-07-15

### Added

- Support for OC4IDS 0.9.2.

## [0.1.1] - 2019-07-05

### Changed

- Incorrect config item removed.

## [0.1.0] - 2019-06-28

First release.
