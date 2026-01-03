# student management system:
#       student = {} stdId -> student object
#       course = {} cId -> course object

class Student:
  def __init__(self, stdId, stdName, stdDob):
    self.stdId = stdId
    self.stdName = stdName
    self.stdDob = stdDob

class Course:
  def __init__(self, cId, cName, cCredit):
    self.cId = cId
    self.cName = cName
    self.cCredit = cCredit
    #
    # mark = {stdId1: mark, stdId2: mark}
    self.marks = {}

class StudentManagementSystem:
  def __init__(self):
    self.students = {}
    self.courses = {}

  def __ipNumberOfStds(self):
    while True:
      try:
        n = int(input("Number of student: "))
        if n < 0:
          raise ValueError
        else: return n
      except ValueError:
        print("-----Invalid input, pls try again-----")

  def __ipNumberOfCourses(self):
    while True:
      try:
        n = int(input("Number of course: "))
        if n < 0:
          raise ValueError
        else: return n
      except ValueError:
        print("-----Invalid input, pls try again-----")

  def ipStdInfor(self):
    for i in range(self.__ipNumberOfStds()):
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
    for i in range(self.__ipNumberOfCourses()):
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

  def ipMarks(self): # only for inserting yet, no updating available
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
        if stdMark < 0:
          raise ValueError
        else: break
      except ValueError:
        print("-----Invalid input, pls try again-----")
    self.courses[cId].marks = {stdId: stdMark}

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

def runMenu():
  # initializing
  stdMgSystem = StudentManagementSystem()
  #
  while True:
    print("\n-----Student mark management-----")
    print("1. Input student")
    print("2. Input course")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show student marks")
    print("7. Exit")
    
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
    else: # choice == 7
      return

runMenu()