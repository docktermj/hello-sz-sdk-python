#! /usr/bin/env python3

from independent_module import print_version
from senzing_core import SzAbstractFactory as SzAbstractFactoryCore
from senzing_core import SzAbstractFactoryParameters as SzAbstractFactoryParametersCore

FACTORY_PARAMETERS: SzAbstractFactoryParametersCore = {
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

sz_abstract_factory = SzAbstractFactoryCore(**FACTORY_PARAMETERS)
print_version(sz_abstract_factory)
