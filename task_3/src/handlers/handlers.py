import timeit
from typing import Callable

from src.algorithms import kmp_search, boyer_moore_search, rabin_karp_search


def measure_search_time(
    results: dict[str, float], search_func: Callable, text: str, pattern: str
) -> None:
    measured_func = timeit.timeit(stmt=lambda: search_func(text, pattern), number=1)
    results[search_func.__name__] = measured_func


def compare_search_algorithms(text: str, pattern: str) -> None:
    results: dict[str, float] = {}

    # KMP Search Algorithm
    measure_search_time(results, kmp_search, text, pattern)

    # Boyer-Moore Search Algorithm
    measure_search_time(results, boyer_moore_search, text, pattern)

    # Rabin_Karp Search Algorithm
    measure_search_time(results, rabin_karp_search, text, pattern)

    for key, time in results.items():
        print(f" -- Pattern is found by {key} during {time} seconds.")


def run_all_scenarios_for_text(text: str, patterns: list[tuple[str, str]]) -> None:
    for pattern_array in patterns:
        for index, pattern in enumerate(pattern_array):
            pattern_type = "real" if index == 0 else "fake"
            scenarios = [
                (f"short {pattern_type} pattern", pattern),
                (f"medium {pattern_type} pattern", pattern),
                (f"long {pattern_type} pattern", pattern),
            ]

            for label, string_pattern in scenarios:
                print(f"\n Searching {label}.")
                compare_search_algorithms(text, string_pattern)


def read_file_and_find_pattern(path_to_file: str, correct_patterns: list[str]):
    with open(path_to_file, "r", encoding="utf-8", errors="replace") as fh:
        text_1 = " ".join([el.strip() for el in fh.readlines()])
        patterns = [
            (correct_patterns[0], "silver moonlight"),
            (
                correct_patterns[1],
                "ancient forests hide forgotten magic secrets",
            ),
            (
                correct_patterns[2],
                "As the last embers of the fire faded, the travelers realized they were no longer alone in the silent valley. "
                "A faint whisper drifted through the cold night air, carrying a warning older than the mountains themselves.",
            ),
        ]

        run_all_scenarios_for_text(text_1, patterns)
        fh.close()
