import redis
import requests
import hashlib
from functools import wraps

# Initialize Redis connection
r = redis.Redis()

def track_and_cache(expire: int = 10):
    """
    Decorator to cache page content and track access count using Redis.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(url: str):
            cache_key = f"cache:{url}"
            count_key = f"count:{url}"

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
    response = requests.get(url)
    return response.text