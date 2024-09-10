#!/usr/bin/env python3

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union

def count_calls(method: Callable) -> Callable:
    '''Counts the number of times a method is called.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs):
        '''Invokes the method.
        '''
        if isinstance(self._redis, redis.Redis):
            key = method.__qualname__
            self._redis.incr(key)
        return method(self, *args, **kwargs)
    return invoker

class Cache:
    """
    Represents an object for storing data in a Redis data storage.
    Provides methods to store and retrieve data using unique keys.
    """
    
    def __init__(self) -> None:
        """
        Initializes a Cache instance.

        Sets up a connection to the Redis server and clears any existing data
        in the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis and returns a unique key.

        Args:
            data (str): The data to be stored in Redis.

        Returns:
            str: A unique key generated for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        '''Retrieves a value from a Redis data storage.
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieves a string value from a Redis data storage.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieves an integer value from a Redis data storage.
        '''
        return self.get(key, lambda x: int(x))