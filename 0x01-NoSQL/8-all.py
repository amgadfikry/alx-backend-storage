#!/usr/bin/env python3
""" Python function that lists all documents in a collection """


def list_all(mongo_collection):
    """ function get list of all documents in collections"""
    li = mongo_collection.find({})
    if li:
        return li
    else:
        return []
