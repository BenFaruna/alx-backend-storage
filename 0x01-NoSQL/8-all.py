#!/usr/bin/env python3
"""module for pymongo"""


def list_all(mongo_collection):
    """function returns all data in collection"""
    return mongo_collection.find()
