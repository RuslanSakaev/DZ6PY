# Задайте число. Составьте список чисел Фибоначчи

# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Должно быть введено целое число")
#     return number

# def fib(n):#возвращает член последовательности фибоначчи
#     if n in [1, 2]:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return fib(n-1) + fib(n-2)


# def sequense_of_fibs(n: int) -> list[int]: #возвращает последовательность фибоначчи
#     list2 = [fib(i) for i in range(1, n+1)]
#     return list2

# num = InputNumbers("Введите число: ")

# print(sequense_of_fibs(num))

"""Укороченный код"""

fib = (lambda n, fib=[1,1]: fib[:n]+[fib.append(fib[-1] + fib[-2]) or fib[-1] for i in range(n-len(fib))])

print(fib(10))