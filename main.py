"""Conduct a doubling experiment for benchmarking Python files."""

import timeit
import os
from typing import List, Tuple, Dict
import matplotlib.pyplot as plt
from collections import defaultdict


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


def determine_complexity(doubling_ratio):
    """Determine time complexity based on doubling ratio."""
    if doubling_ratio > 7.9:  # exponential
        return "Exponential"
    elif doubling_ratio > 3.9: # cubic
        return "Cubic"
    elif doubling_ratio > 1.9: # quadratic 
        return "Quadratic"
    elif doubling_ratio > 1.2: # linearithmic
        return "Linearithmic"
    elif doubling_ratio > 0.9: # linear  
        return "Linear"
    elif doubling_ratio > 0.2: # logarithm
        return "Logarithmic"
    else: # constant
        return "Constant" 


def main() -> None:
    """Read in .py files from a directory, then benchmark them."""
    directory = input("Directory to benchmark: ")
    repetitions = int(input("Number of repetitions for doubling experiment: "))
    experiment_results = doubling_experiment(directory, repetitions)

    # Initialize running totals and counts
    totals = defaultdict(float)
    counts = defaultdict(int)

    # Calculate running totals and counts
    for repetitions, doubling_ratios in experiment_results:
        for file, doubling_ratio in doubling_ratios.items():
            totals[file] += doubling_ratio
            counts[file] += 1

    # Calculate averages and determine complexities
    result_times = []
    for file in totals:
        average_ratio = totals[file] / counts[file]
        complexity = determine_complexity(average_ratio)
        result_times.append((file, average_ratio, complexity))
        print(f"{file}: Average Doubling Ratio ({average_ratio}): Runtime Complexity ({complexity})")

    # Plotting the results
    files, ratios, complexities = zip(*result_times)  # Unpacking the result_times list
    bars = plt.bar(files, ratios)
    plt.xlabel('File')
    plt.ylabel('Average Doubling Ratio')
    plt.title('Doubling Experiment Results')

    # Increase the space on the y-axis
    plt.ylim(0, max(ratios) * 1.2)  # Increase the y-limit to 120% of the maximum ratio

    # Adding the complexity as a label on top of each bar
    for bar, complexity in zip(bars, complexities):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, complexity, ha='center', va='bottom')

    plt.xticks(rotation=90)  # Rotating the x-axis labels for better visibility

    # Increase the space at the bottom of the plot
    plt.subplots_adjust(bottom=0.2)

    plt.show()

if __name__ == "__main__":
    main()