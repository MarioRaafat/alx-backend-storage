import requests
import redis
from functools import wraps

# Initialize Redis connection
redis_store = redis.Redis()

def cache_with_expiration(func):
    """
    Decorator to cache the result of a function call and count how many times a URL was accessed.
    The cache expires after 10 seconds.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """
        Wrapper function to handle caching and counting of URL accesses.
        """
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
    """
    Fetches the HTML content of a URL using the requests module.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    response.raise_for_status()  # Ensure any request errors are raised
    return response.text


if __name__ == "__main__":
    # Example usage
    url = "http://google.com"
    print(get_page(url))  # Fetches from the web and caches the result
    print(get_page(url))  # Should hit the cache
