class Student():
  def __init__(self,name,id):
    self.name=name
    self.id=id
  def changeID(self,id):
    self.id=id
  def print1(self):
      print("{}-{}".format(self.name,self.id))
      
kot=Student("kot",11)
kot.print1()
kot.changeID(13)
kot.print1()
