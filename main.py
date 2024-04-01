"""Conduct a doubling experiment for benchmarking Python files."""

import timeit
import os
from typing import List, Tuple, Dict


def read_files(directory: str) -> List[str]:
    """Reads all Python files in a directory and returns a list of file names."""
    py_files = []
    for file in os.listdir(directory):
        if file.endswith(".py"):
            py_files.append(os.path.join(directory, file))
    return py_files


def benchmark(files: List[str]) -> Dict[str, List[float]]:
    """Benchmarks the execution time of each Python file in a list."""
    results = {}
    for file in files:
        with open(file, "r") as f:
            code = f.read()
        # Timing the execution of the code
        execution_time = timeit.timeit(code, number=1)
        results[file] = [execution_time]
    return results


def doubling_experiment(
    directory: str, total_repetitions: int
) -> List[Tuple[int, Dict[str, List[float]]]]:
    """Conducts a doubling experiment for benchmarking."""
    files = read_files(directory)
    results = []
    # Begin with a small number of repetitions
    repetitions = 1
    prev_times = {}
    while repetitions <= total_repetitions:
        current_results = benchmark(files)
        if prev_times:
            doubling_ratios = {}
            for file, current_time in current_results.items():
                prev_time = prev_times[file][-1]
                doubling_ratio = current_time[0] / prev_time
                doubling_ratios[file] = doubling_ratio
            results.append((repetitions, doubling_ratios))
        else:
            results.append((repetitions, {}))
        prev_times = current_results
        repetitions *= 2
    return results


def main() -> None:
    """Read in .py files from a directory, then benchmark them."""
    directory = input("Directory to benchmark: ")
    repetitions = int(input("Number of repetitions for doubling experiment: "))
    experiment_results = doubling_experiment(directory, repetitions)
    print("Experiment Results:")
    for repetitions, doubling_ratios in experiment_results:
        print(f"\nRepetitions: {repetitions}")
        for file, doubling_ratio in doubling_ratios.items():
            print(f"\t{file}: Doubling Ratio - {doubling_ratio}")


if __name__ == "__main__":
    main()
