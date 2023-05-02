
import tkinter as tk
from ttkthemes import ThemedStyle
import ttkthemes as ttkth
from python.Patient import Patient
class mm_gui:

    def __init__(self, patient):
        # Create the GUI window
        self.root = tk.Tk()
        self.patient = patient
        self.style = ThemedStyle(self.root)
        self.style.set_theme("equilux")
        self.style.theme_use("equilux")
        self.name = self.patient.get_name()
        self.root.title("Medicatio Management for " + self.name)
        self.root.geometry("800x500")

        # Create the medication listbox

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill="both", expand=True)
        for med in self.patient.medications:
            self.listbox.insert("end", med)

        # Create the add medication button and entry box
        self.add_entry = tk.Entry(self.root)
        self.add_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Medication", command=self.add_medication)
        self.add_button.pack()

        # Create the remove medication button
        self.remove_button = tk.Button(self.root, text="Remove Selected Medication", command=self.remove_medication)
        self.remove_button.pack()

        # Create the update medication button and entry box
        self.update_entry = tk.Entry(self.root)
        self.update_entry.pack()
        self.update_button = tk.Button(self.root, text="Update Selected Medication", command=self.update_medication)
        self.update_button.pack()

        self.close_btn = tk.Button(self.root, text="Close", command=self.root.destroy)
        self.close_btn.pack()
        self.root.mainloop()
        # Create the go back btn
        

    def add_medication(self):
        # Add the medication to the listbox and the medication list
        medication = self.add_entry.get()
        self.patient.medications.append(medication)
        self.listbox.insert("end", medication)
        self.add_entry.delete(0, "end")

    def remove_medication(self):
        # Remove the selected medication from the listbox and the medication list
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.listbox.delete(index)
            del self.patient.medications[index]

    def update_medication(self):
        # Update the selected medication in the listbox and the medication list
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            medication = self.update_entry.get()
            self.patient.medications[index] = medication
            self.listbox.delete(index)
            self.listbox.insert(index, medication)
            self.update_entry.delete(0, "end")