# Функция бинарного поиска из книги "Грокаем алгоритмы" Адитья Бхаргава

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(list=my_list, item=3))
print(binary_search(list=my_list, item=-1))
print(binary_search(list=my_list, item=7))
print(binary_search(list=my_list, item=9))
