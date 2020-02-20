# fibonacci
#  fib [0,1,1,2,3,5,8] just add two previous
# create cache = global
cache = {}
# two steps to using a cache

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
# check if number is already in cache and return chached n if true
    if n in cache:
        return cache [n]
    else:
        value = fib(n-1) + fib(n-2)
        # store val in cache
        cache[n] = value
        return value

print (fib(3))