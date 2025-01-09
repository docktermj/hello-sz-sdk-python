#! /usr/bin/env python3

import grpc
from independent_module import print_version
from senzing_grpc import SzAbstractFactory as SzAbstractFactoryGrpc
from senzing_grpc import SzAbstractFactoryParameters as SzAbstractFactoryParametersGrpc

FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}


sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
print_version(sz_abstract_factory)
