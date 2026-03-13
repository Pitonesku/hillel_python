# Написати програму, яка переміщає всі нулі у кінець списку.
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!

#******************************
# # Version 1


lst = [0,1,3,0,5,0,98]
zero_lst = []
for i, el in enumerate(lst):
   if el == 0:
      zero_lst.insert(0, [i, el])
for i in zero_lst:
    lst.append(lst.pop(i[0]))
print(lst)

#********************************************


# Version 2
lst = [1,0,0,9,6,0]
i = 0
while i < lst.count(0):
    lst.append(lst.pop(lst.index(0,i)))
    i+=1
print(lst)