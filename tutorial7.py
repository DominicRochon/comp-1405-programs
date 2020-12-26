#Tutorial 7 :D
class Course:
    name = None
    term = None
    grade = None

class Student:
    name = None
    id = None
    courseGrade = Course

    def __init__(self, name, id, courseGrade.name, courseGrade.grade):
        self.name = name
        self.id = id
        self.courseGrade = courseGrade

    def __str__(self):
        return f'{self.name,self.id, self.courseGrade}'

    def computeAverage(student):
        totalMark = 0
        if len(student.courseGrade) > 0:
            for i in range(len(student.courseGrade)):
                totalMark += student.courseGrade[i].grade
            return totalMark/len(student.courseGrade)
        else:
            return -1

def findByID(students,inId):
        for i in range(len(students)):
            if students[i].id == inId:
                return students[i]
        return None

def findByCourse(students,inCourse):
    matches = []
    for i in range(len(students)):
        for k in range(len(students[i].courseGrade)):
            if students[i].courseGrade[k][0] == inCourse:
                matches.append(students[i])
    return matches

def studentsInGradeRange(students, low, high):
    inRange = []
    for i in range(len(students)):
        if high >= students[i].computeAverage() >= low:
            inRange.append(students[i].name)
    return inRange

def topTwo(students,n=1):
    for i in range(len(students)):
        if len(students[i]) >= n:
            computeAverage(students[i])

s1 = Student( 'cat', 123, ['comp1405', 78, 'comp1805', 72])
s2 = Student( 'dog', 323, [ ('comp1405', 88), ('phys1205', 82), ('math1105', 82) ] )
s3 = Student( 'bird', 121, [ ('comp1405', 22), ('comp1805', 41) ] )

s = [s1,s2,s3]

# print (s1.name, s1.id, s1.courseGrade)
#print (s1)
#print (s1.__str__())
print (s1.computeAverage())
# print (findByID(s, 121))
#print (findByCourse(s, 'math1105'))
#print (studentsInGradeRange(s,80,100))