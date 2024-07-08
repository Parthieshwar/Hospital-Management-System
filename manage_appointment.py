'''
lst = ["ID", "Department", "Doctor", "Patient Name", "Age", "Gender", "Address", "Mob. Number", "Room Number", "Patient Condition"]

lst = ["ID", "Department", "Doctor Name", "Mob. Number"]

lst = ["ID","Department", "Doctor", "Patient Name", "Age", "Gender"]

'''
from handling_csv_files import *
from datetime import datetime, timedelta
import pandas as pd
import csv


def check_csv_id(id, filename):
    try:
        with open(f'{filename}.csv') as file:
            data = list(csv.reader(file))
            for index, row in enumerate(data[1:]):
                if int(row[0]) == id:
                    return True, index
    except FileNotFoundError:
        return False, None
    return False, None

def delete_csv_row(id, filename):
    try:
        with open(f'{filename}.csv', 'r') as file:
            data = list(csv.reader(file))
        for i, row in enumerate(data[1:]):
            if int(row[0]) == id:
                del data[i + 1]
                with open(f'{filename}.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                return True
    except FileNotFoundError:
        return False
    return False

def create_system_files():
    files = ['appointments.csv', 'patients.csv', 'doctors.csv']
    headers = {
        'appointments.csv': ['ID', 'Department', 'Doctor Name', 'Patient Name', 'Patient Age', 'Patient Gender', 'DateTime'],
        'patients.csv': ['ID', 'Name', 'Age', 'Gender', 'Address', 'Phone'],
        'doctors.csv': ['ID', 'Name', 'Department', 'Phone']
    }
    for file in files:
        try:
            with open(file, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers[file])
        except FileExistsError:
            pass
        
        
def admin_add_appointment():
	temp_lst = ['id']
	temp_lst.append( str(input("Enter Department: ")))
	temp_lst.append( str(input("Enter Doctor Name: ")))
	temp_lst.append( str(input("Enter Patient Name: ")))
	temp_lst.append( str(input("Enter Patient Age: ")))
	temp_lst.append( str(input("Enter Patient Gender: ")))
	
	temp_lst[0] = ( int(input("Enter Appointment ID: ")))

	#Saving the new elements
	flag,index = check_csv_id(temp_lst[0], 'appointments')
	# print("index " + str(index))
	if flag == 0:
		with open('appointments.csv', 'a', newline='') as file:
			wr = csv.writer(file)
			wr.writerow(temp_lst)
	else:
		print("This ID is already existed, ")
		with open("appointments.csv") as file:
			data = list(csv.reader(file))
		#data[index+1][info]
		new_data = data[index+1]
		print("ID's Info:\n"+ str(new_data))
		del data



def is_slot_available(date_time):
    with open("appointments.csv") as file:
        data = list(csv.reader(file))
        for row in data:
            if row[1] == date_time:
                return False
    return True

def admin_auto_book_appointment():
    date_input = input("Enter the date (YYYY-MM-DD): ")
    time_input = input("Enter the time (HH:MM): ")
    appointment_duration = timedelta(minutes=30)
    
    try:
        date_time = datetime.strptime(f"{date_input} {time_input}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format!")
        return
    
    while not is_slot_available(date_time.strftime("%Y-%m-%d %H:%M")):
        date_time += appointment_duration

    appointment_id = int(input("Enter Appointment ID: "))
    department = input("Enter Department: ")
    doctor_name = input("Enter Doctor Name: ")
    patient_name = input("Enter Patient Name: ")
    patient_age = input("Enter Patient Age: ")
    patient_gender = input("Enter Patient Gender: ")

    new_appointment = [appointment_id, date_time.strftime("%Y-%m-%d %H:%M"), department, doctor_name, patient_name, patient_age, patient_gender]

    with open('appointments.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_appointment)
    
    print(f"Appointment booked for {date_time.strftime('%Y-%m-%d %H:%M')}")




def admin_cancel_appointment(id, def_para=0):
    if def_para != 0:
        delete_csv_row(id, 'appointments')
    else:
        flag = delete_csv_row(id, 'appointments')
        if flag:
            print("Appointment's Info has been canceled")
        else:
            print("This ID does not exist")

def admin_edit_appointment(id):
    flag, index = check_csv_id(int(id), 'appointments')
    if flag:
        with open("appointments.csv") as file:
            data = list(csv.reader(file))
        new_data = data[index]
        print("Current Appointment Details:", new_data)
        while True:
            msg = "\n0. Edit ID\n1. Edit Department\n2. Edit Doctor Name\n3. Edit Patient Name\n4. Edit Patient Age\n5. Edit Patient Gender\n6. Edit Date and Time\n's' for save\n'e' for exit"
            print(msg)
            user_choice = input("Enter your choice: ").lower()
            if user_choice == '0':
                new_data[0] = int(input("Enter new ID: "))
            elif user_choice == '1':
                new_data[1] = input("Enter new Department: ")
            elif user_choice == '2':
                new_data[2] = input("Enter new Doctor Name: ")
            elif user_choice == '3':
                new_data[3] = input("Enter new Patient Name: ")
            elif user_choice == '4':
                new_data[4] = input("Enter new Patient Age: ")
            elif user_choice == '5':
                new_data[5] = input("Enter new Patient Gender: ")
            elif user_choice == '6':
                date_str = input("Enter Date (YYYY-MM-DD): ")
                time_str = input("Enter Time (HH:MM): ")
                datetime_str = f"{date_str} {time_str}"
                new_data[6] = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %H:%M')
            elif user_choice == 's':
                admin_cancel_appointment(id, 1)
                with open('appointments.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(new_data)
                print("Saving......")
                break
            elif user_choice == 'e':
                break
    else:
        print("The ID does not exist !!")

def admin_Manage_appointment():
    while True:
        msg = "\n1. Book\n2. Auto Book\n3. Edit\n4. Cancel\n5. return to previous screen\n"
        print(msg)
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            admin_add_appointment()
        elif user_choice == '2':
            admin_auto_book_appointment()
        elif user_choice == '3':
            id = int(input("Enter appointment ID to edit: "))
            admin_edit_appointment(id)
        elif user_choice == '4':
            id = int(input("Enter appointment ID to cancel: "))
            admin_cancel_appointment(id)
        elif user_choice == '5':
            break
        else:
            pass