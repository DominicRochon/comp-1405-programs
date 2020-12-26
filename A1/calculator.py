print ('\nGrade calculator \n-----------------------')
name = input ('Please enter your name: ')

assignment = float(input ( name + ', please enter your assignment grade: '))
tutorial = float(input ( name + ', please enter your tutorial grade: '))
studyGroup = float(input ( name + ', please enter your study group grade: '))
midTerms = float(input ( name + ', please enter your midterms grade: '))
finalExam = float(input ( name + ', please enter your final exam grade: '))

assignment *= 0.42
tutorial *= 0.08
studyGroup *= 0.05
midTerms *= 0.2
finalExam *= 0.25

scheme1 = 'pass'
scheme2 = 'pass'

#scheme 1 is the assignment + tutorial part of the course
if assignment + tutorial < 25:
    scheme1 = 'fail'

#scheme 2 is midterms + final exam
if midTerms + finalExam < 22.5:
    scheme2 = 'fail'

average = assignment + tutorial + studyGroup + midTerms + finalExam

if scheme1 == 'pass' and scheme2 == 'pass' and average >= 50:
    print ( name + ' passes with a final grade of ' + str(average))
elif scheme1 == 'fail' and scheme2 == 'pass':
    print ( name + ' fails with a final grade of ' + str((assignment + tutorial)*2))
elif scheme1 == 'pass' and scheme2 == 'fail':
    print ( name + ' fails with a final grade of ' + str((midTerms + finalExam)*(100/45)))
else:
    if (assignment + tutorial)*2 < (midTerms + finalExam)*(100/45):
        print ( name + ' fails with a final grade of ' + str((assignment + tutorial)*2))
    else:
        print ( name + ' fails with a final grade of ' + str((midTerms + finalExam)*(100/45)))