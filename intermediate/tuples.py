import random
import sys
import timeit
#tuple: ordered, inmutable, allows duplicate elements
my_tuple = ("MOU",) # comma is necessarry for tuples even if it is strange. if comma haven't been, this statement will be str  
print(my_tuple)

my_tuple2 = tuple(["mou",20,"mersin"])
print(my_tuple2)
#there is index logic similar to lists
# loop logic is the same with lists

for x in my_tuple2:
    print(x)


my_tuple3 = ('a','p','p','l','e')
print(my_tuple3.count('e'))

#colon usage is same with lists
print(my_tuple3[2:3])

my_new_tuple = ("a","b","c")
princess , king , prince =my_new_tuple
print(king)
print(prince)
 

number_tuple = (1,2,3,4,5,6,7)
i1 , *i2, i3 = number_tuple
print(i1,i2,i3)


my_test_list =[1,2,3,4,"mou",True]
my_test_tuple = (1,2,3,4,"mou",True)

print(sys.getsizeof(my_test_list),"bytes")
print(sys.getsizeof(my_test_tuple),"bytes")

print(timeit.timeit(stmt="[0,1,2,3,4]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4)",number=1000000))

# working with tuples is more efficiency