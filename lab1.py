# Словарь для преобразования всех цифр прописью
digits_to_words = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}


# Функция для преобразования мин и макс числа прописью
def translate_number(number_str):
    result = []
    for char in number_str:
        result.append(digits_to_words[char])
    return " ".join(result)


valid_numbers = []

# Эмуляция чтения бесконечной последовательности
try:
    with open('test.txt', 'r', encoding='utf-8') as file:
        while True:
            block = file.read(1024)
            if not block:
                break

            words = block.split()

            for word in words:
                if word.isdigit():
                    if len(word) > 5:
                        last_digit = int(word[-1])
                        if last_digit % 2 != 0:
                            valid_numbers.append(word)
                            print(f"Найдена подходящая лексема: {word}\n")


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

except FileNotFoundError:
    print("Файл test.txt не найден.")