# 0x02. Redis

## Tasks
0. Writing strings to Redis

Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.

Create a `store` method that takes a data argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.

File: [exercise.py](./exercise.py)
   
1. Reading from Redis and recovering original type

In this exercise we will create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

Remember to conserve the original Redis.get behavior if the key does not exist.

Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize Cache.get with the correct conversion function.

The following code should not raise:
```
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

File: [exercise.py](./exercise.py)
   
2. Incrementing values

In this task, we will implement a system to count how many times methods of the Cache class are called.

Above Cache define a `count_calls` decorator that takes a single method Callable argument and returns a Callable.

As a key, use the qualified name of method using the `__qualname__` dunder method.

Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.

Protip: when defining a decorator it is useful to use `functool.wraps` to conserve the original function’s name, docstring, etc.

Decorate `Cache.store` with `count_calls`

File: [exercise.py](./exercise.py)
   
3. Storing lists

In this task, we will define a `call_history` decorator to store the history of inputs and outputs for a particular function.

Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.

In `call_history`, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.

`call_history` has a single parameter named method that is a Callable and returns a Callable.

In the new function that the decorator will return, use `rpush` to append the input arguments.

Decorate `Cache.store` with call_history.

File: [exercise.py](./exercise.py)
   
4. Retrieving lists

In this tasks, we will implement a replay function to display the history of calls of a particular function.

Use keys generated in previous tasks to generate the following output:

```sh
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```
File: [exercise.py](./exercise.py)
   
5. Implementing an expiring web cache and tracker

In this tasks, we will implement a `get_page` function (prototype: `def get_page(url: str) -> str:`). The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.

Inside `get_page` track how many times a particular URL was accessed in the key `"count:{url}"` and cache the result with an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow response and test your caching.

File: [web.py](./web.py)
