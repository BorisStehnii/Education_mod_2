import time
from contextlib import contextmanager


class Timer:

    def __init__(self):
        self.start_time = 0
        self.finish_time = 0

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"It takes: {time.time() - self.start_time}")


@contextmanager
def timer_():
    start = time.time()
    yield None
    print(f"It takes: {time.time() - start}")


with Timer():
    a = 20_000_000
    for _ in range(a):
        pass

with timer_():
    a = 20_000_000
    for _ in range(a):
        pass

