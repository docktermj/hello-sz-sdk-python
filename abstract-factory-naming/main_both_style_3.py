#! /usr/bin/env python3

import grpc
from independent_module import print_version
from senzing_core import SzAbstractFactoryCore, SzAbstractFactoryParametersCore
from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

FACTORY_PARAMETERS_CORE: SzAbstractFactoryParametersCore = {
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

FACTORY_PARAMETERS_GRPC: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

sz_abstract_factory_core = SzAbstractFactoryCore(**FACTORY_PARAMETERS_CORE)
print_version(sz_abstract_factory_core)

sz_abstract_factory_grpc = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS_GRPC)
print_version(sz_abstract_factory_grpc)
