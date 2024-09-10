import requests
import redis
from typing import Callable
from functools import wraps

# Initialize Redis connection
redis_store = redis.Redis()

def cache_with_expiration(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(url: str) -> str:
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"
        
        # Increment access count
        redis_store.incr(count_key)
        
        # Check if content is cached
        cached_content = redis_store.get(cache_key)
        if cached_content:
            print("Cache hit!")
            return cached_content.decode('utf-8')
        
        # Fetch content and cache it with an expiration time of 10 seconds
        print("Fetching URL...")
        content = func(url)
        redis_store.setex(cache_key, 10, content)
        return content

    return wrapper

@cache_with_expiration
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text