import numpy as np
import input as inputs, output
from domains import course, student
# student management system:
#       student = {} stdId -> student object
#       course = {} cId -> course object

class StudentManagementSystem:
  def __init__(self):
    self.students = {}
    self.courses = {}

  def ipStdInfor(self):
    inputs.ipStdInfor(self)

  def ipCourseInfor(self):
    inputs.ipCourseInfor(self)

  def ipMarks(self):
    inputs.ipMarks(self)

  def listStds(self):
    output.listStds(self)

  def listCourses(self):
    output.listCourses(self)

  def showStdMark(self):
    output.showStdMark(self)

  def ShowStdGpa(self):
    output.ShowStdGpa(self)

def runMenu():
  # initializing
  stdMgSystem = StudentManagementSystem()
  # add some sample information
  stdMgSystem.students["123"] = student.Student("123", "Duong", "28/05/05")
  stdMgSystem.students["124"] = student.Student("124", "Dung", "12/12/05")
  stdMgSystem.students["125"] = student.Student("125", "Thuy", "2/2/05")
  stdMgSystem.courses["Math001"] = course.Course("Math001", "Calculus", 3)
  stdMgSystem.courses["Bio001"] = course.Course("Bio001", "Genentic", 2)
  stdMgSystem.courses["Math001"].marks["123"] = 15
  stdMgSystem.courses["Math001"].marks["124"] = 12
  stdMgSystem.courses["Bio001"].marks["123"] = 16
  stdMgSystem.courses["Bio001"].marks["124"] = 20
  stdMgSystem.courses["Bio001"].marks["125"] = 9
  #
  while True:
    print("\n-----Student mark management-----")
    print("1. Input student")
    print("2. Input course")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show student marks")
    print("7. Show students GPA")
    
    choice = input("Select an option: ")
    print("\n")

    if choice == '1':
      stdMgSystem.ipStdInfor()
    elif choice == '2':
      stdMgSystem.ipCourseInfor()
    elif choice == '3':
      stdMgSystem.ipMarks()
    elif choice == '4':
      stdMgSystem.listStds()
    elif choice == '5':
      stdMgSystem.listCourses()
    elif choice == '6':
      stdMgSystem.showStdMark()
    elif choice == '7':
      stdMgSystem.ShowStdGpa()
    else:
      continue

runMenu()