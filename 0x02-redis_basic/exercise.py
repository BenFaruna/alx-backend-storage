#!/usr/bin/env python3
"""module defines the cache class and functions associated with it"""
import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    """cache class using redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key and returns string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]=None) -> Union[str, bytes, int, float]:
        """returns key value after converting with function fn"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

