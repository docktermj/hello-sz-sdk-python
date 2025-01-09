#! /usr/bin/env python3

from senzing import SzAbstractFactory, SzError


def print_version(sz_abstract_factory: SzAbstractFactory):
    try:
        sz_product = sz_abstract_factory.create_product()
        RESULT = sz_product.get_version()
        print(f"\nFile {__file__}:\n{RESULT}\n")
    except SzError as err:
        print(f"\nFile {__file__}:\nError:\n{err}\n")
