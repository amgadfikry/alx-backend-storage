#!/usr/bin/env python3
""" cash class to handle simple cache """
import redis
import uuid
from typing import Union


class Cache:
    """ class of all content of creating cache """
    def __init__(self) -> None:
        """ magic method that init with every class instance """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """ method generate random key and set data as value of key
            in redis store
            Params:
                data: is value of key
            Return:
                string of key
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
