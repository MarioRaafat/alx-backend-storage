#!/usr/bin/env python3

import uuid
import redis
from typing import Any, Callable, Union

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

    def store(self, data: str) -> str:
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