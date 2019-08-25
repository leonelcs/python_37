from functools import  wraps

def max_len(m):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if len(result) > m:
                print("The length of the string is bigger than allowed")
            return result
        return wrapper
    return decorator

def min_len(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if len(result) < n:
                print("The length of the string is smaller than allowed")
            return result
        return wrapper
    return decorator

@min_len(0)
@max_len(5)
def imprime(s):
    return s

print("teste")
print(imprime("a"))
print(imprime(""))
print(imprime("skldfalsdf"))

