import os
import sys


def multi_threads(duration_seconds):
    number_cores = os.cpu_count()
    os.environ['OMP_NUM_THREADS'] = str(number_cores // 2)
    import time
    from numpy.random import rand

    def task(n):
        operations = 0
        data1 = rand(n, n)
        data2 = rand(n, n)

        start_time = time.time()
        end_time = start_time + int(duration_seconds)

        while time.time() < end_time:
            data1.dot(data2)
            operations += 1

        return operations

    min_matrix_size = 1000
    max_matrix_size = 1500
    average_operations_per_second = 0
    for size in range(min_matrix_size, max_matrix_size + (min_matrix_size // 10), 100):
        operations = task(size)
        average_operations_per_second += int(operations / int(duration_seconds))
        print(f'Matrix {size}x{size}: {operations} operations in {int(duration_seconds)} seconds')
        print(f"Operations per second: {int(operations / int(duration_seconds))}")

    return int(average_operations_per_second / ((max_matrix_size - min_matrix_size) / 100))


if __name__ == '__main__':
    res = multi_threads(sys.argv[1])
    print(res)
