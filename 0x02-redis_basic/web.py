#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker  """

from functools import wraps
import redis
import requests
from typing import Callable

redis = redis.Redis()


def count_req(method: Callable) -> Callable:
    """ Decorator count how many request """

    @wraps(method)
    def wrapper(url):
        """ Wrapper """
        redis.incr(f"count:{url}")
        cached = redis.get(f"cached:{url}")

        if cached:
            return cached.decode('utf-8')

        html = method(url)
        redis.setex(f"cached:{url}", 10, html)

        return html

    return wrapper


@count_req
def get_page(url: str) -> str:
    """ get a page """
    response = requests.get(url)
    return response
