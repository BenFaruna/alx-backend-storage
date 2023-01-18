#!/usr/bin/env python3
"""module for updating course"""


def update_topics(mongo_collection, name, topics):
    """update topics in collection"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
