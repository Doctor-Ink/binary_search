# Функция бинарного поиска из книги "Грокаем алгоритмы" Адитья Бхаргава

def binary_search(list, item):    # В переменных low и high хранятся границы
    low = 0                       # той части списка, в которой выполняется поиск
    high = len(list) - 1
    while low <= high:              # <--- пока эта часть не сократится до одного элемента...
        mid = (low + high) // 2     # <--- проверяем средний элемент
        guess = list[mid]
        if guess == item:           # <--- значение найдено
            return mid
        if guess > item:            # <--- Много
            high = mid - 1
        else:                       # <--- Мало
            low = mid + 1
    return None                     # <--- Значение не существует

my_list = [1, 3, 5, 7, 9]
print(binary_search(list=my_list, item=3))
print(binary_search(list=my_list, item=-1))

