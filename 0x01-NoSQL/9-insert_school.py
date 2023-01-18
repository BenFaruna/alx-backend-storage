#!/usr/bin/env python3
"""module for inserting into a collection"""


def insert_school(mongo_collection, **kwargs):
    """inserts a document to school collection"""
    _id = mongo_collection.insert_one(kwargs)
    return _id.inserted_id
