import os
import sys

userdata = open("account", "w")
username = input("Enter username: ")
password = input("Enter password: ")
userdata.write("username=" + username + "\n")
userdata.write("password=" + password)
userdata.close()

install_instaloader = "python -m pip install instaloader"
install_pyfiglet = "python -m pip install pyfiglet"

print("\n" + install_instaloader)
os.system(install_instaloader)
print("\n" + install_pyfiglet)
os.system(install_pyfiglet)
os.system("mkdir output")

print("\n\nIf you like to change the username and the password that you entered, you can do it by editing \"account\" file!")
print("\nInstaPhantom is ready for use!")
