Community Health Clinic Patient Record System

1. Project Overview

The Community Health Clinic Patient Record System is a simple Python application developed for the Object-Oriented Programming 1 assignment. It demonstrates how object-oriented programming can be used to manage basic patient records in a healthcare setting.

The system allows a user to enter patient details, add multiple patient records, and display the records.

2. Project Objectives

- To apply classes and objects in Python.
- To store patient information using attributes.
- To use methods to add and display patient records.
- To demonstrate the use of a list and a class method.
- To explore Digital Public Goods (DPG) principles.

3. Technologies Used

- Python
- Visual Studio Code
- GitHub

4. Main Features

- Enter a patient ID, name, and age.
- Add multiple patient records during a program session.
- Display all patient records.
- Use a list to store patient objects.
- Demonstrate a class method using "@classmethod".

5. Classes Used

Patient

The "Patient" class represents an individual patient. It stores the patient's ID, name, and age and includes a method to display the patient's information.

PatientRecordSystem

The "PatientRecordSystem" class manages the clinic system. It stores patient objects in a list and provides methods to add and display records.

6. How to Run the Program

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open "Patient_Record_System.py".
4. Run the Python file.
5. Follow the terminal prompts to enter patient details.
6. Choose whether to add another patient.
7. View the displayed patient records.

7. Example Input and Output

Example input:

- Patient ID: 902832818
- Patient name: John
- Patient age: 27

Example output:

System: Community Health Clinic
Patient added successfully!

--- All Patient Records ---
Patient ID: P001
Name: John
Age: 25

The information above is fictional and is provided for demonstration purposes.

8. Digital Public Goods Principles

- Open source: The source code can be shared publicly under an appropriate open-source licence.
- Accessibility: Simple prompts make the program easier to use.
- Privacy: Only fictional information should be used for demonstrations. Further security protections are needed before using real patient data.
- Modularity and reusability: Separate classes organise the code and make it easier to maintain and adapt.

9. Limitations

The current version stores records temporarily in memory. Records are not saved permanently after the program ends. The system also does not yet include user authentication, access controls, or a database.

10. Future Improvements

- Save patient records permanently.
- Add a search feature for patient IDs.
- Allow patient records to be updated or deleted.
- Introduce authentication and stronger privacy protections.
- Connect the application to a database.

11. Author and Academic Purpose

This project was developed as part of an Object-Oriented Programming 1 individual assignment. It demonstrates basic Python OOP concepts in a healthcare scenario.