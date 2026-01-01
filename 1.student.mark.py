# students: a list of dictionaries,
#         each dictionary represents one student {'id': ..., 'name':...., 'dob':....}
students = []
students = [{'id': '123', 'name': 'Duong', 'dob': '28/05/05'},{'id': '124', 'name': 'Dung', 'dob': '12/12/04'}]

# course: a list of dictionaries:
#         each dict is one course {'id':...., 'name':...., 'credit':....}
courses = []
courses = [{'id': 'ICT001', 'name': 'informatics', 'credit': 3}, {'id': 'math001', 'name': 'calculus I', 'credit': 4}]

# marks: a dict where keys are courseId
#        and value is another dict mapping student id to their marks
#        marks = {'courseId': {'std1Id': ..., 'std2Id': ...., ...}, ....}
marks = {'ICT001': {'123': 10, '124': 15}, 'math001': {'123': 20}}

# input functions
def ipNumberOfStds():
  return int(input("Number of student: "))

def ipStdInfor():
  existingStdId = [std['id'] for std in students]
  for i in range(ipNumberOfStds()):
    while True: # check for new id
      stdId = input(f"\tStudent {i + 1}'s id: ")
      if stdId not in existingStdId:
        break
      else:
        print(f"student with id '{stdId}' already existed")
    #
    stdName = input("\t\tName: ")
    # may have date parsing for validity
    stdDob = input("\t\tDob: ")
    #
    existingStdId.append(stdId)
    students.append({'id': stdId, 'name': stdName, 'dob': stdDob})

def ipNumberOfCourses():
  return int(input("Number of course: "))

def ipCourseInfor():
  existingCourses = [c['id'] for c in courses]
  for i in range(ipNumberOfCourses()):
    while True:
      cId = input(f"Course {i + 1}'s id: ")
      if cId not in existingCourses:
        break
      else:
        print(f"Course id {cId} already existed!")
    #
    cName = input("\t\tName: ")
    # try catch cCredit
    cCredit = int(input("\t\tCredit: "))
    #
    existingCourses.append(cId)
    courses.append({'id': cId, 'name': cName, 'credit': cCredit})

def ipMarks():
  existingCourses = [c['id'] for c in courses]
  print("Updating mark:")
  #
  while True:
    cId = input("\tCourse's id: ")
    if cId in existingCourses:
      break
    else:
      print(f"\tThere is no course {cId}, try again")
  #
  existingStdId = [std['id'] for std in students]
  while True:
    stdId = input(f"\tStudent id: ")
    if stdId in existingStdId:
      break
    else:
      print(f"\tThere is no student id {stdId}, try again")
  #
  # may have mark parsing for validity
  stdMark = int(input("\t\tmark (base 20): "))
  marks[cId][stdId] = stdMark

def listStds():
  print("-"*10)
  for std in students:
    print(f"\t{std['id']}\t{std['name']}\t{std['dob']}")
  print("-"*10)

def listCourses():
  print("-"*10)
  for course in courses:
    print(f"\t{course['id']}\t{course['name']}\t{course['credit']}")
  print("-"*10)

def showStdMark():
  cId = input("Enter course ID to view mark: ")
  if cId not in marks:
    print("No course found")
    return
  #
  print("-"*10)
  course = marks[cId]
  print("Stdudent id \t mark")
  for (stdId, stdMark) in course.items():
    print(f"{stdId}\t{stdMark}")
  print("-"*10)

def runMenu():
  while True:
    print("\n-----Student mark management-----")
    print("1. Input student")
    print("2. Input course")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show student marks")
    
    choice = input("Select an option: ")
    print("\n")

    if choice == '1':
      ipStdInfor()
    elif choice == '2':
      ipCourseInfor()
    elif choice == '3':
      ipMarks()
    elif choice == '4':
      listStds()
    elif choice == '5':
      listCourses()
    else: # choice == 6
      showStdMark()

runMenu()