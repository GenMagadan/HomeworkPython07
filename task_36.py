# Напишите функцию print_operation_table(operation, num_rows=6,
# num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы
# num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет
# с единицы (подумайте, почему не с нуля). Примечание: бинарной
# операцией называется любая операция, у которой ровно два
# аргумента, как, например, у операции умножения. Пример:
# Ввод: `print_operation_table(lambda x, y: x * y)`
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# def print_op(oper, row, col):
#     for i in range(1, row + 1):
#         print(*list(map(oper, [i]*col, range(1, col + 1))))


# print_op(lambda x, y: x * y, 6, 6)

# Более красивый вариант
def print_operation(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        print()
        for j in range(1, num_columns + 1):
            if operation(i, j) > 9:
                print(operation(i, j), end="  ")
            else:
                print(operation(i, j), end="   ")


print_operation(lambda x, y: x * y, 7, 7)
