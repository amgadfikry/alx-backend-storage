#!/usr/bin/env python3
""" unction that returns all students sorted by average score """


def top_students(mongo_collection):
    """ function that returns all students sorted by average score"""
    result = mongo_collection.aggregate([
        {'$set': {'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}},
        ])
    return result
