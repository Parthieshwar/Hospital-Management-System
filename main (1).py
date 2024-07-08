from Admin_functions import admin_check_pass
from manage_patients import admin_Manage_patients
from manage_doctors import admin_Manage_doctors
from manage_appointment import admin_Manage_appointment
from manage_user import user_Manage_func
from handling_csv_files import create_system_files
def main():
	create_system_files()
	while True:
		msg = "\nWelcome to Hosiptal Management System\n1. Enter Admin Mode\n2. Enter User Mode\nEnter 'Exit' to Turn Off the system\n"
		print(msg)
		user_in = str(input("Enter your choice: "))
		user_in = user_in.lower()
		if (user_in == '1'):
			incorrect_pass = admin_check_pass()
			print(incorrect_pass)
			while incorrect_pass == 0:
				msg = "\n1. To manage Patients\n2. To manage Doctors\n3. To manage appointments\n4. To exit Admin Mode\n"
				print(msg)
				user_input = str(input("Enter your choice: "))
				if (user_input == '1'):
					admin_Manage_patients()
				elif (user_input == '2'):
						admin_Manage_doctors()
				elif (user_input == '3'):
					admin_Manage_appointment()
				elif (user_input == '4'):
					break
				else: 
					pass
		elif (user_in == '2'):
			user_Manage_func()
		elif (user_in == 'exit'):
			break
		else:
			pass


if __name__ == '__main__':
  main()