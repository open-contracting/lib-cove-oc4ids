from libcove.lib.common import SchemaJsonMixin
from urllib.parse import urljoin


class SchemaOC4IDS(SchemaJsonMixin):

    def __init__(self, lib_cove_oc4ids_config=None):
        self.schema_host = lib_cove_oc4ids_config.config['schema_host']
        self.release_schema_name = lib_cove_oc4ids_config.config['schema_item_name']
        self.release_pkg_schema_name = lib_cove_oc4ids_config.config['schema_name']
        self.release_schema_url = urljoin(self.schema_host, self.release_schema_name)
        self.release_pkg_schema_url = urljoin(self.schema_host, self.release_pkg_schema_name)
