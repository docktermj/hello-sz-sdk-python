#! /usr/bin/env python3

from senzing import SzAbstractFactory, SzError


def print_version(sz_abstract_factory: SzAbstractFactory):
    try:
        sz_product = sz_abstract_factory.create_product()
        result = sz_product.get_version()
        print(result)
    except SzError as err:
        print(f"\nFile {__file__}:\nError:\n{err}\n")
