
import cProfile, pstats
import io

# iterative is faster than recursion in fibonacci
# O(n) = 2^n in recursion
def profiler(function):
    def wrapper(*args,**kwargs):
        file_object = io.StringIO()
        pr = cProfile.Profile()
        pr.enable()
        return_value = function(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr, stream=file_object).sort_stats('cumulative')
        ps.print_stats()
        print(file_object.getvalue())
        return return_value
    return wrapper


@profiler
def fibo(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a+b
    return a

@profiler
def wrap_fibonacci(x):
    def fibo_rec(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fibo_rec(n-1)+fibo_rec(n-2)
    return fibo_rec(x)



value = fibo(900)
print(value)
value = wrap_fibonacci(30)
print(value)

