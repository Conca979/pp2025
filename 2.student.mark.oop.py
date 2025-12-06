#

class Courses:
  def __init__(self, name):
    self._n_ = int(input(f"\t\tNumber of courses {name} involved: "))
    self.course = {}
    for _ in range(self._n_):
      n = input(f"\t\t\t#{_ + 1} Course: ")
      self.course[n] = [
        input(f"\t\t\t- {n} course id: "),
        input(f"\t\t\t- mark: ")
      ]

class Student:
  def __init__(self, n):
    self.infor = self._getInfor_(n)
    self._getCourseInfor_()

  def _getInfor_(self, n):
    self.name = input(f"\tStudent {n} name: ")
    self.id = input(f"\t\t{self.name}'s id: ")
    self.Dob = input(f"\t\t{self.name}'s dob YYYY/MM/DD: ")
    return {"Name": self.name, "ID": self.id, "Dob": self.Dob, "Courses": None}

  def _getCourseInfor_(self):
    courses = Courses(list(self.infor.values())[0])
    self.infor["Courses"] = courses

class Class():
  def __init__(self):
    self._n_ = int(input("Number of students in class: "))
    self.students = []

  def getStudentInfor(self):
    for _ in range(self._n_):
      self.students.append(Student(_ + 1))

  def displayStudents(self):
    print("In class: ")
    for _ in range(self._n_):
      i = self.students[_].infor
      print(f"\tStudent #{_ + 1}: {i['Name']}")
      print(f"\t\tID: {i['ID']}\n\t\tDob: {i['Dob']}\n\t\tMarks: ")
      i = list(i["Courses"].course.items())
      for j in range(len(i)):
        print(f"\t\t\t- {i[j][0]} {i[j][1][0]}: {i[j][1][1]}/20")


# class: class.students = [studentObject1, ..., studentObjectn]
# studentObject: .infor = {"name": name, "ID": id, "Courses": list of object}
# courseObject: .course = {course1Name: [id, mark], ..., course2Name: [id, mark]]

classA = Class()
classA.getStudentInfor()
classA.displayStudents()