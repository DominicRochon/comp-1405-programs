import random
import copy

surnames = ['cat', 'dogggggo', 'owlie']
given = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', "I", 'J']

class Student:
    def __init__(self, surname, given_name, id, courses):
        self.surname = surname
        self.given_name = given_name
        self.id = id
        self.courses = courses
    def __repr__(self):
        return f'<{self.surname}, {self.given_name}: {self.id}>'
    def __str__(self):
        return f'<{self.surname}, {self.given_name}: {self.id}>'

def id_key(s):
    return s.id 

def surname_key(s):
    return s.surname

def namelen_key(s):
    return len(s.surname)

def insertion_sort(students):
    for index in range(1, len(students)):
        pos = index
        while pos >= 1 and students[pos - 1].id > students[pos].id:
            tmp = students[pos].id
            students[pos].id = students[pos - 1].id
            students[pos - 1].id = tmp
            pos -= 1

    return students

def selectionSort(students):
    num = 0
    smallestPos = 0
    for num in range (len(students)):
        smallest = 'zzzzzzz'
        for pos in range(num, len(students)):
            if students[pos].surname < smallest:
                smallest = students[pos].surname
                smallestPos = pos
        
        tmp = copy.deepcopy(students[num])
        students[num] = students[smallestPos]
        students[smallestPos] = tmp
        #print('during ', students)



# build a list of n students
n = 5
students = [Student(f'{surnames[i%len(surnames)]}', f'{given[i%len(given)]}', random.randint(0,1000), []) for i in range(n)]

print('before', students)
# students.sort(key=id_key)
students.sort(key= namelen_key)
#selectionSort(students)
print('after ', students)
