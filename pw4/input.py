from domains.student import *
from domains.course import *
import math

def _ipNumberOfStds(self):
  while True:
    try:
      n = int(input("Number of student: "))
      if n < 0:
        raise ValueError
      else: return n
    except ValueError:
      print("-----Invalid input, pls try again-----")

def _ipNumberOfCourses(self):
  while True:
    try:
      n = int(input("Number of course: "))
      if n < 0:
        raise ValueError
      else: return n
    except ValueError:
      print("-----Invalid input, pls try again-----")

def ipStdInfor(self):
  for i in range(_ipNumberOfStds()):
    while True: # check for new id
      stdId = input(f"\tStudent {i + 1}'s id: ")
      if stdId not in self.students:
        break
      else:
        print(f"student with id '{stdId}' already existed")
    #
    stdName = input("\t\tName: ")
    # may have date parsing for validity
    stdDob = input("\t\tDob: ")
    #
    self.students[stdId] = Student(stdId, stdName, stdDob)

def ipCourseInfor(self):
  for i in range(_ipNumberOfCourses()):
    while True:
      cId = input(f"Course {i + 1}'s id: ")
      if cId not in self.courses:
        break
      else:
        print(f"Course id {cId} already existed!")
    #
    cName = input("\t\tName: ")
    # try catch cCredit
    while True:
      try:
        cCredit = int(input("\t\tCredit: "))
        if cCredit < 1:
          raise ValueError
        else: break
      except ValueError:
        print("-----Invalid input, pls try again-----")
    #
    self.courses[cId] = Course(cId, cName, cCredit)

def ipMarks(self):
  print("Updating mark:")
  #
  while True:
    cId = input("\tCourse's id: ")
    if cId in self.courses:
      break
    else:
      print(f"\tThere is no course {cId}, try again")
  #
  while True:
    stdId = input(f"\tStudent id: ")
    if stdId in self.students:
      break
    else:
      print(f"\tThere is no student id {stdId}, try again")
  #
  # may have mark parsing for validity
  while True:
    try:
      stdMark = int(input("\t\tmark (base 20): "))
      if stdMark < 0 or stdMark > 20:
        raise ValueError
      else:
        stdMark = math.floor(stdMark*10)/10
        break
    except ValueError:
      print("-----Invalid input, pls try again-----")
  self.courses[cId].marks[stdId] = stdMark