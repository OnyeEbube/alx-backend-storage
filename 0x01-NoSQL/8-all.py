#!/usr/bin/env python3
"""A python function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """List all collections"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
