import numpy as np
import math

def listStds(self):
  print("-"*10)
  for std in self.students.values():
    print(f"\t{std.stdId}\t{std.stdName}\t{std.stdDob}")
  print("-"*10)

def listCourses(self):
  print("-"*10)
  for course in self.courses.values():
    print(f"\t{course.cId}\t{course.cName}\t{course.cCredit}")
  print("-"*10)

def showStdMark(self):
  cId = input("Enter course ID to view mark: ")
  if cId not in self.courses:
    print("No course found")
    return
  #
  print("-"*10)
  course = self.courses[cId].marks
  print("Stdudent id \t mark")
  for (stdId, stdMark) in course.items():
    print(f"{stdId}\t\t{stdMark}")
  print("-"*10)

def ShowStdGpa(self):
  stds = [[stdId] for stdId in self.students] # python 3.7 onward does guarantee the preservation of dict insertion
  i = 0
  for stdId in self.students:
    marks = []
    credits = []
    for course in self.courses.values(): # gathering marks of a specific student by id
      if stdId in course.marks:
        marks.append(course.marks[stdId])
        credits.append(course.cCredit)
    
    if len(marks) != 0:
      stds[i].append(math.floor(np.average(marks, weights = credits)*10)/10)
      i += 1
    else:
      stds[i].append(0)
      i += 1
  #
  stds.sort(key = lambda x : x[1], reverse = False)
  print("-"*10)
  print("Student ordered by their GPA\n", stds)
  for std in stds:
    print(f"\t{std[0]}\t{self.students[std[0]].stdName}\t{std[1]}")
  print("-"*10)