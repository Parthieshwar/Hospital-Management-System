'''
lst = ["ID", "Department", "Doctor", "Patient Name", "Age", "Gender", "Address", "Mob. Number", "Room Number", "Patient Condition"]

lst = ["ID", "Department", "Doctor Name", "Mob. Number"]

lst = ["ID","Department", "Doctor", "Patient Name", "Age", "Gender"]

'''
from handling_csv_files import *
import pandas as pd
import csv


##
def user_print_data (file_name,header_col=[],id=0):
    id=int(id)
    
    if file_name == 'patients':
        file_name = file_name +".csv"
        data_frame = pd.read_csv(file_name)
        print(data_frame.to_string(index=False))
    
    else:
        file_name = file_name+".csv"
        data_frame = pd.read_csv(file_name,usecols=header_col)
        print(data_frame.to_string(index=False))




##
def user_display_patient(id):
	flag, index = check_csv_id(int(id), 'patients')
	if flag == 1:
		print("ID is existed,")
		with open("patients.csv") as file:
			data = list(csv.reader(file))
		#data[index+1][info]
		new_data = data[index+1]
		print(new_data)
		del data
	else:
		print("The ID is not existed !!")


def user_display_doctor_appointment(id):
    flag, index = check_csv_id(int(id), 'doctors')
    if flag == 1:
        print("Doctor's ID is existed,\n")
        with open("doctors.csv") as file: 
            data = list(csv.reader(file))
        #data[index+1][info]
        new_data = data[index+1] #Get the doctor Name
        # print(new_data[2])
        
        flag2, index2 = check_csv_specific_cell( str(new_data[2]), "appointments", ["Doctor"] )
        if flag2 == 1:
            print("Doctor " +str(new_data[2])+ "  appointment: \n")
            
            with open("appointments.csv") as file:
                data = list(csv.reader(file))
            #data[index2+1][info]
            new_data = data[index2+1]
            print(new_data)
        else :
            print("Doctor " +str(new_data[2])+" has No appointment")

    else:
        print("The Doctor's ID is not existed !!")




#################################################
def user_Manage_func ():
    while True:
        msg = '''\n1. View available departments
2. View available doctors
3. View all patients Residents in a hospital in details
4. Search for patient by ID
5. The user enter the doctor's ID to view an appointments
6. To exit User Mode\n'''
        print(msg)
        user_input = str(input("Enter your choice: "))
        if user_input == '1':
            #call: user_print_department
            user_print_data('doctors',['Department'],0)
        elif user_input == '2':
            #Print Doctors + Department
            user_print_data('doctors',['Department','Doctor Name'])
        elif user_input == '3':
            #Print Doctors + Department
            user_print_data('patients')
        elif user_input == '4':
            id = int(input("Enter Patient ID to view: "))
            user_display_patient(id)
        elif user_input == '5':
            id = int(input("Enter Doctor's ID: ")) 
            user_display_doctor_appointment(id)
        elif user_input == '6':
            break
        else:
            pass
