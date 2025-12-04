from src.decorators import handle_errors
from src.handlers import read_file_and_find_pattern


@handle_errors
def main():
    print("\n Starting analysis for Стаття 1.")

    correct_patterns_one = [
        "популярних алгоритмів",
        "Фундаментальні знання допомагають дізнатися, що всередині",
        "Алгоритм ділить вхідну колекцію на рівні половини, і з кожною ітерацією "
        "порівнює цільовий елемент з елементом у середині. Пошук закінчується при знаходженні елемента.",
    ]
    read_file_and_find_pattern(
        "task_3/src/articles/article_1.txt", correct_patterns_one
    )

    print("\n Starting analysis for Стаття 2.")

    correct_patterns_two = [
        "Постановка проблеми",
        "Випадковим чином обирається контрольна сесія, для якої буде сформовано рекомендацію.",
        "Експерименти проводилися на комп’ютері з процесором AMD Ryzen 5 3600 та 32 Гб оперативної пам’яті. "
        "Для формування рекомендацій було використано колаборативну фільтрацію.",
    ]
    read_file_and_find_pattern(
        "task_3/src/articles/article_2.txt", correct_patterns_two
    )

    print("\n Analysis completed.")


if __name__ == "__main__":
    main()
