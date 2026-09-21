class Hospital:
    
    def __init__(self,name , doctor , staff):
        self.name = name 
        self.doctor = doctor
        self.staff = staff
        
    def welcome(self):
        print(f"Welcome to {self.name}")
        
        
        
class Patient(Hospital):
    def __init__(self, name, doctor, staff, disease , ward_number):
        super().__init__(name, doctor, staff)
        self.disease = disease
        self.ward_number = ward_number

class Operation(Hospital):
    def __init__(self, name, doctor, staff, disease , Op_time):
        super().__init__(name, doctor, staff)
        self.disease = disease
        self.Op_time = Op_time


patient = Patient("Private Hospital","Dr.Ahmad", "Night", "fever" , 540 )
op_patient = Operation("Private Hospital","Dr.Ahmad", "Night", "fever" , "5:40" )
print(patient.welcome())
print(patient.__dict__)
print(op_patient.__dict__)