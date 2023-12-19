#!/usr/bin/env python3
""" Python script that provides some stats about Nginx logs """
from pymongo import MongoClient


def main():
    """ main function run if excute"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    total = collection.count_documents({})
    methods_total = [
            collection.count_documents({'method': m}) for m in methods]
    status = collection.count_documents({'method': 'GET', 'path': '/status'})
    print('{} logs'.format(total))
    print('Methods:')
    for x in range(len(methods)):
        print('\tmethod {}: {}'.format(methods[x], methods_total[x]))
    print('{} status check'.format(status))


if __name__ == "__main__":
    main()
