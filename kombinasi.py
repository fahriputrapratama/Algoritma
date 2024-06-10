person = [
    {'nama' : 'fahri', 'age' : '19'},
    {'nama' : 'husen', 'age' : '19'},
    {'nama' : 'ihsan', 'age' : '19'},
    {'nama' : 'bintang', 'age' : '19'},
]
personnew = {'nama' : 'arkan', 'age' : '25'}
person.append(personnew)
print(person)

for i in person:
    print('-', i['nama'], i['age'])