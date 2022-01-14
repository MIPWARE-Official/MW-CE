print("Loading some things. . .")
import os
print("Loaded 'os'")
import itertools
print("Loaded 'itertools'")
import threading
print("Loaded 'threading'")
import time
print("Loaded 'time'")
import sys
print("Loaded 'sys'")
import csv
print("Loaded 'csv'")
import random
print("Loaded 'random'")
time.sleep(1)

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

print("Loaded all imports")
from os import system, name
from datetime import datetime
from time import sleep

#Def's the "screen_clear" function to clear the screen
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
sleep(1.3)

print("calibrating text colors. . .")
print(f"{bcolors.HEADER}calibrating. . .{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}Text colors calibration complete!{bcolors.ENDC}")

def exitmwce():
  screen_clear()
  exit

version = ("0.0.2 Alpha PE")

screen_clear()

def infoofmwce():
      print("MIPWARE Command Executor (MW-CE)")
      print("Copyright 2022-2023")
      print(version)
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      print()
      def dosmainmenu():
        command = input(f"{bcolors.ROOTRED}(./ROOT){bcolors.ENDC} Command: ") 
        #commands
        if command == ("help"):
          print()
          print("help: opens an list of commands")
          print("clear: Clears the screen")
          print("exit: Exits the MW-CE")
          print("print: Prints text on the screen")
          print("info: shows the bulid, version and info of MW-CE")
          print("list: Shows external files that can be runned")
          print("run (file name): runs the file that is listed in the command")
          print("tree: shows both reg directories and sub-directories and most files too")
          print()
          dosmainmenu()

        elif command == ("clear --help"):
          print()
          print("Clears the screen")
          print()
          dosmainmenu()

        elif command == ("exit --help"):
          print()
          print("Exits the MW-CE")
          print
          dosmainmenu()

        elif command == ("tree"):
          print()
          print(f"{bcolors.WARNING}ERR0R 002: Invalid command usage of 'tree'.{bcolors.ENDC}")
          print("Run 'tree --help' for help on the usage of 'tree'")
          print()
          dosmainmenu()

        elif command == ("tree --help"):
          print()
          print("tree -v: Shows a tree of MW-CE's virtual file system")
          print("tree -e: (Does not work atm) Shows both reg directories and sub-directories and most files too that is on a external drive")
          print()
          dosmainmenu()

        elif command == ("clear"):
          screen_clear()
          dosmainmenu()

        elif command == ("run"):
          print()
          print(f"{bcolors.WARNING}ERR0R 002: Invalid command usage of 'run'.{bcolors.ENDC}")
          print()
          dosmainmenu()

        elif command == ("tree -v"):
          print()
          print("Stuff-----")
          print("         |")
          print("         |")
          print()
          dosmainmenu()

        elif command == ("list"):
          print()
          print("========files========")
          print()
          print("Coming soon!")
          print()
          dosmainmenu()

        elif command == ("run spammer.exe"):
          print()
          print(f"{bcolors.ROOTRED}DANGER: This will spam text on your screen{bcolors.ENDC}")
          print(f"{bcolors.ROOTRED}Are you sure you want to run this program?{bcolors.ENDC}")
          print()
          commandwhat1 = input("y? n?: ")
          
          if commandwhat1 == ("y"):
            print("Running 'spammer.exe'...")
            def spammerwhat4():
              time.sleep(0.2)
              print("YOUR COMPUTER HAS AN VIRUS!")
              spammerwhat4()
            spammerwhat4()

          

          elif commandwhat1 == ("n"):
            print()
            print("Aborting")
            print()
            dosmainmenu()

          else:
            print("ERR0R 003: Invalid choice")
            dosmainmenu()


        elif command == ("exit"):
          screen_clear()

          print(f"{bcolors.HEADER}Are you sure that you want to exit MW-CE?{bcolors.ENDC}")
          exitinput1 = input("y? n?: ")

          if exitinput1 == ("y"):
            exit
            exit

          elif exitinput1 == ("n"):
            print("Aborting exit. . .")
            time.sleep(1.5)
            screen_clear()

          elif exitinput1 == ("Y"):
            exit
            exit

          elif exitinput1 == ("N"):
            print("Aborting exit. . .")
            time.sleep(1.2)
            screen_clear()
            dosmainmenu()

          else:
            print()
            print(f"{bcolors.WARNING}ERR0R 003: Invalid choice{bcolors.ENDC}")
            print()
            print("Aborting exit. . .")
            print()
            time.sleep(1.2)
            screen_clear()
            dosmainmenu()


        elif command == ("print"):
          GYTVTRCT = input("Enter text to print: ")
          print(GYTVTRCT)
          dosmainmenu()

        elif command == ("time"):
          now = datetime.now()
          current_time = now.strftime("%H:%M:%S")
          print("The current time is", current_time)
          dosmainmenu()
        
        #File reading system template
        elif command == (" run File name here"):
          exec(open('File name here').read())
          dosmainmenu()


        elif command == ("run software1"):
          exec(open('software1.py').read())
          dosmainmenu()


        elif command == ("info"):
          infoofmwce()
          dosmainmenu()

        elif command == ("easteregg1"):
          print("Android is better then IOS, change my mind")
          dosmainmenu()

        else:
          print()
          print(f"{bcolors.WARNING}ERR0R 001: Invalid command{bcolors.ENDC}")
          print()
          dosmainmenu()

      dosmainmenu()
infoofmwce()
