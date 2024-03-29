# Функция бинарного поиска из книги "Грокаем алгоритмы" Адитья Бхаргава

def binary_search(list, item):    # В переменных low и high хранятся границы
    low = 0                       # той части списка, в которой выполняется поиск
    high = len(list) - 1
    while low <= high:              # <--- пока эта часть не сократится до одного элемента...
        mid = (low + high) // 2     # <--- check middle element
        guess = list[mid]
        if guess == item:           # <--- value is defined
            return mid
        if guess > item:            # <--- much
            high = mid - 1
        else:                       # <--- not much
            low = mid + 1
    return None                     # <--- Value is not defined

my_list = [1, 3, 5, 7, 9]           # <--- Lets testing!

print(binary_search(list=my_list, item=3))    # нумерация элементов начинается с 0.
                                              # второй ячейке соответсвует индекс 1
print(binary_search(list=my_list, item=-1))   # "None" в Python означает "ничто".
                                              # это признак того, что элемент не найден

