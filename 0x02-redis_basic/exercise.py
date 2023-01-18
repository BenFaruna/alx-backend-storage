#!/usr/bin/env python3
"""module defines the cache class and functions associated with it"""
import redis
import uuid
from functools import wraps
from typing import Callable, Optional, Union


def replay(method: Callable) -> None:
    """display the history of calls of a particular function"""
    _self = method.__self__
    name = method.__qualname__
    key = _self.get(name)
    if key:
        count = key.decode('utf-8')
        inputs = _self._redis.lrange(name + ':inputs', 0, -1)
        outputs = _self._redis.lrange(name + ':outputs', 0, -1)

        in_out = list(zip(inputs, outputs))
        print('{}  was called {} times:'.format(name, count))
        for i, j in in_out:
            input_ = i.decode('utf-8')
            value = j.decode('utf-8')
            print('{}(*{}) -> {}'.format(name, input_, value))


def count_calls(method: Callable) -> Callable:
    """decorator function for counting method call"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """function that does the increment"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator for recording history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper adding to the db list"""
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ':outputs', output)
        return output
    return wrapper


class Cache:
    """cache class using redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key and returns string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """returns key value after converting with function fn"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """returns the value of key from the db"""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """returns the integer value of key in db"""
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
