'''
2/19/16 - Sean Lyngen

Python script for gathering username and passwords for access to devices.
Password and Enable passwords are asked for twice and compared against
each other as a method of confirmation


'''
#Enable the getpass module
import getpass

#Get userID
user = raw_input('Enter Username: ')
#Get Password
password1 = getpass.getpass('Enter Password: ')
#Get Password again for verification
password2 = getpass.getpass('Re-Enter Password: ')
#Compare passwords to ensure they match before continuing
while password1 != password2:
    password1 = getpass.getpass('Passwords Do not match, Enter Password: ')
    password2 = getpass.getpass('Re-Enter Password: ')
#Get Enable Password
enablepassword1 = getpass.getpass('Enter ENABLE Password: ')
#Get Enable Password again
enablepassword2 = getpass.getpass('Re-Enter ENABLE Password: ')
#Compare Enable passwords to ensure they match before continuing
while enablepassword1 != enablepassword2:
    enablepassword1 = getpass.getpass('Enter ENABLE Password: ')
    enablepassword2 = getpass.getpass('Re-Enter ENABLE Password: ')
