import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time:.6f} секунд")
        return result
    return wrapper

@measure_time
def function1():
    for _ in range(1000000):
        pass

@measure_time
def function2():
    for _ in range(500000):
        pass

function1()
function2()