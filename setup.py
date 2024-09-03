import os
import sys

install_instaloader = "python -m pip install instaloader"
install_pyfiglet = "python -m pip install pyfiglet"

print("\n" + install_instaloader)
os.system(install_instaloader)
print("\n" + install_pyfiglet)
os.system(install_pyfiglet)
os.system("mkdir output")

input("\nInstaPhantom is ready for use! Press \"Enter\" to continue...")
