#!/usr/bin/env python3
""" cash class to handle simple cache """
import redis
import requests
from functools import wraps
import hashlib

# Initialize Redis connection
r = redis.Redis()

def track_and_cache(expire: int = 10):
    """
    Decorator to cache page content and track access count using Redis.
    """
    def decorator(func):
        """ decorator that caches the result of a function """
        @wraps(func)
        def wrapper(url: str):
            """ wrapper function that caches the result of the function """
            hash_key = hashlib.sha256(url.encode()).hexdigest()
            cache_key = f"cache:{hash_key}"
            count_key = f"count:{hash_key}"

            # Track access count
            r.incr(count_key)

            # Check cache
            cached = r.get(cache_key)
            if cached:
                return cached.decode("utf-8")

            # Fetch, cache, and return
            content = func(url)
            r.setex(cache_key, expire, content)
            return content
        return wrapper
    return decorator


@track_and_cache(expire=10)
def get_page(url: str) -> str:
    """ fetches the content of a URL and caches it """
    response = requests.get(url)
    return response.text