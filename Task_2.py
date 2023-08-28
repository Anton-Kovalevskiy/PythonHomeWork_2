# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

from random import randint
from math import sqrt

x = randint(0, 1000)
y = randint(0, 1000)
s = x + y
print("Сумма чисел равна:", s)
p = x * y
print("Произведение чисел равно:", p)

def KatesResult(s, p):
    x0 = (s + sqrt(s * s - 4 * p))/2
    y0 = s - x0
    return x0, y0

print("Ответ Кати: Петя загадал числа", KatesResult(s, p))