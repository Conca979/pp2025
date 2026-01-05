import numpy as np
import input as inputs, output
from domains import course, student
import os
import json
# student management system:
#       student = {} stdId -> student object
#       course = {} cId -> course object

class StudentManagementSystem:
  def __init__(self):
    # self.students = {'stdId': stdObject, 'stdId': stdObject, ...}
    self.students = {}
    # self.cources = {'cId': cObject, 'cId': cObject, ...}
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

class Data:
  def loadData(self, stdList, c):
    def _insertData_(data, stdList = stdList, c = c):
      for std in data['students']:
        stdList[std['stdId']] = student.Student(std['stdId'], std['stdName'], std['stdDob'])
      for cs in data['courses']:
        c[cs['cId']] = course.Course(cs['cId'], cs['cName'], cs['cCredit'], cs['marks'])

    if 'data.json' in os.listdir('./domains'):
      with open('./domains/data.json') as f:
        data = json.load(f)
        _insertData_(data)
    else:
      with open('./domains/data.json', mode = 'w') as f:
        f.write('''{"students": [], "courses": []}''')
  
  def saveData(self, stdList, c):
    data = {"students": [], "courses": []}
    for stdId in stdList:
      data["students"].append({"stdId": stdId, "stdName": stdList[stdId].stdName, "stdDob": stdList[stdId].stdDob})
    for cId in c:
      data["courses"].append({"cId": cId, "cName": c[cId].cName, "cCredit": c[cId].cCredit, "marks": c[cId].marks})
    #
    with open('./domains/data.json', mode = 'w') as f:
      f.write(json.dumps(data))


def runMenu():
  # initializing
  stdMgSystem = StudentManagementSystem()
  data = Data()
  data.loadData(stdMgSystem.students, stdMgSystem.courses)
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
    print("8. Save data")
    print("9. Exit")
    
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
    elif choice == '8':
      data.saveData(stdMgSystem.students, stdMgSystem.courses)
    elif choice == '9':
      choice = input("\t\tSave the data?\n\t1: yes\n\telse: no\n\t")
      if choice == '1':
        data.saveData(stdMgSystem.students, stdMgSystem.courses)
        return
      else:
        return
    else:
      print("---No avaiable option, pls try again---")

runMenu()