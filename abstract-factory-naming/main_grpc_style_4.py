#! /usr/bin/env python3

import grpc
from independent_module import print_version
from senzing_grpc import SzAbstractFactoryGrpc as SzAbstractFactory
from senzing_grpc import SzAbstractFactoryParametersGrpc as SzAbstractFactoryParameters

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
print_version(sz_abstract_factory)
