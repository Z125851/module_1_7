grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#set_ = {'Aaron' : [5, 3, 3, 5, 4], 'Bilbo' : [2, 2, 2, 3], 'Johnny' : [4, 5, 5, 2],
#        'Khendrik' : [4, 4, 3], 'Steve' : [5, 5, 5, 4, 5]}
# надо посчитать средний бал ля каждого
#print(len(grades[0]))
a = (sum(grades [0]) / len(grades[0]))
b = (sum(grades[1]) / len(grades[1]))
c = (sum(grades[2]) / len(grades[2]))
d = (sum(grades[3]) / len(grades[3]))
e = (sum(grades[4]) / len(grades[4]))
my_dict = {'Aaron' : a, 'Bilbo' : b, 'Johnny' : c, 'Khendrik' : d, 'Steve' : e}
my_list = list(students)
print(my_list)
print(my_dict.get('Aaron'))
print(my_dict)
