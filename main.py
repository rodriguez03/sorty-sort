"""Conduct a doubling experiment for benchmarking Python files."""

import timeit
import random
import string
import contextlib
from typing import Union
import os
from typing import List, Tuple, Dict


def generate_data(data_type: str, size: int):
    """Generate a list of data of the specified type and size."""
    if data_type == "int":
        return [random.randint(0, 100) for _ in range(size)]
    elif data_type == "str":
        return [
            "".join(random.choices(string.ascii_letters + string.digits, k=5))
            for _ in range(size)
        ]
    else:
        raise ValueError("Invalid data type. Expected 'int' or 'str'.")


def benchmark(file: str, data: List) -> float:
    """Benchmarks the execution time of a Python file."""
    with open("sorting_algorithms/" + file, "r") as f:
        code = compile(f.read(), file, "exec")
    # Timing the execution of the code
    with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
        execution_time = timeit.timeit(lambda: exec(code, {"data": data}), number=1)
    return execution_time


def doubling_experiment(
    file: str, data_type: str, start_size: int, total_repetitions: int
) -> List[Tuple[int, float, Union[float, str]]]:
    """Conducts a doubling experiment for benchmarking."""
    results = []
    # Begin with a small number of repetitions
    repetitions = 1
    prev_time = 0
    for _ in range(total_repetitions):
        data = generate_data(data_type, start_size * repetitions)
        current_time = benchmark(file, data)
        doubling_ratio = "N/A" if repetitions == 1 else current_time / prev_time
        results.append((repetitions, current_time, doubling_ratio))
        prev_time = current_time
        repetitions *= 2
    return results


def determine_complexity(doubling_ratio: float) -> str:
    """Determine time complexity based on doubling ratio."""
    if doubling_ratio > 7.8:  # exponential
        return "Exponential"
    elif doubling_ratio > 3.8:  # cubic
        return "Cubic"
    elif doubling_ratio > 1.8:  # quadratic
        return "Quadratic"
    elif doubling_ratio > 1.2:  # linearithmic
        return "Linearithmic"
    elif doubling_ratio > 0.8:  # linear
        return "Linear"
    elif doubling_ratio > 0.2:  # logarithm
        return "Logarithmic"
    else:  # constant
        return "Constant"


def main() -> None:
    """Read in .py files from a directory, then benchmark them."""
    # header
    print("")
    print("Welcome to your Algorithm Analysis Tool!")
    print("")
    # inputs
    directory = input("File to benchmark: ")
    data_type = input("Type of data to use (int,str): ")
    while True:
        try:
            start_size = int(input("Start size of list of data: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    total_repetitions = 5
    experiment_results = doubling_experiment(
        directory, data_type, start_size, total_repetitions
    )
    # outputs
    print("")
    sum_doubling_ratios = 0
    count_doubling_ratios = 0
    for i, (repetitions, total_time, doubling_ratio) in enumerate(
        experiment_results, start=1
    ):
        if isinstance(doubling_ratio, str):
            print(
                f"Run {i:2} of {total_repetitions} for {directory} operation with {data_type} list using size {start_size * repetitions:5} took {total_time:.10f} seconds and had a doubling ratio of {doubling_ratio:>12}"
            )
        else:
            print(
                f"Run {i:2} of {total_repetitions} for {directory} operation with {data_type} list using size {start_size * repetitions:5} took {total_time:.10f} seconds and had a doubling ratio of {doubling_ratio:.10f}"
            )
            sum_doubling_ratios += doubling_ratio
            count_doubling_ratios += 1
    print("")
    # predicted big O output
    average_doubling_ratio = (
        sum_doubling_ratios / count_doubling_ratios if count_doubling_ratios else "N/A"
    )
    print(f"Average Doubling Ratio: {average_doubling_ratio}")
    print(f"Predicted Time Complexity: {determine_complexity(average_doubling_ratio)}")
    print("")


if __name__ == "__main__":
    main()
