#1
set1 = {10, 20, 30, 40, 50}
set2 = list(set1)
for x in set1:
    if x == 10 or x == 20 or x == 30:
        set2.remove(x)
set3 = set(set2)
print(set3)


#2
list = {10, 20, 30, 40, 50}
another_list = {60, 70, 80, 20, 10}
list.intersection_update(another_list)
print(sum(list))

#3
list = {10, 20, 30, 40, 50}
another_list = {30, 40, 50, 60, 70}
list.intersection_update(another_list)
print(list)


#4
list = {10, 20, 30, 40, 50}
another_list = {30, 40, 50, 60, 70}
list.symmetric_difference_update(another_list)
print(list)
