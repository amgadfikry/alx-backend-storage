#!/usr/bin/env python3
""" cash class to handle simple cache """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ decorator that store the history of inputs and outputs
        for a particular function
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        self._redis.rpush("{}:inputs".format(key), str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush("{}:outputs".format(key), output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """ display the history of calls of a particular function """
    key = method.__qualname__
    redis = method.__self__._redis
    inputs = redis.lrange("{}:inputs".format(key), 0, -1)
    outputs = redis.lrange("{}:outputs".format(key), 0, -1)
    print("{} was called {} times:".format(key, len(inputs)))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, i.decode('utf-8'),
                                     o.decode('utf-8')))


def count_calls(method: Callable) -> Callable:
    """ decorator that count how many times a function has been called """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ class of all content of creating cache """
    def __init__(self) -> None:
        """ magic method that init with every class instance """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
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
