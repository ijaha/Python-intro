# Напишите программу, которая циклично запрашивает у пользователя номера символов по таблице Unicode
# и выводит соответствующие им символы. Завершает работу при вводе нуля.

try:
    symbol = int(input('Введите номер символа по таблице Unicode: '))
except ValueError:
    symbol = int(input('Введите (целое число / номер символа) по таблице Unicode: '))

while symbol != 0:
    print(chr(symbol))
    symbol = int(input('Введите номер символа по таблице Unicode: '))
