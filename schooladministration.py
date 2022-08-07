import csv

def write_into_csv(info_list):
with open('student_info.csv', 'a', newlinem') as csv file:

writer = csv.writer(csv_file)
if csv_tell() == 0:
writer.writerow( ["Name", "Age", "Contact Number", "E-Mail ID"])
writer.writerow(info_list)
if__name__ == '__main__':
condition = True
student_num = 1
while(condition):

student_info = input("Enter student information in the following format (Name Age Contact Number E-mail_ID): ")
student_info_list = student_info.split(' ')

print("Entered information: " + student_info)

student_info_list = student_info.split(' ')

print("Entered split up information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail ID: {}".format(student_info_list[0], student_info_list[1], student_info_lit[2], student_info_list[3]))
choice_check = input("Is the entered information correct? (yes/no): ")

if condition_check == "yes":
   write_into_csv(student_info_list)
   condition_check = input("Enter (yes/no) if you want to enter the information for another student: ")
   if condition_check == "yes"
   condition = True
   student_num = student_num + 1
   elif condition_check == "no":
   condition = False
   print("\nPlease re-enter the values:")
