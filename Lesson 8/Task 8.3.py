# ДЗ 8.3. Унікальне число
# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та повертати його.
# Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.

lst=[10,1,2,3,4,3]

def find_unique_value(lst : list[int | float]) -> int | float:
    """
    Return unique value from the list

    """
    for _ in lst:
        if lst.count(_) == 1:
           return _

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1' 
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2' 
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3' 
print("ОК")
     


#Version #2 for ALL unique values
def find_all_unique_values(lst : list[int | float]) -> list[int | float]:
    """
    Return all unique values from the list

    """
    unique_values_list=[]

    for _ in lst:
        if lst.count(_) == 1:
          unique_values_list.append(_)
    return unique_values_list
     

print(find_all_unique_values(lst))