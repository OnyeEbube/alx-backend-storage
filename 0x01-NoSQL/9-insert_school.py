#!/usr/bin/env python3
"""A python function that inserts a new document in a collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document"""
    return mongo_collection.insert_one(kwargs).inserted_id
