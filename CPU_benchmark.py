#TODO
"""
Fix 'multi threaded tests' label (now appears twice)
Add plots for multi and single threaded tests by specific key
Add one more algorithm for multi tests

"""

import argparse
import textwrap
import time
import math
import subprocess


class CPUBenchmark:
    def __init__(self, std_duration=15, mtd_duration=15):
        """"user's duration can be set here
            by default duration is 15 seconds
        """
        # a dictionary to store benchmark results (amount of operations per second)
        self.std_duration = std_duration
        self.mtd_duration = mtd_duration
        self.results = {}

    # benchmarks for different aspects of the CPU
    def single_threaded_performance_benchmarks(self):
        print("Factorization tests are running now!")
        result_test1 = self.factorization_single_thread(duration_to_run=self.std_duration)
        print("Pi calculation tests are running now!")
        result_test2 = self.pi_calculation(duration_to_run=self.std_duration)
        print("\nMatrices multiplication tests are running now!")
        result_test3 = self.matrix_multiplication_single_thread(duration_to_run=self.std_duration)

        self.results['single_threaded_performance'] = {
            'factorization_benchmark_test': result_test1,
            'pi_calculation_benchmark_test': result_test2,
            'matrix_multiplication_benchmark_test': result_test3

        }

    def multi_threaded_performance_benchmarks(self):
        print("\n---MULTI THREADED TESTS---\n")
        print("Matrices multiplication tests are running now!")
        result_test1 = self.matrix_multiplication_multi_threads(duration_to_run=self.mtd_duration)
        self.results['multi_threaded_performance'] = {
            'first_benchmark_test': result_test1
        }

    def run_benchmark(self, keys):
        self.print_asci_banner()

        # std keys
        if keys.t_std is not None:
            self.std_duration = keys.t_std
        if not keys.no_std:
            if keys.n_std is not None:
                if keys.n_std > 1:
                    for _ in range(keys.n_std):
                        print(f"\n---SINGLE THREADED TESTS ({_+1})---\n")
                        self.single_threaded_performance_benchmarks()
            else:
                print("\n---SINGLE THREADED TESTS---\n")
                self.single_threaded_performance_benchmarks()

        # mtd keys
        if keys.t_mtd is not None:
            self.mtd_duration = keys.t_mtd
        if not keys.no_mtd:
            if keys.n_mtd is not None:
                if keys.n_mtd > 1:
                    for _ in range(keys.n_mtd):
                        print(f"\n---MULTI THREADED TESTS ({_+1})---\n")
                        self.multi_threaded_performance_benchmarks()
            else:
                print("\n---MULTI THREADED TESTS---\n")
                self.multi_threaded_performance_benchmarks()

    @staticmethod
    def print_asci_banner():
        print("""
   ___  ___         _                     _                          _    
  / __\/ _ \/\ /\  | |__   ___ _ __   ___| |__  _ __ ___   __ _ _ __| | __
 / /  / /_)/ / \ \ | '_ \ / _ \ '_ \ / __| '_ \| '_ ` _ \ / _` | '__| |/ /
/ /__/ ___/\ \_/ / | |_) |  __/ | | | (__| | | | | | | | | (_| | |  |   < 
\____|/     \___/  |_.__/ \___|_| |_|\___|_| |_|_| |_| |_|\__,_|_|  |_|\_\

 _                           _              ___                           
| |__  _   _   _ __ __ _ ___| |_ _ __      / _ \                          
| '_ \| | | | | '__/ _` / __| __| '__|____| | | |                         
| |_) | |_| | | | | (_| \__ \ |_| | |_____| |_| |                         
|_.__/ \__, | |_|  \__,_|___/\__|_|        \___/                          
       |___/                                                                                                                                                                                                                              
""")

    @staticmethod
    def factorization_single_thread(duration_to_run):
        """"As 1 operation is considered running 1 time function is_prime,
        since numbers are hard-coded, the same steps will be performed"""
        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
            return True

        operations_count = 0
        start = time.time()
        while time.time() - start < duration_to_run:
            # 2 generated prime numbers
            prime1 = 9551
            prime2 = 3877
            # semi-prime number
            number = prime1 * prime2
            j = 2
            while not is_prime(number):
                if number % j == 0:
                    number //= j
                    j = 1
                operations_count += 1
                j += 1

        elapsed_time = round(time.time() - start, 3)
        print(f"Total operations count (factorization): {'{:,}'.format(operations_count)}")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Operations per second (factorization): {'{:,}'.format(int(operations_count / elapsed_time))}\n")

        return int(operations_count / elapsed_time)

    @staticmethod
    def pi_calculation(duration_to_run):
        """"As 1 operation is considered exactly one action (line of code) in the for loop"""
        pi = 3.141592
        operations_count = 0
        start = time.time()
        while time.time() - start < duration_to_run:
            times_to_run = 1000
            for x in range(1, times_to_run):
                pi * 2**x
                float(x) / pi
                float(pi) / x
            operations_count += 3*times_to_run  # 3 operations per loop iteration

        elapsed_time = round(time.time() - start, 3)
        print(f"Total operations count (pi calculation): {'{:,}'.format(operations_count)}")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Operations per second (pi calculation): {'{:,}'.format(int(operations_count / elapsed_time))}\n")

        return int(operations_count / elapsed_time)

    @staticmethod
    def matrix_multiplication_single_thread(duration_to_run):
        """As 1 operation is considered two matrices multiplication"""
        completed_process = subprocess.run(['python3', 'single_thread.py', str(duration_to_run)],
                                           capture_output=True, text=True)
        if completed_process.returncode == 0:
            print(completed_process.stdout[:len(completed_process.stdout) - 3])
            print(f"The average number of operations per second: {completed_process.stdout[-3:-1]}")
            return
        else:
            pass

    @staticmethod
    def matrix_multiplication_multi_threads(duration_to_run):
        """As 1 operation is considered two matrices multiplication"""
        completed_process = subprocess.run(['python3', 'multi_threads.py', str(duration_to_run)],
                                           capture_output=True, text=True)
        if completed_process.returncode == 0:
            print(completed_process.stdout[:len(completed_process.stdout)-3])
            print(f"The average number of operations per second: {completed_process.stdout[-3:-1]}")
            return
        else:
            pass


if __name__ == "__main__":
    epilog = """
What aspects of the CPU tests my benchmark:
    * Single-Threaded Performance:
        * Factorization
        * Matrices multiplication
        * Calculations with pi
    * Multi-Threaded Performance:
        * Matrices multiplication
    
Benchmark test can be run separately or grouped with using specific parameters.
Result include score points for selected tests and overall average result.
"""
    parser = argparse.ArgumentParser(prog='CPU_benchmark', formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="CPU benchmark by @rastr",
                                     epilog=textwrap.dedent(epilog))
    parser.add_argument('--no_std', action='store_true',
                        help='Exclude benchmarks aimed at testing single threaded performance')
    parser.add_argument('--n_std', type=int, default=1,
                        help='Number of times to run single threaded tests')
    parser.add_argument('--t_std', type=int, help='Time for running single threaded benchmarks')
    parser.add_argument('--no_mtd', action='store_true',
                        help='Exclude benchmarks aimed at testing multi threaded performance')
    parser.add_argument('--n_mtd', type=int, default=1,
                        help='Number of times to run single threaded tests')
    parser.add_argument('--t_mtd', type=int, help='Time for running multi threaded benchmarks')
    args = parser.parse_args()
    print(args)
    benchmark = CPUBenchmark()
    benchmark.run_benchmark(args)

    print(f"Time: {benchmark.results}")
