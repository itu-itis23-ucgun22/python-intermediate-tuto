

list_a = [1, 2, 3, 4, 5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)
[-10, 2, 3, 4, 5]
[-10, 2, 3, 4, 5]


import copy
list_a = [1, 2, 3, 4, 5]
list_b = copy.copy(list_a)

# not affects the other list
list_b[0] = -10
print(list_a)
print(list_b)
[1, 2, 3, 4, 5]
[-10, 2, 3, 4, 5]

import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.copy(list_a)

list_a[0][0]= -10
print(list_a)
print(list_b)

list_b = list(list_a)
list_b = list_a[:]
list_b = list_a.copy()



list_c= copy.deepcopy(list_a)

# not affects the other
list_a[0][0]= -10
print(list_a)
print(list_c)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
                
# Only copies the reference
p1 = Person('Alex', 27)
p2 = p1
p2.age = 28
print(p1.age)
print(p2.age)

# shallow copy
import copy
p3 = Person('Alex', 27)
p4 = copy.copy(p1)
p4.age = 28
print(p3.age)
print(p4.age)
27
28
class Company:
    def __init__(self, boss, employee):
        self. boss = boss
        self.employee = employee

boss = Person('Jane', 55)
employee = Person('Joe', 28)
company = Company(boss, employee)

company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)

print()
# deep copy will not affect nested objects
boss = Person('Jane', 55)
employee = Person('Joe', 28)
company = Company(boss, employee)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)

