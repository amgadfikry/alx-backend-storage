#!/usr/bin/env python3
""" cash class to handle simple cache """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ class of all content of creating cache """
    def __init__(self) -> None:
        """ magic method that init with every class instance """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method generate random key and set data as value of key
            in redis store
            Params:
                data: is value of key
            Return:
                string of key
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, float, bytes, int]:
        """ method take callable function and convert data
            using this function
        """
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> str:
        """ method convert value to string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ method convert value to int"""
        return self.get(key, lambda x: int(x))
