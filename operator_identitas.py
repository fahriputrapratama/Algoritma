c = 8
d = 8
print(c is d)

list1 = [1,2,3]
list2 = [1,2,3]
print (list1 is list2)
# hasil false dikarenakan tipe data array list dictionary itu bersifat independen kecuali pemecahan

list3 = [1,2,3]
list4 = list3
list3.append(5)
print (list3)
print(list4)
print(list3 is list4)