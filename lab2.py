import re

# Словарь для перевода цифр в слова (ключ:значение)

digits_to_words = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}


# Функция для преобразования каждой цифры мин и макс числа прописью

def translate_number(number_str):
    result = []
    for char in number_str:
        result.append(digits_to_words[char])
    return ' '.join(result)


# Чтение файла

with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()

    pattern = r'\b\d{5,}[13579]\b'

    valid_numbers = re.findall(pattern, content)

    print(f"Найдены подходящие лексемы: {', '.join(valid_numbers)}\n")

if valid_numbers:
    min_num = valid_numbers[0]
    max_num = valid_numbers[0]

    for n in valid_numbers:
        if int(n) < int(min_num):
            min_num = n
        if int(n) > int(max_num):
            max_num = n

    print("Минимальное число прописью:")
    print(translate_number(min_num))

    print("\nМаксимальное число прописью:")
    print(translate_number(max_num))
else:
    print("Подходящих чисел не найдено.")
