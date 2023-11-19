# CPU benchmark by rastr

## Description

The CPU benchmark is a python project that allows you to measure and benchmark the performance of your CPU (single and multi threads) using various algorithms.
Result of the each algorithm includes: 
  * Elapsed time
  * Number of operations performed in a specific time
  * Number of operations performed in a second

## Features

-Single-threaded performance benchmarking
-Multi-threaded performance benchmarking
-Easy-to-use command-line interface
-Customizable duration for single and multi threaded benchmark tests

## Table of Contests

- [Installation](#installation)
- [Usage](#usage)
- [Benchmarking Algorithhms](#benchmarking-algorithms)
- [Contributing](#contributing)
- [License](#lisence)

## Installation
1. Clone the repository to your local system
   ```shell
   git clone https://github.com/rastr-0/CPU_benchmark.git
2. Change your working directory to the project folder:
   ```shell
   cd CPU_benchmark
3. Install the requered dependencies
   ```shell
   pip install -r requirements.txt


## Usage
The CPU Benchmark project provides a simple and convenient command-line interface (CLI) to run benchmark tests.
You can browse all the details about using CLI with the --help command.
Here are examples of using CLI:
* To run a single-threaded and multi-threaded tests with the specific time 10 seconds
  ```shell
  python3 CPU_benchmark.py --t_std 10 --t_mtd 10
* To run only single-threaded tests with the specific time 15 seconds
  ```shell
  python3 CPU_benchmark.py --no_mtd --t_std 15
* To run only multi-threaded tests 3 times with the default time(15 seconds):
  ```shell
  python3 CPU_benchmark.py --no_std --n_mtd 3
* To run a single-threaded and multi-threaded tests 3 times with the specific time 12 seconds:
  ```shell
  python3 --t_std 12 --n_std 3 --t_mtd 12 --n_mtd 3

## Benchmarking Algorithms
* Single-threaded performance: Measures how fast your CPU can perform a specific tests in a single-thread
  * Factorization
  * Pi calculation
  * Matrix multiplication
  * Fibonacci calculation
* Multi-threaded performance: Measures how fast your CPU can perform a specific tests in multi-threadeds
  * Matrix multiplication
  * Fibonacci calculation

## Problems to fix
* No ability to set the execution time of the fibonacci calculation tests
* The way fibonacci calculation is implemented for multi-threads doesn't look like good. Right now there are 2 separete files for multi/single fibonacci numbers,
  ideally, these tests should be added to other single and multi tests, respectively.

## Contributing
If you want to contribute to this project, feel free to open issues, submit pull requests, or suggest improvements.

## License
This project is licensed under the MIT License.
