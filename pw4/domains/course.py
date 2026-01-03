class Course:
  def __init__(self, cId, cName, cCredit):
    self.cId = cId
    self.cName = cName
    self.cCredit = cCredit
    #
    # mark = {stdId1: mark, stdId2: mark}
    self.marks = {}