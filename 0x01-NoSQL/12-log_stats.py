#!/usr/bin/env python3
""" Python script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

total = collection.count_documents({})
methods_total = [collection.count_documents({'method': m}) for m in methods]
status = collection.count_documents({'method': 'GET', 'path': '/status'})
print(f'{total} logs')
print('Methods:')
for x in range(len(methods)):
    print(f'    method {methods[x]}: {methods_total[x]}')
print(f'{status} status check')
