def count_letters(sentence):
    # Инициализация словаря для подсчета букв
    letter_count = {}

    # Приведение предложения к нижнему регистру
    sentence = sentence.lower()

    # Перебор каждого символа в предложении
    for char in sentence:
        # Проверка, является ли символ буквой
        if char.isalpha():
            # Увеличение счетчика для данной буквы
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count


# Пример использования
sentence = input("Введите предложение: ")
result = count_letters(sentence)
print(result)
