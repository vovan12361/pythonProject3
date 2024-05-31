import copy
from datetime import datetime
from random import randint, random

str1 = "abcdefghjklmnqprst"

print("5_1")
print(str1[:8])
print(str1[(len(str1) // 2):(len(str1) // 2 + 4)])
print(str1[-5:])

print("5_2")
print(str1[::-1])

print("5_3")
print(str1[1::2])

print("5_4")
print(str1[::2] + str1[1::2])

print("5_5")

year = datetime.now().year.__str__()
day = datetime.now().day.__str__()
month = datetime.now().month.__str__()
print(day + "/" + month + "/" + year)

print("5_6")

str1 = "C:\\Users\\vovan\\PycharmProjects\\pythonProject3\\main.py".split("\\")
print("\n".join(str1))

print("5_7")
str1 = "1+25+3".split("+")
integ = list(map(int, str1))
print(sum(integ))


def check_palindrom(str):
    return print(str == str[::-1])


print("5_8")
str1 = "saippuakivikauppias"
str2 = "топот"
str3 = "чайник"
check_palindrom(str1)
check_palindrom(str2)
check_palindrom(str3)

print("5_9")
list_names = ['Danil Danilovich', 'Vladimir Vladimirovich', 'Aleksey Alekseevich', 'Artem Artemovich',
              'Rishat Rishatovich']
holiday = list("день открытых дверей")
for i in range(len(list_names)):
    str1 = "--------------" \
           "\nУважаемый (ая), {}!" \
           "\nПриглашаем Вас на {}" \
           "\nДата события: {} мая." \
           "\nС уважением, Василий.".format(list_names[i], ''.join(holiday), i + 1)
    print(str1)

print("6_1")
print(sum(map(int, input().split('+'))))

print("6_2")


def _6_2():
    l = list(map(int, input().split(" ")))
    print(str(max(l)) + " " + str(min(l)))
    l.remove(max(l))
    l.remove(min(l))
    print(str(sum(l)) + " " + str(sum(l) / len(l)))
    print(str(max(l)) + " " + str(min(l)))

_6_2()

print("6_3")

def _6_3():
    l = list(input())
    l_copy = copy.copy(l)
    l.reverse()
    print(l == l_copy)

_6_3()

print("6_4")


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_prime_numbers(arr):
    prime_numbers = []
    for num in arr:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


def _6_4():
    l = [randint(10, 1000) for _ in range(30)]
    prime_numbers = get_prime_numbers(l)
    print(prime_numbers)

_6_4()

print("6_5")


def _6_5():
    l = input().split(" ")
    summa = 0
    for i in l:
        num = int(i)
        summa += num
    print(summa / len(l))

_6_5()

print("6_6")
l = [randint(1, 100) for i in range(15)]


def _6_6():
    mini = int(input("Min num:"))
    maxi = int(input("Max num:"))
    print(l)
    arr = [i for i in range(len(l)) if mini <= l[i] <= maxi]
    print(len(l))
    print(arr)

_6_6()

print("6_7")


def _6_7():
    mini = int(input("Min num:"))
    maxi = int(input("Max num:"))
    arr1 = [i for i in l if mini <= i <= maxi]
    for i in arr1:
        l.remove(i)
    # print(arr)
    print(l)

_6_7()

print("7_1")
arr = [randint(1, 100) for _ in range(5)]
print(arr)
for i in arr:
    if i % 3 == 0:
        print(f"Есть число кратное трём, это число: {i}")
        break
else:
    print("Не нашли")

print("7_2")
arr = [randint(0, 4) for _ in range(10)]
print(f"Массив {arr}")
x = int(input("Введите число для поиска:"))
for i in arr:
    if i == x:
        print(i)

print("7_3")


def find_max(array):
    mini = min(array)
    ind = 0
    for i in range(len(array)):
        if array[i] >= mini:
            mini = array[i]
            ind = i
    return ind


arr = [randint(1, 10) for _ in range(10)]
print(arr)
print(f"Last index of max elem:{find_max(arr)}.\n"
      f" First index of min elem:{arr.index(min(arr))}")

print("7_4")
arr = [randint(1, 100) for i in range(10)]
print(arr)
arr.sort(reverse=True)
print(arr)

print("7_5")


def f(n1, n2):  # компаратор - сравнение по первым цифрам
    s1 = str(n1)
    s2 = str(n2)
    if s1[0] > s2[0]:
        return 1
    elif s1[0] < s2[0]:
        return -1
    else:
        return 0


def quickSort(arr, comp):  # быстрая сортировка с компаратором
    n = len(arr)
    if n <= 1:
        return arr
    sep = arr[0]
    lft = [x for x in arr[1:] if comp(x, sep) <= 0]
    rgh = [x for x in arr[1:] if comp(x, sep) > 0]
    return quickSort(lft, comp) + [sep] + quickSort(rgh, comp)


arr = [randint(1, 100) for _ in range(10)]
print(arr)
print(quickSort(arr, f))

print()

print(arr)
arr = [randint(1, 100) for i in range(10)]
arr.sort(key=lambda n: str(abs(n))[0])  # сортировка
print(arr)

print("7_6")

print("7_7")
arr = [randint(1, 10) for i in range(10)]
arr = quickSort(arr, f)
res = []
for i in arr:
    if res.count(i) == 0:
        res.append(i)
print(arr)
print(res)

print("7_8")
arr = [randint(1, 5) for _ in range(10)]
print(arr)
n = 10
series = []
seriesLength = []
length = 1
series.append(arr[0])
for i in range(1, n):
    if arr[i] == arr[i - 1]:
        length += 1
    else:
        seriesLength.append(length)
        length = 1
        series.append(arr[i])
seriesLength.append(length)
for i in range(len(seriesLength)):
    print(f"{seriesLength[i]} - {series[i]}")

print("7_9")
arr = [randint(1, 25) for _ in range(10)]
print(arr)
for i in range(n - 1):
    isChange = False
    for j in range(n - 2, i - 1, -1):
        if arr[j + 1] < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            isChange = True
    if not isChange:
        break
print(arr)

print("7_10")
arr = [randint(1, 10) for _ in range(10)]
arr = quickSort(arr, f)
maxi = -1
for i in arr:
    if arr.count(i) > 1 and i > maxi:
        maxi = i
print(arr)
print(maxi)

print("8_0(1)")
t = [[-8, -14, -19, -18],
     [25, 28, 26, 20],
     [11, 18, 20, 25]]
print(f"2 метеостанция, 4 день: {t[1][3]}\n"
      f"3 метеостанция, 1 день: {t[2][0]}")

print("8_0(2)")
for i in range(3):
    print(t[i][1])

print("8_0(3)")
mean = 1
for i in range(4):
    print(t[2][i], end=' ')
    mean += t[2][i]
print(f"\n{mean / 4}")

print("8_0(4)")
for i in range(3):
    for j in range(4):
        if 24 <= t[i][j] <= 26:
            print(f"Температура на {i + 1} метеостанции в {j + 1} день была: {t[i][j]}")

def printMatrix ( matrix ):
   for row in matrix:
      for x in row:
          print ( "{:4d}".format(x), end = "" )
      print ()


print("8_1")

matrix = [[0] * 3 for i in range(3)]
for i in range(3):
    for j in range(3):
        matrix[i][j] = randint(30, 60)
        print ( "{:4d}".format(matrix[i][j]), end = "" )
    print()

mini = 0
maxi = 61
min_ind = [-1,-1]
max_ind = [-1,-1]
for i in range(3):
    for j in range(3):
        if matrix[i][j] < maxi:
            maxi = matrix[i][j]
            max_ind = [i, j]
        if matrix[i][j] > mini:
            mini = matrix[i][j]
            min_ind = [i, j]
print(f"Max ind: {min_ind} = {mini}")
print(f"Min ind: {max_ind} = {maxi}")

print("8_2")
matrix = [[randint(1,40)] * 3 for i in range(3)]
for i in range(3):
    for j in range(3):
        matrix[i][j] = randint(30, 60)
        print ( "{:4d}".format(matrix[i][j]), end = "" )
    print()

maxi = 0
ind = 0
for row in matrix:
    s = sum(row)
    print(s)
    if s > maxi:
        maxi = s
        ind = matrix.index(row)
print(f"Max sum of {matrix[ind]} is {maxi}")
n = 5
def createMatrix(a,b):
    matrix = [[0] * b for i in range(a)]
    for i in range(a):
        for j in range(b):
            matrix[i][j] = randint(10, 35)
            print ( "{:4d}".format(matrix[i][j]), end ="")
        print()
    return matrix

print("8_3")
matrix = createMatrix(n,n)
mini = 100
for i in range(n):
    for j in range(n):
        if j < i:
            if matrix[i][j] < mini:
                mini = matrix[i][j]
power = 1
print()
for i in range(n):
    power *= matrix[n-1][i]
print(mini)
print(power)

print("8 (1)")
matrix = createMatrix(3, 4)
for i in range(3):
    isZero = False
    for j in range(4):
            if not isZero: matrix[i][j] = randint(0, 1)
            else: matrix[i][j] = 0
            if matrix[i][j] == 1: isZero = True
    if not isZero:
        matrix[i][j] = 1
printMatrix(matrix)

print("8 (2)")
matrix = createMatrix(2,3)

print("8 (3)")
matrix = createMatrix(3, 3)
print(matrix[0])
print(matrix[2])

print("8 (4)")
matrix = createMatrix(5, 5)
for i in range(5):
    if i % 2 == 0:
        print(matrix[i])

print("8 (5)")
matrix = createMatrix(5,5)
matrix = list(zip(*matrix))
printMatrix(matrix)
for i in range(5):
    for j in range(5):
        if matrix[i][0] > matrix[i][4]:
            print(matrix[i][j], end=' ')
    print()

print("8 (6)")
matrix = createMatrix(5, 5)
printMatrix(matrix)
summa = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] % 2 != 0 and matrix[i][j] < 0:
            summa += abs(matrix[i][j])
print(summa)

print("8 (7)")
matrix = createMatrix(5, 5)
printMatrix(matrix)
k = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 7:
            k += 1
print(k)

print("8 (8)")
matrix = createMatrix(5, 5)
for i in range(5):
    for j in range(5):
        if i == j:
            print(matrix[i][j])

print("8 (9)")
matrix = createMatrix(5, 5)
print(matrix[4])
matrix = list(zip(*matrix))
print(matrix[4])

print("8 (10)")
matrix = createMatrix(5, 5)
def print_matrix_zigzag(matrix):
    for i in range(len(matrix)):
        if i % 2 == 0:
            row = matrix[i][::-1]
        else:
            row = matrix[i]
        for element in row:
            print(element, end=' ')
        print()
matrix = createMatrix(5, 5)
print_matrix_zigzag(matrix)

print("8 (11)")
def create_border_matrix(n, m):
    # Создаем матрицу из нулей
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                matrix[i][j] = 1

    return matrix
n, m = 5, 9  # n - количество строк, m - количество столбцов
matrix = create_border_matrix(n, m)
for row in matrix:
    print(row)

print("8 (12)")

def create_matrix(n):
    matrix = [[1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 3
            elif i < j:
                matrix[i][j] = 2
    return matrix

n = 5
matrix = create_matrix(n)
for row in matrix:
    print(row)
