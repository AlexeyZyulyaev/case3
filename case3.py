#Импорт библиотеки для работы с математическими функциями
import math
def maxDragonPower(N):
    if N in [1,2,3]:
        return N

    power = 1

    count_of_third = N // 3

    if N % 3 == 1:
        count_of_third -= 1
        power *= 4  
    elif N % 3 == 2:
        power *= 2 
    else:  
        pass

    # Умножаем на нужное количество троек
    power *= math.pow(3, count_of_third)

    return power
# Пример использования
n = int(input("Введите количество голов: "))
print("Максимальная сила стаи:", maxDragonPower(n))