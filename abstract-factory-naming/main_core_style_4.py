#! /usr/bin/env python3

from independent_module import print_version
from senzing_core import SzAbstractFactoryCore as SzAbstractFactory
from senzing_core import SzAbstractFactoryParametersCore as SzAbstractFactoryParameters

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "instance_name": "Example",
    "settings": {
        "PIPELINE": {
            "CONFIGPATH": "/etc/opt/senzing",
            "RESOURCEPATH": "/opt/senzing/er/resources",
            "SUPPORTPATH": "/opt/senzing/data",
        },
        "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
    },
}

sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
print_version(sz_abstract_factory)
