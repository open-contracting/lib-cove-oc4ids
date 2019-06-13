# Lib Cove OC4IDS


## Command line

Call `libcoveoc4ids` and pass the filename of some JSON data.

    libcoveoc4ids tests/fixtures/api/basic_1.json

## Code for use by external users

The only code that should be used directly by users is the `libcoveoc4ids.config` and `libcoveoc4ids.api` modules.

Other code ( Code in `lib`, etc)
should not be used by external users of this library directly, as the structure and use of these may change more frequently.
