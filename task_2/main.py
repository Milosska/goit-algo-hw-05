from src.decorators import handle_errors
from src.algorithms import binary_search


@handle_errors
def main():
    array = [
        0.05,
        0.5,
        1.1,
        1.8,
        2.2,
        3.0,
        3.7,
        4.4,
        4.9,
        5.5,
    ]

    print(binary_search(3.7, array))  # Exact match - 3.7
    print(binary_search(2.1, array))  # Find nearest value - 2.2
    print(
        binary_search(-0.1, array)
    )  # Find nearest value (given less then min element) - 0.05
    print(
        binary_search(6.2, array)
    )  # Find nearest value (given more then max element) - 6.2


if __name__ == "__main__":
    main()
