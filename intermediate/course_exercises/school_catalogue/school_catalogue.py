class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  def __repr__(self):
    return 'A {} school named {} with {} students'.format(self.level, self.name, self.numberOfStudents)
  def getName(self): return self.name
  def getLevel(self): return self.level
  def getNumberOfStudents(self): return self.numberOfStudents
  def setNumberOfStudents(self, number): self.numberOfStudents = number

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy
  def __repr__(self): 
    parentRepr = super().__repr__()
    return parentRepr + '\nThe pickup policy is {}'.format(self.pickupPolicy)
  def getPickupPolicy(self): return self.pickupPolicy

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  def __repr__(self): return "The {} school has the following sport teams: {}".format(self.name, self.sportsTeams)
  def getSportsTeams(self): return self.sportsTeams