from contextlib import nullcontext
from operator import index


x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    print(some_list)
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for num in range(0, 4): #len(some_list)
        print(some_list[num][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instuctors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print(str(len(some_dict['locations'])) + ' ' + 'LOCATIONS')
    for num in range(0, len(some_dict['locations'])):
        print(some_dict['locations'][int(num)])
    print(str(len(some_dict['instuctors'])) + ' ' + 'INSTUCTORS')
    for num in range(0, len(some_dict['instuctors'])):
        print(some_dict['instuctors'][int(num)])

printInfo(dojo)


