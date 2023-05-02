class Patient:
    def __init__(self, name, age, gender, condition, medications):
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.medications = medications

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, State: {self.state}, Medications: {self.medications}"
    
    def add_medication(self, medication):
        self.medications.append(medication)

    def  get_name(self):
        return self.name
    
    def remove_medication(self, medication):
        self.medications.remove(medication)
    
    def update_medication(self, old_medication, new_medication):
        index = self.medications.index(old_medication)
        self.medications[index] = new_medication
    
    