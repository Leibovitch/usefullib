from functools import wraps
from time import time

def timing(is_active):
    ''' call a function a number of times '''
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ts = time()
            result = fn(*args, **kwargs)
            te = time()
            if is_active:
                print('func:%r args:[%r, %r] took: %2.4f sec' % (fn.__name__, args, kwargs, te-ts))

            return result
        return wrapper
    return decorate