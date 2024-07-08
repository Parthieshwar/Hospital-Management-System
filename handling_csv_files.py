import csv
import pandas as pd



def create_system_files ():
	#Patinets file
	try:
		f = open('patients.csv')
		print("patients.csv file is exist")
	except:
		#ID:[dep_name,doctor_name,P_name,P_age,P_gender,P_add,P_number,room_num,P_cond]
		lst = ["ID", "Department", "Doctor", "Patient Name", "Age", "Gender", "Address", "Mob. Number", "Room Number", "Patient Condition"]
		with open('patients.csv','w', newline='') as file:
			x = csv.writer(file)
			x.writerow(lst)
		print("Creating patients.csv file done!!")
	else:
		pass

	#Doctors file	
	try:
		f = open('doctors.csv')
		print("doctors.csv file is exist")
	except:
		#ID:[dep_name,doc_name,doc_number]
		lst = ["ID", "Department", "Doctor Name", "Mob. Number","Attending Patients"]
		with open('doctors.csv','w', newline='') as file:
			x = csv.writer(file)
			x.writerow(lst)
		print("Creating doctors.csv file done!!")
	else:
		pass

	#Appointments file	
	try:
		f = open('appointments.csv')
		print("appointments.csv file is exist")
	except:
		#ID:[dep_name,doc_name,]
		lst = ["ID","Department", "Doctor", "Patient Name", "Age", "Gender"]
		with open('appointments.csv','w', newline='') as file:
			x = csv.writer(file)
			x.writerow(lst)
		print("Creating doctors.csv file done!!")
	else:
		pass



#################
def check_csv_id(ID, file_name):
	file_name = file_name+".csv"
	ID = int(ID)
	_id = pd.read_csv(file_name,usecols= ['ID']) #return the column as integer
	_id = list(_id['ID'])
	# print("_id" + str(_id))
	i, flag_id_existed = 0, 0
	while i < len(_id):
		if (ID == _id[i]):
			flag_id_existed = 1
			break
		i += 1

	return flag_id_existed,i





####################
def check_csv_specific_cell(name_to_search , file_name, header_col):
	file_name = file_name+".csv"
	_id = pd.read_csv(file_name,usecols= header_col) #return the column as integer
	# print(_id)
	_id = list(_id['Doctor'])
	# print("_id" + str(_id))
	i, flag_id_existed = 0, 0
	while i < len(_id):
		if (str(name_to_search) == str(_id[i])):
			flag_id_existed = 1
			break
		i += 1

	return flag_id_existed,i




#####################
def delete_csv_row(idx, file_name):
	flag, index = check_csv_id(idx, file_name)
	if (flag == 1):
		print("ID is existed !")

		file_name = file_name+".csv"
		#deleting the ROW
		#
		data = pd.read_csv(file_name, index_col="ID")
		data.drop([idx],axis=0,inplace=True)
		data.to_csv(file_name, index=True)
		#
		return True

	else:
		return False