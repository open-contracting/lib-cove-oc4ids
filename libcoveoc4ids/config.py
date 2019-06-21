import os
import datetime
from libcove.config import LIB_COVE_CONFIG_DEFAULT, LibCoveConfig

LIB_COVE_OC4IDS_CONFIG_DEFAULT = LIB_COVE_CONFIG_DEFAULT.copy()

LIB_COVE_OC4IDS_CONFIG_DEFAULT.update({
    # These default values are very wide on purpose. It is left to apps using this to tighten them up.
    'root_list_path': 'projects',
    'root_id': 'id',
    'id_name': 'id',
    'root_is_list': False,
    'convert_titles': False,
    'schema_name': 'project-package-schema.json',
    'schema_item_name': 'project-schema.json',
    'schema_host':
    'http://standard.open-contracting.org/infrastructure/schema/0__9__1/'
})


class LibCoveOC4IDSConfig(LibCoveConfig):
    def __init__(self, config=None):

        self.config = LIB_COVE_OC4IDS_CONFIG_DEFAULT.copy()
        if config:
            self.config.update(config)
