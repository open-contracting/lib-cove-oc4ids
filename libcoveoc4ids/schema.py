from copy import deepcopy
from urllib.parse import urljoin

from libcove.lib.common import SchemaJsonMixin, get_schema_codelist_paths, load_core_codelists

import libcoveoc4ids.config


class SchemaOC4IDS(SchemaJsonMixin):
    def __init__(self, lib_cove_oc4ids_config=None):
        self.config = lib_cove_oc4ids_config or libcoveoc4ids.config.LibCoveOC4IDSConfig()

        self.version = self.config.config["schema_version"]
        self.version_choices = self.config.config["schema_version_choices"]
        self.schema_host = self.config.config["schema_host"]
        self.schema_name = self.config.config["schema_item_name"]
        self.pkg_schema_name = self.config.config["schema_name"]
        self.schema_url = urljoin(self.schema_host, self.schema_name)
        self.pkg_schema_url = urljoin(self.schema_host, self.pkg_schema_name)
        self.codelists = self.config.config["schema_codelists"]["0.9"]

    def get_pkg_schema_obj(self, *, deref=False, use_extensions=False):  # noqa: ARG002 # lib-cove API
        package_schema_obj = deepcopy(self._pkg_schema_obj)
        if deref:
            return self.deref_schema(self.pkg_schema_str)

        return package_schema_obj

    def process_codelists(self):
        """Load the appropriate codelists."""
        # Note the order of these function calls is required for it to work
        self.core_codelist_schema_paths = get_schema_codelist_paths(self, use_extensions=False)
        self.extended_codelist_schema_paths = get_schema_codelist_paths(self, use_extensions=True)

        core_unique_files = frozenset(value[0] for value in self.core_codelist_schema_paths.values())
        self.core_codelists = load_core_codelists(self.codelists, core_unique_files, config=self.config)
        # property required by libcove
        self.extended_codelists = deepcopy(self.core_codelists)
