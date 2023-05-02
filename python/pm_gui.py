import tkinter as tk
from python.Patient import Patient
from ttkthemes import ThemedStyle
from python.mm_gui import mm_gui
class pm_gui:

    def __init__(self,
                  selected_patient=None):
        self.patients = []
        self.index = 0
        # Create the GUI window
        self.root = tk.Tk()
        self.style = ThemedStyle(self.root)
        self.style.set_theme("equilux")
        self.style.theme_use('equilux')
        self.selected_patient = selected_patient
        self.root.geometry("800x500")
        self.root.title("Patient Management")
        # Create the name label and entry box
        name_label = tk.Label(self.root, text="Name")
        name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.select_patient = selected_patient

        # Create the age label and entry box
        age_label = tk.Label(self.root, text="Age")
        age_label.pack()
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack()

        # Create the gender label and entry box
        gender_label = tk.Label(self.root, text="Gender")
        gender_label.pack()
        self.gender_entry = tk.Entry(self.root)
        self.gender_entry.pack()

        # Create the state label and entry box
        state_label = tk.Label(self.root, text="Conditions")
        state_label.pack()
        self.state_entry = tk.Entry(self.root)
        self.state_entry.pack()

        # Create the medication label and entry box
        med_label = tk.Label(self.root, text="Medications")
        med_label.pack()
        self.med_entry = tk.Entry(self.root)
        self.med_entry.pack()

        # Create the add patient button
        add_button = tk.Button(self.root, text="Add Patient", command=self.add_patient)
        add_button.pack()

        # Create the patient listbox
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill="both", expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.select_patient)
        self.listbox.bind("<Double-Button-1>", self.open_new_patient_gui)


        # Create the remove patient button
        remove_button = tk.Button(self.root, text="Remove Patient", command=self.remove_patient)
        remove_button.pack()


        if self.selected_patient:
            self.name_entry.insert(0, self.selected_patient.name)
            self.age_entry.insert(0, self.selected_patient.age)
            self.gender_entry.insert(0, self.selected_patient.gender)
            self.state_entry.insert(0, self.selected_patient.condition)
            for med in self.selected_patient.medications:
                self.listbox.insert("end", med)
            self.listbox.select_set(0)
        self.root.mainloop()


    def add_patient(self):
        # Add the patient to the listbox and the patient list
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        state = self.state_entry.get()
        medications = [self.med_entry.get()]
        patient = Patient(name, age, gender, state, medications)
        self.patients.append(patient)
        self.listbox.insert("end", patient.name)
        self.clear_entries()

    def get_selected_patient(self):
        # Get the selected patient from the listbox
        index = self.listbox.curselection()
        if index:
            # Return the patient object if one is selected
            return self.patients[index[0]]
        else:
            # Return None if no patient is selected
            return None
    
    def select_patient(self, event):
        # Set the selected patient to the patient at the selected index in the listbox
        selection = self.listbox.curselection()
        if selection:
            index = selection[0] 
            self.selected_patient = self.patients[index]
    
    def open_new_patient_gui(self, event):
        # Open a new instance of the PatientGUI clas
        new_patient_gui = mm_gui(self.get_selected_patient())

    def remove_patient(self):
        # Remove the selected patient from the listbox and the patient list
        if self.selected_patient:
            self.patients.remove(self.selected_patient)
            self.listbox.delete(self.listbox.curselection())
            self.selected_patient = None

    def clear_entries(self):
        # Clear all the entry boxes
        self.name_entry.delete(0, "end")
        self.age_entry.delete(0, "end")
        self.gender_entry.delete(0, "end")
        self.state_entry.delete(0, "end")
        self.med_entry.delete(0, "end")
    
        # Update the selected medication in the listbox and the medication list
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            old_medication = self.listbox.get(index)
            new_medication = self.update_entry.get()
            self.patient.update_medication(old_medication, new_medication)
            self.listbox.delete(index)
            self.listbox.insert(index, new_medication)
            self.update_entry.delete(0, "end")
