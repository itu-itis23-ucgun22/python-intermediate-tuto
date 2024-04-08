#lists: ordered , mutable , allows duplicate elements
my_list = ["banana","cherry","apple"]
print(my_list)
my_list.sort()
print(my_list)
item1=my_list.reverse()
print(my_list)

my_list2=["a","b","c","d"]
item = sorted(my_list2)
item.reverse()
print(item)
new_list = [1] * 5
print(new_list) 

current_list=new_list+my_list2
print(current_list)

print(my_list2[0:1])
print(my_list2[::-1])
print(my_list2[::3])
list_org = ["banana","cherry","apple"]
list_cpy = list_org
list_org.append("melon")
list_cpy.append("berry") 
print(list_org)
print(list_cpy)
#aynı işlemler uygulanır

a_list = [1,23,3,4,56]
b_list = a_list.copy()
c_list=list(a_list)
#direkt kopyasını alır
d_list = a_list[:]
a_list.pop()
print(a_list,b_list,c_list,d_list)

square_list = [i*i for i in a_list]
print(square_list)