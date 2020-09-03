from urllib.parse import urljoin

from libcove.lib.common import SchemaJsonMixin


class SchemaOC4IDS(SchemaJsonMixin):

    def __init__(self, lib_cove_oc4ids_config=None):
        # Currenly this mostly copies config into the object as properties
        self.version = lib_cove_oc4ids_config.config['schema_version']
        self.version_choices = \
            lib_cove_oc4ids_config.config['schema_version_choices']
        self.schema_host = lib_cove_oc4ids_config.config['schema_host']
        self.schema_name = lib_cove_oc4ids_config.config['schema_item_name']
        self.pkg_schema_name = lib_cove_oc4ids_config.config['schema_name']
        self.schema_url = urljoin(self.schema_host, self.schema_name)
        self.pkg_schema_url = urljoin(self.schema_host, self.pkg_schema_name)
