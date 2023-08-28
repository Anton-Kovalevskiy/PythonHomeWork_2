# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

from random import randint

def CoinsLine(n):
    coins = []
    print("Получен ряд монеток: ")
    for i in range (n):
        coins.append (randint(0, 1))
        print(coins[i], end = " ")
    print()
    return coins


def FindMinCoins (coins):
    averse = 0
    reverse = 0
    result = 0
    for i in range(len(coins)):
        if coins [i] == 0:
            averse += 1
        else:
            reverse +=1
    if averse > reverse:
        result = reverse
    else:
        result = averse
    return result


print ("Введите количество монет n на столе:")
n = int(input())
coins = CoinsLine(n)
print("Минимальное количество монеток, которое нужно перевернуть равно ", FindMinCoins(coins))

