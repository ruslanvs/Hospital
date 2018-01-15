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

    def printPatientList( self ):
        print "List of all patients:"
        for i in self.patients:
            print i.name, "bed: ", i.bedNr, "id: ", i.id
        return self

    def discharge( self, patientName ):
        print "Discharging", patientName, "..."
        for i in range ( 0, len( self.patients) ):
            if self.patients[i].name == patientName:
                print "Patient discharged"
                self.patients.pop(i)
                self.bedCount -= 1
                self.printPatientList()
                return self
        print "Error:", patientName, "was not found in the list. Discharge failed."
        return self


patient1 = Patient( "Danny", "milk" )
patient2 = Patient( "Stan", "none" )
patient3 = Patient( "Nataly", "dust" )
patient4 = Patient( "George", "none" )

SaintLuke = Hospital( "Saint Luke", 3 )

SaintLuke.admit( patient1 )
SaintLuke.admit( patient2 )
SaintLuke.admit( patient3 )
SaintLuke.admit( patient4 )

SaintLuke.discharge( "Stan" )
SaintLuke.discharge( "Nataly" )