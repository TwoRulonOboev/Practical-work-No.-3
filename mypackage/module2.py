def count_word_in_text(file_name: str, word: str) -> int:
    """Возвращает количество вхождений слова в текстовом файле."""
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()  
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден.")
        return 0
    except IOError:
        print(f"Ошибка при чтении файла '{file_name}'.")
        return 0

    words = text.lower().split()
    return words.count(word.lower()) 

if __name__ == "__main__":
    word_to_find = input('')
    occurrences = count_word_in_text('text.txt', word_to_find)
    print(f'Слово "{word_to_find}" встречается {occurrences} раз(а).')
