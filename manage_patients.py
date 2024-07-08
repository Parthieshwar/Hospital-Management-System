'''
lst = ["ID", "Department", "Doctor", "Patient Name", "Age", "Gender", "Address", "Mob. Number", "Room Number", "Patient Condition"]

lst = ["ID", "Department", "Doctor Name", "Mob. Number"]

lst = ["ID","Department", "Doctor", "Patient Name", "Age", "Gender"]

'''
from handling_csv_files import *
import pandas as pd
import csv



def admin_add_patient():
	temp_lst = ['id']
	temp_lst.append( str(input("Enter Department: ")))
	temp_lst.append( str(input("Enter Doctor Name: ")))
	temp_lst.append( str(input("Enter Patient Name: ")))
	temp_lst.append( str(input("Enter Patient Age: ")))
	temp_lst.append( str(input("Enter Patient Gender: ")))
	temp_lst.append( str(input("Enter Patient Address: ")))
	temp_lst.append( str(input("Enter Patient Mobile Number: ")))
	temp_lst.append( str(input("Enter Patient Room Number: ")))
	temp_lst.append( str(input("Enter Patient Condition: ")))
	
	temp_lst[0] = ( int(input("Enter Patient ID: ")))

	#Saving the new elements
	flag,index = check_csv_id(temp_lst[0], 'patients')
	# print("index " + str(index))
	if flag == 0:
		with open('patients.csv', 'a', newline='') as file:
			wr = csv.writer(file)
			wr.writerow(temp_lst)
	else:
		print("This ID is already existed, ")



# # 
def admin_delete_patient(id, def_para = 0):
	if (def_para != 0):
		delete_csv_row(id, 'patients')
	else:
		flag = delete_csv_row(id, 'patients')
		if flag == True:
			print("Patient's Info has been deleted")
		else:
			print("This ID is not existed")




# # 
def admin_edit_patient_info(id):
	flag, index = check_csv_id(int(id), 'patients')
	if flag == 1:
		print("ID is existed,")
		with open("patients.csv") as file:
			data = list(csv.reader(file))
		#data[index+1][info]
		new_data = data[index+1]
		print(new_data)
		del data
		cpy_temp_data = new_data.copy()
		while True:
			msg = "\n0. Edit ID\n1. Edit Department\n3. Edit Doctor Name\n4. Edit Patient Name\n5. Edit Patient Age\n6. Edit Patient gender\n7. Address\n8. Mobile Number\n9. Room Number\n10. Patient Condition"
			print(msg)
			msg = "'s' for save\n'e' for exit"
			print(msg)
			user_choice = str(input("Enter your choice: "))
			user_choice = user_choice.lower()
			if user_choice == '0':
				x = int(input("old info: " + str(new_data[0]) +" Enter new: "))
				flag, index = check_csv_id(x, 'patients')
				if (flag == 1):
					print("You can not assign this ID, because It's already taked !")
				else:
					new_data[0] = x
			elif user_choice == '1':
				x = int(input("old info: " + str(new_data[1]) +" Enter new: "))
				new_data[1] = x
			elif user_choice == '2':
				x = str(input("old info: " + str(new_data[2]) +" Enter new: "))
				new_data[2] = x
			elif user_choice == '3':
				x = str(input("old info: " + str(new_data[3]) +" Enter new: "))
				new_data[3] = x
			elif user_choice == '4':
				x = str(input("old info: " + str(new_data[4]) +" Enter new: "))
				new_data[4] = x
			elif user_choice == '5':
				x = str(input("old info: " + str(new_data[5]) +" Enter new: "))
				new_data[5] = x
			elif user_choice == '6':
				x = str(input("old info: " + str(new_data[6]) +" Enter new: "))
				new_data[6] = x
			elif user_choice == '7':
				x = str(input("old info: " + str(new_data[7]) +" Enter new: "))
				new_data[7] = x
			elif user_choice == '8':
				x = str(input("old info: " + str(new_data[8]) +" Enter new: "))
				new_data[8] = x
			elif user_choice == '9':
				x = str(input("old info: " + str(new_data[9]) +" Enter new: "))
				new_data[9] = x
			elif user_choice == '10':
				x = str(input("old info: " + str(new_data[10]) +" Enter new: "))
				new_data[10] = x
			elif user_choice == 's':
				#check if Admin didn't change nothing, 
				i, flg_data_not_same = 0, 0
				while i < len(new_data):
					if (str(new_data[i] != cpy_temp_data[i])):
						flg_data_not_same = 1
						break
					i += 1
				if (flg_data_not_same == 1):
					admin_delete_patient(id,1)
					with open('patients.csv', 'a', newline='') as file:
						wr = csv.writer(file)
						wr.writerow(new_data)
						print("Saving......")
				else:
					print("exit......")
			elif user_choice == 'e':
				break
			else: 
				pass
	else:
		print("The ID is not existed !!")




# #
def admin_display_patient(id):
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




######################################################
def admin_Manage_patients():
	while True:
		msg = "\n1. Add new patient\n2. Delete patient Info\n3. Edit patient Info\n4. Display patient Info\n5. return to previous screen\n"
		print(msg)
		user_choice = str(input("Enter your choice: "))
		# user_choice = user_choice.lower()
		if user_choice == '1':
			#call: admin_add_patient
			admin_add_patient()

		elif user_choice == '2':
			#call : admin_delete_patient(id)
			id = int(input("Enter Patient ID to delete: "))
			admin_delete_patient(id)

		elif user_choice == '3':
			#call : admin_edit_patient_info(id)
			id = int(input("Enter Patient ID to edit: "))
			admin_edit_patient_info(id)

		elif user_choice == '4':
			#call : admin_display_patient(id)
			id = int(input("Enter Patient ID to display: "))
			admin_display_patient(id)

		elif user_choice == '5':
			#break
			break 
		else:
			#do nothing
			pass	
	return None
