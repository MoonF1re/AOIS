class FixedMatrix:
    def __init__(self):
        self.size = 16
        self.data = [
            [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0]
        ]

    def display_matrix(self):
        for row in self.data:
            print(" ".join(map(str, row)))

    def get_value(self, row, col):
        return self.data[row][col]

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def extract_word(self, idx):
        # Извлечение вертикального слова из матрицы
        return ''.join(str(self.data[(idx + i) % self.size][idx]) for i in range(self.size))

    def function_one(self, word1, word2):
        return ''.join('1' if a == '1' and b == '1' else '0' for a, b in zip(word1, word2))

    def function_fourteen(self, word1, word2):
        return ''.join('0' if a == '1' and b == '1' else '1' for a, b in zip(word1, word2))

    def function_three(self, word1, word2):
        return word1

    def function_twelve(self, word1, word2):
        return ''.join('0' if a == '1' else '1' for a in word1)

    def add_ab(self, prefix):
        # Поиск и изменение слова с заданным префиксом
        found_word = ""
        pos = 0

        for i in range(self.size):
            word = self.extract_word(i)
            if word.startswith(prefix):
                found_word = word
                pos = i
                break

        if not found_word:
            return ""

        V, A, B = found_word[:3], found_word[3:7], found_word[7:11]
        total_ab = int(A, 2) + int(B, 2)
        S = format(total_ab, '05b')
        new_word = V + A + B + S

        self.update_word(pos, new_word)
        return new_word

    def update_word(self, idx, word):
        # Обновление вертикального слова в матрице
        for i in range(self.size):
            self.data[i][idx] = int(word[i])

    # def menu(self):
    #     while True:
    #         print("\nМеню:")
    #         print("1. Показать матрицу")
    #         print("2. Получить значение")
    #         print("3. Изменить значение")
    #         print("4. Извлечь слово")
    #         print("5. Добавить AB")
    #         print("6. И (f1)")
    #         print("7. НЕ-И (f14)")
    #         print("8. ДА (f3)")
    #         print("9. НЕ (f12)")
    #         print("10. Выход")
    #
    #         choice = input("Выберите опцию: ")
    #
    #         if choice == '1':
    #             self.display_matrix()
    #         elif choice == '2':
    #             row = int(input("Введите номер строки: "))
    #             col = int(input("Введите номер столбца: "))
    #             print("Значение:", self.get_value(row, col))
    #         elif choice == '3':
    #             row = int(input("Введите номер строки: "))
    #             col = int(input("Введите номер столбца: "))
    #             value = int(input("Введите новое значение: "))
    #             self.set_value(row, col, value)
    #         elif choice == '4':
    #             idx = int(input("Введите индекс: "))
    #             print("Слово:", self.extract_word(idx))
    #         elif choice == '5':
    #             prefix = input("Введите префикс: ")
    #             print("Новое слово:", self.add_ab(prefix))
    #         elif choice == '6':
    #             idx = int(input("Введите индекс 1-го слова: "))
    #             print("Слово №1:", self.extract_word(idx))
    #             idx2 = int(input("Введите индекс 2-го слова: "))
    #             print("Слово №2:", self.extract_word(idx2))
    #             print("Ваше слово: ", self.function_one(self.extract_word(idx),self.extract_word(idx2)))
    #         elif choice == '7':
    #             idx = int(input("Введите индекс 1-го слова: "))
    #             print("Слово №1:", self.extract_word(idx))
    #             idx2 = int(input("Введите индекс 2-го слова: "))
    #             print("Слово №2:", self.extract_word(idx2))
    #             print("Ваше слово: ", self.function_fourteen(self.extract_word(idx), self.extract_word(idx2)))
    #         elif choice == '8':
    #             idx = int(input("Введите индекс 1-го слова: "))
    #             print("Слово №1:", self.extract_word(idx))
    #             idx2 = int(input("Введите индекс 2-го слова: "))
    #             print("Слово №2:", self.extract_word(idx2))
    #             print("Ваше слово: ", self.function_three(self.extract_word(idx), self.extract_word(idx2)))
    #         elif choice == '9':
    #             idx = int(input("Введите индекс 1-го слова: "))
    #             print("Слово №1:", self.extract_word(idx))
    #             idx2 = int(input("Введите индекс 2-го слова: "))
    #             print("Слово №2:", self.extract_word(idx2))
    #             print("Ваше слово: ", self.function_twelve(self.extract_word(idx), self.extract_word(idx2)))
    #         elif choice == '10':
    #             break
    #         else:
    #             print("Неверная опция. Пожалуйста, попробуйте снова.")


# matrix = FixedMatrix()
# matrix.menu()