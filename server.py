class Patient( object ):
    def __init__( self, name, allergies, id = "", bedNr = "" ):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bedNr = bedNr

class Hospital( object ):
    def __init__( self, name, capacity, patients = [], idCount = 100, bedCount = 0 ):
        self.name = name
        self.capacity = capacity
        self.patients = patients
        self.idCount = idCount
        self.bedCount = bedCount

    def admit( self, newPatient ):
        print "Attempting to admit", newPatient.name, ", checking available capacity..."
        if len( self.patients ) < self.capacity:
            self.bedCount += 1
            self.idCount += 1
            newPatient.bedNr = self.bedCount
            newPatient.id = self.idCount
            self.patients.append( newPatient )
            print "New patient", newPatient.name, "has been admitted."
        else:
            print "Sorry, the hospital is full"

        print "There are currently", len( self.patients ), "patients in the hospital."
        return self

        # print self.patients
        # print self.patients[0].name
        # print self.patients[0].allergies
        # print self.patients[0].id
        # print self.patients[0].bedNr



patient1 = Patient( "Danny", "milk" )
patient2 = Patient( "Stan", "none" )
patient3 = Patient( "George", "dust" )
patient4 = Patient( "Nataly", "none" )


SaintLuke = Hospital( "Saint Luke", 3 )

SaintLuke.admit( patient1 )