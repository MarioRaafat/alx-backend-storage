#!/usr/bin/env python3

import uuid
import redis

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