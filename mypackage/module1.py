import random

def generate_random_numbers(file_name: str, count: int):
    """Заполняет файл случайными целыми числами."""
    with open(file_name, 'w') as f:
        for _ in range(count):
            f.write(f"{random.randint(1, 100)}\n")  # Случайные числа от 1 до 100

def remove_duplicates(input_file: str, output_file: str):
    """Удаляет дубликаты из файла и записывает уникальные числа в новый файл."""
    with open(input_file, 'r') as f:
        numbers = f.readlines()
    
    unique_numbers = set(int(num.strip()) for num in numbers)  # Используем set для удаления дубликатов

    with open(output_file, 'w') as g:
        for num in sorted(unique_numbers):
            g.write(f"{num}\n")  # Сортируем перед записью

def print_file(file_name: str):
    """Выводит содержимое файла на печать."""
    with open(file_name, 'r') as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    # Пример использования
    generate_random_numbers('f.txt', 20)  # Заполняем файл f случайными числами
    remove_duplicates('f.txt', 'g.txt')    # Удаляем дубликаты и записываем в g
    print_file('g.txt')                     # Печатаем содержимое g
