import run

class Course:
  def __init__(self, num):
    self.name = input(f"\t\t\t#{num} Course: ")
    self.id = input(f"\t\t\t- {self.name} course id: ")
    self.mark = run.rUpTo(int(input(f"\t\t\t- mark (base 10): ")))

class Student:
  def __init__(self, n):
    self.Courses = []
    self.infor = self._getInfor_(n)
    self._getCourseInfor_()

  def _getInfor_(self, n):
    self.name = input(f"\tStudent {n} name: ")
    self.id = input(f"\t\t{self.name}'s id: ")
    self.Dob = input(f"\t\t{self.name}'s dob YYYY/MM/DD: ")
    return {"Name": self.name, "ID": self.id, "Dob": self.Dob, "Courses": self.Courses}

  def _getCourseInfor_(self):
    self.nOfCourses = int(input("\t\tNumber of courses: "))
    for _ in range(self.nOfCourses):
      self.Courses.append(Course(_ + 1))

class Class():
  def __init__(self):
    self._n_ = int(input("Number of students in class: "))
    self.students = []

  def getStudentInfor(self):
    for _ in range(self._n_):
      self.students.append(Student(_ + 1))

  def rawStudentsInfor(self):
    print("In class: ")
    for _ in range(self._n_):
      i = self.students[_]
      print(f"\tStudent #{_ + 1}: {i.name}")
      print(f"\t\tID: {i.id}\n\t\tDob: {i.Dob}\n\t\tMarks: ")
      i = i.Courses
      for j in range(len(i)):
        print(f"\t\t\t- {i[j].name} {i[j].id}: {i[j].mark}/10")


# class: class.students = [studentObject1, ..., studentObjectn]
# studentObject: .infor = {"name": name, "ID": id, "Courses": list of courseObject}

classA = Class()
classA.getStudentInfor()
classA.rawStudentsInfor()