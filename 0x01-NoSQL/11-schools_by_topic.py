#!/usr/bin/env python3
"""module for topic in schools"""


def schools_by_topic(mongo_collection, topic):
    """find and return schools with topic"""
    schools = mongo_collection.find(
            {"topics": {"$in": [topic]}}
            )
    return schools
