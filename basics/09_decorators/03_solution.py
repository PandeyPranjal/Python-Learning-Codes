#3. Cache Return Values
#Problem: Implement a decorator that caches the return values fo a function, so that when it's called with the same argument, the cached value is returned instead 
import time

def cache(func):
    cache_value={} 
    print (cache_value)
    def wrapper(*args):
        if args in  cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result 
    return wrapper


@cache
def longRunningFunc(a, b):
    time.sleep(4)
    return a+b


print(longRunningFunc(2, 3))
print(longRunningFunc(2, 3))
print(longRunningFunc(2, 3))
