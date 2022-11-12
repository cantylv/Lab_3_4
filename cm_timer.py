from datetime import datetime
from time import sleep
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Время выполнения блока = ", datetime.now() - self.start_time)


@contextmanager
def cm_timer_2():
    start_time = datetime.now()
    yield None
    print("Время выполнения блока = ", datetime.now() - start_time)
