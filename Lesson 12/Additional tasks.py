# # Реалізуйте функцію для сортування списку методом "сортування бульбашкою". Функція повинна приймати список чисел 
# # і повертати його відсортованим в порядку зростання.

# def bubble_sort(arr):
#     _ = 0
#     while _ < len(arr)-1:
#         i = 0
#         while i < len(arr)-1:
#             if arr[i] > arr[i+1]:
#                 min = arr[i+1]
#                 max = arr[i]
#                 arr[i] = min
#                 arr[i+1] = max
#                 i+=1
#             else: i+=1
#         _+=1
#     return arr


# print(bubble_sort([]))
# print(bubble_sort([5, 2, 9, 1, 5, 6]))

# # # Перевірка
# assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
# assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
# assert bubble_sort([3, 8, 1, 7, 2, 9, 6]) == [1, 2, 3, 6, 7, 8, 9]


# Реалізуйте функцію для виконання бінарного пошуку в відсортованому списку. 
# Функція повинна повертати індекс шуканого елемента або -1, якщо елемент не знайдено.

def binary_search(arr, target):
    index = 0
    while len(arr) >= 1:
        
        if target > arr[int(len(arr)/2-1)]:
            index =index + int(len(arr)/2)
            arr = arr[int(len(arr)/2)::]
           
        elif target < arr[int(len(arr)/2-1)]:
            arr = arr[:int(len(arr)/2-1):]
        elif target == arr[int(len(arr)/2-1)]:
            index =index + int(len(arr)/2-1)
            return index
        
    return -1
    
print(binary_search([11, 12, 22, 25, 34, 64, 90], 22))
   
# Перевірка
# assert binary_search([11, 12, 22, 25, 34, 64, 90], 22) == 2