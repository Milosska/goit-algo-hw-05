from src.classes import HashTable
from src.decorators import handle_errors


@handle_errors
def main():
    # Тестуємо нашу хеш-таблицю:
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    print(H.get("apple"))  # Виведе: 10
    print(H.get("orange"))  # Виведе: 20
    print(H.get("banana"))  # Виведе: 30

    print(H.delete("apple"))  # Виведе: ['apple', 10]
    print(H.delete("prune"))  # Викине помилку 'Key is not in the hash table.'


if __name__ == "__main__":
    main()
