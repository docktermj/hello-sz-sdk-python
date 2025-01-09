#! /usr/bin/env python3

import random

import grpc
from independent_module import print_version
from senzing_core import SzAbstractFactory as SzAbstractFactoryCore
from senzing_core import SzAbstractFactoryParameters as SzAbstractFactoryParametersCore
from senzing_grpc import SzAbstractFactory as SzAbstractFactoryGrpc
from senzing_grpc import SzAbstractFactoryParameters as SzAbstractFactoryParametersGrpc

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

random_number = random.randint(1, 2)

if random_number == 1:
    sz_abstract_factory = SzAbstractFactoryCore(**FACTORY_PARAMETERS_CORE)
else:
    sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS_GRPC)

print(f"Random number: {random_number}")
print_version(sz_abstract_factory)
