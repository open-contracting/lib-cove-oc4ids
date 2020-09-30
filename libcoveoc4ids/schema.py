from urllib.parse import urljoin

from libcove.lib.common import SchemaJsonMixin
import libcoveoc4ids.config


class SchemaOC4IDS(SchemaJsonMixin):
    def __init__(self, lib_cove_oc4ids_config=None):
        self.config = (
            lib_cove_oc4ids_config or libcoveoc4ids.config.LibCoveOC4IDSConfig()
        )

        self.version = self.config.config["schema_version"]
        self.version_choices = self.config.config["schema_version_choices"]
        self.schema_host = self.config.config["schema_host"]
        self.schema_name = self.config.config["schema_item_name"]
        self.pkg_schema_name = self.config.config["schema_name"]
        self.schema_url = urljoin(self.schema_host, self.schema_name)
        self.pkg_schema_url = urljoin(self.schema_host, self.pkg_schema_name)
