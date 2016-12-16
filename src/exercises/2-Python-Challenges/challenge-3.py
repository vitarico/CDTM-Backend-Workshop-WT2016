class person():
    def __init__(self, name, age, studyObject):
        self.name=name
        self.age=age
        self.studyObject=studyObject

    def addAge(self):
        age +=1

Victoria = person("Victoria", 23, "EE")
print Victoria.name

class dualPerson(person):
    def __init__(self,name, age, studyObject="EE", secondStudy="CS"):
        person.__init__(self, name, age, studyObject)
        self.second=secondStudy

Hannes= dualPerson("Hannes", 45, studyObject="CS")

print Hannes.studyObject