class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)


class PatientRecordSystem:
    def __init__(self, system_name):
        self.system_name = system_name
        self.patients = []

    def show_system_name(self):
        print("\nSystem:", self.system_name)
    @classmethod
    def system_description(cls):
        return "A simple system for managing patient records."

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully!")

    def display_all_patients(self):
        if not self.patients:
            print("No patient records found.")
            return

        print("\n--- All Patient Records ---")
        for patient in self.patients:
            patient.display_info()
            print("--------------------")


# Start the clinic system
clinic = PatientRecordSystem("Community Health Clinic")
clinic.show_system_name()

# Ask the user to enter patient details
while True:
    patient_id = input("\nEnter patient ID: ")
    name = input("Enter patient name: ")

    try:
        age = int(input("Enter patient age: "))
    except ValueError:
        print("Please enter age as a whole number.")
        continue

    patient = Patient(patient_id, name, age)
    clinic.add_patient(patient)

    another = input("Add another patient? (yes/no): ").lower()
    if another != "yes":
        break

# Display all saved records
clinic.display_all_patients()
print(PatientRecordSystem.system_description())