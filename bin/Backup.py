#States working dir
dir = 'bin'

#Loads text colors

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ROOTRED = ' \u001b[31m'

#Trys to load NEEDED imports

try:
  import os
  import sys
  import shutil
  import time
  from time import sleep
except:
  print()
  print(f"{bcolors.ROOTRED}ERROR! Failed to load.{bcolors.ENDC}")
  sys.exit(f"{bcolors.FAIL}Program terminated.{bcolors.ENDC}")
print()
def cmdLoader():
  def commandLine():
    command = input("> ")
    if command == ("colorsfix"):
      print("calibrating text colors. . .")
      print(f"{bcolors.HEADER}calibrating. . .{bcolors.ENDC}")
      print(f"{bcolors.OKGREEN}Text colors calibration complete!{bcolors.ENDC}")
      commandLine()
    elif command == ("test"):
      print("Test done!")
      commandLine()

    elif command == ("exit"):
      exit()

    elif command == ('restore'):
      os.chdir('..')
      open('main.py', 'w').close()
      shutil.copyfile('Backup.txt','main.py')
      os.chdir('bin')
      commandLine()
      
    elif command == ("backup"):
      os.chdir('..')
      open('Backup.txt', 'w').close()
      shutil.copyfile('main.py','Backup.txt')
      os.chdir('bin')
      commandLine()

    elif command == ("MW-CE"):
      os.chdir("..")
      try:
        exec(open('MW-CE.py').read())
        exit()
      except:
        print("Error!")
        commandLine()

    elif command == ("help"):
      print()
      print("exit: Exits recover mode")
      print()
      print("MW-CE: Trys to re-enter MW-CE")
      print()
      print("backup: Backs up MW-CE's programming in 'Backup.txt'")
      print()
      print("restore: Restores the backup")
      print()
      print("colorsfix: Fixes the bcolors system")
      print()
      commandLine()
    
    else:
      print(f"{bcolors.WARNING}ERROR! Bad command name{bcolors.ENDC}")
      commandLine()
  commandLine()
cmdLoader()
