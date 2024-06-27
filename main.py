def get_multiplied_digits(number):
    """Рекурсивное умножение цифр"""
    str_number = str(number)    #строковое представление(str) числа number
    first = int(str_number[0])  #отделение первой цифры в числе
    while len(str_number) > 1:  #условие: длина str_number больше 1
        return first * get_multiplied_digits(int(str_number[1:]))  #умножите первую цифру числа на результат
                                                   # работы этой же функции с числом, но уже без первой цифры
    if len(str_number) <= 1:    #Если же длина str_number не больше 1,
        return first            #тогда вернуть оставшуюся цифру first


result = get_multiplied_digits(40203)
print(result)