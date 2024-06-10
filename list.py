person = ['dimas', 'izath', 'idris']

person.append('fahri')
print(person)

person.insert(1,'husen')
print(person)

person.remove('dimas')
print(person)

del person[2]
print(person)

person.pop()
print(person)

person1 = ['fahri','husen','ihsan','bintang','fahri']

print(person1[0])

print(person1.index('fahri'))
print(person1.count('fahri'))

person2 = ['fahri','husen','ihsan','bintang','fahri']
person2.reverse()
print(person2)
person2.sort()
print(person2)

print(len(person2))