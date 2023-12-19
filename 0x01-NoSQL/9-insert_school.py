#!/usr/bin/env python3
""" Python function that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """ function that insert new document to collection """
    return mongo_collection.insert_one(kwargs).inserted_id
