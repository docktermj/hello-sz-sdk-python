#! /usr/bin/env python3

import random

import grpc
from independent_module import print_version

random_number = random.randint(1, 2)

if random_number == 1:

    from senzing_core import SzAbstractFactoryCore as SzAbstractFactory
    from senzing_core import (
        SzAbstractFactoryParametersCore as SzAbstractFactoryParameters,
    )

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
else:
    from senzing_grpc import SzAbstractFactoryGrpc as SzAbstractFactory
    from senzing_grpc import (
        SzAbstractFactoryParametersGrpc as SzAbstractFactoryParameters,
    )

    FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
        "grpc_channel": grpc.insecure_channel("localhost:8261"),
    }

sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
print(f"Random number: {random_number}")
print_version(sz_abstract_factory)
