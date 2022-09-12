import instaloader
from os import system
from pyfiglet import Figlet

def help():
	print("\n\n\n____________ Options Menu ____________\n")
	print("help:   Print this menu")
	print("login:   Logging into your account")
	print("target:   Setting the target user")
	print("profile:   Download the target profile picture and some usefull things")
	print("bio:   Print the bio of the target")
	print("followers:   Get all followers of the target")
	print("following:   Get all followees of the target")
	print("exit:   Exit script\n\n\n")

def login(loader):
	userdata = open("account", "r")
	username = userdata.readline().split("=")[1][0:-1]
	password = userdata.readline().split("=")[1][0::]
	userdata.close()
	
	try:
		user = loader.login(str(username), str(password))
		print("Logged in succesfully!\n")
		return user
	except instaloader.exceptions.BadCredentialsException:
		print("Error: Wrong password\n")
		return ""

def setTarget():
	target = input("Enter target's username: ")
	print("Target set succesfully! (" + target + ") \n")
	return target

def profile(loader, target):
	loader.download_profile(target, profile_pic_only=True)
	print("\n")
	system("mv " + target + " ./output/" + target)
	print("\n")

def showBio(loader, target):
	profile = instaloader.Profile.from_username(loader.context, target)
	print("\n\n")
	print(profile.biography)
	print("\n\n")

def followers(loader, target):
	profile = instaloader.Profile.from_username(loader.context, target)
	followers = open("./output/"+target+"_followers", "w")
	question = input("\nDo you want to display them? [Y/N]: ")
	
	while not(question == "y" or question == "Y" or question == "N" or question == "n"):
		print("Error: wrong answer")
		question = input("Do you want to display the followers? [Y/N]: ")
		
	if question == "Y" or question == "y":
		print("\n\n")
		for follower in profile.get_followers():
			followers.write(str(follower.username) + "\n")
			print(follower.username)
		print("\n\n")
	else:
		for follower in profile.get_followers():
			followers.write(str(follower.username) + "\n")
			
	followers.close()

def followees(loader, target):
	profile = instaloader.Profile.from_username(loader.context, target)
	followees = open("./output/"+target+"_followees", "w")
	question = input("Do you want to display them? [Y/N]: ")
	
	while not(question == "y" or question == "Y" or question == "N" or question == "n"):
		print("Error: wrong answer")
		question = input("Do you want to display the followees? [Y/N]: ")
		
	if question == "Y" or question == "y":
		print("\n\n")
		for followee in profile.get_followees():
			followees.write(str(followee.username) + "\n")
			print(followee.username)
		print("\n\n")
	else:
		for followee in profile.get_followees():
			followees.write(str(followee.username) + "\n")
			
	followees.close()




loader = instaloader.Instaloader()

#Just printing the first message
logo = Figlet(font="standard")
print("\n\n\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
print(logo.renderText("   InstaPhantom"))
print("//////////////////////////////////////////////////////////////////////////\n\n\n")


print("Enter \"help\" to show the options.\nAll files that will be downloaded, will be stored to the \"output\" directory\n\n")
#Run the program
commands = ["help", "login", "target", "profile", "bio", "followers", "followees"]
running = True
user = ""
target = ""

while running:
	command = input("Enter command: ")
	
	if command == commands[0]:
		help()
	elif command == commands[1]:
		user = login(loader)
	elif command == commands[2]:
		target = setTarget()
	elif command in commands and user != "" and target != "":
		if command == commands[3]:
			profile(loader, target)
		elif command == commands[4]:
			showBio(loader, target)
		elif command == commands[5]:
			followers(loader, target)
		elif command == commands[6]:
			followees(loader, target)
	elif user == "" and command in commands:
		print("Error: Please use the \"login\" command first!")
		
	elif command == "exit":
		running = False
	else:
		print("Error: This command does not exist!")
