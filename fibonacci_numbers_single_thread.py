import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor


def fibonacci(n):
    # start the sequence
    f0, f1 = 0, 1
    # compute the nth number
    for _ in range(0, n):
        f0, f1 = f1, (f1 + f0)
    return f0


def fibonacci_calculation(amount_of_fi_numbers):
    with ProcessPoolExecutor(max_workers=1) as executor:
        start_time = time.time()
        numbers = range(int(amount_of_fi_numbers))
    # calculate fibonacci numbers
        executor.map(fibonacci, numbers)

    elapsed_time = time.time() - start_time
    print(f"Executed in {round(elapsed_time, 2)} seconds with single thread")


if __name__ == '__main__':
    fibonacci_calculation(sys.argv[1])