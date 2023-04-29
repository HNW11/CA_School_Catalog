#CREATE SCHOOL CLASS
class School:
  
  #Create constructor 
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  #Create getters for all 3 parameters
  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents

  #Create setter for number of students
  def set_numberOfStudents(self, newStudentCount):
    self.numberOfStudents = newStudentCount
  
  #Create repr method
  def __repr__(self):
    return "Welcome to {} a {} school with {} students. ".format(self.name, self.level, self.numberOfStudents)

#Test School Class
test = School("North Middle", "Middle", 865)
print(test)
print(test.get_name())
print(test.get_level())
test.set_numberOfStudents(976)
print(test.get_numberOfStudents()) #Works

#-----------------------------------------------
#CREATE PRIMARY SCHOOL CLASS

class PrimarySchool(School):

  #Create Constructor
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'Primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  #Create Getter for new parameter
  def get_pickupPolicy(self):
    return self.pickupPolicy 
  
  #Create repr
  def __repr__(self):
    schoolRepr = super().__repr__()
    return schoolRepr + " The pickup policy is {}".format(self.pickupPolicy)

#Test Primary School Class 
test2 = PrimarySchool('North Elementary', 332, 'Pickup Allowed')
print(test2.get_pickupPolicy())
print(test2)     #Works

#-----------------------------------------------

#CREATE HIGH SCHOOL CLASS

class HighSchool(School):

  #Create Constructor
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'High', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  #Create getter for sports teams
  def get_sportsTeams(self):
    return self.sportsTeams

  #Create repr
  def __repr__(self):
    schoolRepr = super().__repr__()
    return schoolRepr + f"The {self.name}" + f" sports teams inlcude: {', '.join(self.sportsTeams)}."

#Test High School Class
test3 = HighSchool('North High School', 798, ['Tennis', 'Basketball', 'Football', 'Soccer'])
print(test3.get_sportsTeams())
print(test3)     #Works