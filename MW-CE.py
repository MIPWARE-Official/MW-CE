#Scripted by Isaac D (Therealmip)

#MW-CE script
print("Loading some things. . .")
import os
print("Loaded 'os'")
print("Loaded 'itertools'")
import subprocess
print("Loaded 'subprocess'")
print("Loaded 'threading'")
import time
print("Loaded 'time'")
import sys
print("Loaded 'sys'")
print("Loaded 'youtube_dl'")
import zipfile
print("Loaded 'zipfile'")
print("Loaded 'whois'")
import socket
print("Loaded 'socket'")
print("Loaded 'pytube'")
print("Loaded 'csv'")
print("Loaded 'random'")
print("Loaded 'requests, json'")

print("Loaded 'random'")
time.sleep(1)

#states text colors
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

rootcolor = (bcolors.BOLD)

#loads in some more stuff
print("Loaded all imports")
from os import system, name
from os import listdir
from datetime import datetime
from time import sleep
from tqdm import tqdm
import time
import socket
import shutil
import sys
import platform
import os
import socket
from itertools import product
from importlib import reload  # Python 3.4+

from zipfile import ZipFile, BadZipFile
import string
from random import *
taskkill1 = ("ok")

def easteregg321():
  print(f"{bcolors.ROOTRED}ERR0R 008: Process termination needed{bcolors.ENDC}")
  time.sleep(0.7)
  exit

from cryptography.fernet import Fernet
#Loads the enc key
#for enc-ing files and stuff
key="lbeiXBZ1gIVWtTAlbXCACKEIT7B3AppqxZib-35LmQo="


fernet=Fernet(key)

#Def's the "screen_clear" function to clear the screen
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
sleep(1.3)

#if there is any problems with text colors at first
#this should fix it
print("calibrating text colors. . .")
print(f"{bcolors.HEADER}calibrating. . .{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}Text colors calibration complete!{bcolors.ENDC}")

def exitthing3():
  screen_clear()
  exit

    
  

version = ("0.1 Beta PE")

screen_clear()

#defs the info screen
def infoofmwce():
      print("MIPWARE Command Executor (MW-CE)")
      print("Copyright 2022-2023")
      print(version)
      print(f"{bcolors.OKGREEN}MW-CE loaded!{bcolors.ENDC}")
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
      #defs the command line and commands
      def dosmainmenu():
        taskkill2 = ("ok")
        command = input(f"{bcolors.ROOTRED} (ROOT) {bcolors.ENDC} Command: ")
        #commands
        if command == ("help"):
          print()
          print("======================General commands=====================")
          print("help: opens an list of commands")
          print("clear: Clears the screen")
          print("exit: Exits the MW-CE")
          print("print: Prints text on the screen")
          print()
          print("list: Shows external files that can be runned")
          print("time: Shows the time")
          print("run: runs said file")
          print("tree: shows both reg directories and sub-directories and most files too")
          print("calib_text: Fixes text colors")
          print("pyver: Prints the version of python your running")
          print()
          print("================File encryption and decryption==============")
          print("enc: Encrypts a file in the same dir that this program is in")
          print("dec: Decrypts a file in the same dir that this program is in")
          print()
          print("================Hacking, exploiting and attacks=============")
          print("ddos: DDOS's the target ip and port (DISABLED DUE TO BUGS)")
          print("crackziplock: Crack zip file passwords using dictionary attack in Python using the built-in zipfile module")
          print("scanports: Scans host for open ports")
          print()
          print("=======================Miscellaneous========================")
          print("weather: Prints the weather for the inputed city/town")
          print("whatsnew: Prints what is new to said update/version (REMOVED FOR GOOD)")
          print("dev- help: Prints most dev commands")
          print("google: Opens Google via w3m (MUST HAVE w3m INSTALLED TO USE!)")
          print()
          print("=======================File handeling=======================")
          print("makenew: Makes a new file with inputed name")
          print("readfile: Reads said file")
          print("writefile: Writes said text into said file")
          print("rm: Removes said file")
          print("listdir: Lists all contents in the working dir")
          print("cl: Counts how many lines said file has")
          print()
          dosmainmenu()

        elif command == ("clear --help"):
          print()
          print("Clears the screen")
          print()
          dosmainmenu()


        #Prints a list of contents of the working dir
        elif command == ("listdir"):
          cmd = ['ls']

          proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          o, e = proc.communicate()
          print()
          print(o.decode('ascii'))
          print()
          dosmainmenu()
          


          
        #Main file handling system

        #make a file
        elif command == ("makenew"):
          print()
          print("What should the file name be?")
          print()
          filename1 = input("File name: ")
          open(filename1, "xt")
          print()
          print("File created successfully")
          print()
          dosmainmenu()
          
          
          
        #read a file
        elif command == ("readfile"):
          print()
          whatfile123423434 = input("File: ")
          f = open(whatfile123423434, "r")
          print()
          print(f.read())
          print()
          dosmainmenu()

        #write to said file
        elif command == ("writefile"):
          print()
          whatfile3456542343468 = input("File: ")
          print()
          textthing23435354 = input("Text: ")
          f = open(whatfile3456542343468, "w")
          f.write(textthing23435354)
          f.close()
          print()
          print("File writen")
          print()
          dosmainmenu()

        #remove said file
        elif command == ("rm"):
          print()
          whatfile9999432743 = input("File: ")
          print()
          print("removing file. . .")
          print()
          time.sleep(0.1)
          os.remove(whatfile9999432743)
          print()
          dosmainmenu()

        #file line counter
        elif command == ("cl"):
          print()
          whatfileGYGYUSGYGYUGYTGG = input("File: ")
          print()
          fhand = open(whatfileGYGYUSGYGYUGYTGG)
          count = 0
          for line in fhand:
            count = count + 1
          print('Line Count:', count)
          fhand.close()
          print()
          dosmainmenu()

        #Runs said file
        elif command == ("run"):
          print()
          runwhatile2 = input("File: ")
          exec(open(runwhatile2).read())
          dosmainmenu()
          
          
          



        elif command == ("yt- download"):
          print()
          url = input("Url: ")

          youtube = pytube.YouTube(url)
          video = youtube.streams.first()
          video.download('/video', 'phpinterview')
          dosmainmenu()
          




        
        elif command == ("calib_text"):
          print()
          print("calibrating text colors. . .")
          print()
          time.sleep(2)
          print(f"{bcolors.HEADER}calibrating. . .{bcolors.ENDC}")
          time.sleep(1)
          print(f"{bcolors.OKGREEN}calibrating. . .{bcolors.ENDC}")
          time.sleep(1)
          print(f"{bcolors.ROOTRED}calibrating. . .{bcolors.ENDC}")
          time.sleep(1)
          print(f"{bcolors.BOLD}calibrating. . .{bcolors.ENDC}")
          time.sleep(1)
          print(f"{bcolors.OKBLUE}calibrating. . .{bcolors.ENDC}")
          time.sleep(1)
          print()
          print(f"{bcolors.OKGREEN}Text colors calibration complete!{bcolors.ENDC}")
          time.sleep(2)
          print()
          dosmainmenu()

        #Dev commands

        #Taskkill MW-CE within the script
        elif command == ("dev- taskkill"):
          print()
          taskkill = ("false")
          print("Unloading/reloading main imports. . .")
          import importlib
          importlib.reload(os)
          importlib.reload(sys)
          importlib.reload(time)
          importlib.reload(subprocess)
          
          time.sleep(1.6)
          #error checker script not made yet. W.I.P
          time.sleep(1.2)

          taskkill = ("true")
          
          if taskkill == ("true"):
            sys.exit(print(f"{bcolors.OKGREEN}==Successful termination=={bcolors.ENDC}"))
          else:
            print(f"{bcolors.ROOTRED}==Termination failure=={bcolors.ENDC}")
            print()
            dosmainmenu()

        #Dev commands help ui
        elif command == ("dev- help"):
          print()
          print("=====================Developer commands=====================")
          print("dev- taskkill: Terminates MW-CE when ran")
          print("dev- help: Opens up a command list for developer commands")
          print("dev- fast-taskkill: trys to taskkill MW-CE without doing checks (BIGGER FAIL CHANCE)")
          print()
          dosmainmenu()

        elif command == ("dev- fast-taskkill"):
          sys.exit()
            
        #Must have w3m installed to use this command, if not. It will not work
        elif command == ("google"):
          os.system('w3m google.com')
          dosmainmenu()

        elif command == ("google --install -Ubu"):
          os.system('install-pkg w3m')
          dosmainmenu()

        elif command == ("google --install -Kal"):
          os.system('apt install w3m')
          dosmainmenu()

        elif command == ("google --install -Ter"):
          os.system('pkg install w3m')
          dosmainmenu()

        elif command == ("google --help"):
          print()
          print("google --help: Opens help menu")
          print("google --install -(ver): Installs w3m on said version")
          print("google: Opens Google via w3m")
          print()
          dosmainmenu()

        
        elif command == ("showrandom"):
          print()
          dosmainmenu()
        
        elif command == ("weather"):
          print()
          # API base URL
          BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

          CITY = input("City: ")

          API_KEY = "02a23212a66742cca8aa6709a100dea8"

          URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

          response = requests.get(URL)

          if response.status_code == 200:
            data = response.json()
            main = data['main']

            
            #getting weather
            temperature = main['temp']
            temp_feel_like = main['feels_like']
            humidity = main['humidity']
            pressure = main['pressure']

            #weather report
            weather_report = data['weather']
            #wind report
            wind_report = data['wind']

            #printing everything stated
            
            print()
            print(f"{CITY:-^35}")
            print(f"City ID: {data['id']}")   
            print(f"Temperature: {temperature}")
            print(f"Feel Like: {temp_feel_like}")    
            print(f"Humidity: {humidity}")
            print(f"Pressure: {pressure}")
            print(f"Weather Report: {weather_report[0]['description']}")
            print(f"Wind Speed: {wind_report['speed']}")
            print(f"Time Zone: {data['timezone']}")
            print()
            dosmainmenu()

          else:
            #print error message
            print()
            print(f"{bcolors.WARNING}ERR0R 005: Error in the HTTP request{bcolors.ENDC}")
            print()
            dosmainmenu()
          

      

        elif command == ("e-ziplockcrack"):
          print()
          zipfilething = input("Zipfile > ")
          print()
          print(f"{bcolors.ROOTRED}WARNING: This locked zip cracker is experimental and may crash MW-CE, are yousure you want to run this?{bcolors.ENDC}")
          yesthingbah = input("y? n?")

          if yesthingbah == ("n"):
            screen_clear()
            dosmainmenu()
          

          elif yesthingbah == ("y"):
            pass
          
          screen_clear()
          
          time.sleep(3)
          print()
          def find_pw():
            pw_length = 1
            while True:
              s = string.ascii_lowercase
              for x in product(s, repeat=pw_length):
                pwd = "".join(x)
                with ZipFile(zipfilething) as zf:
                  try:
                    zf.extractall(pwd=bytes(pwd, "UTF-8"))
                    print("Password is {}".format(pwd))
                    return
                  except RuntimeError as e:
                    pass
                  except BadZipFile as e:
                    pass
              pw_length += 1
          find_pw()
          time.sleep(1.2)
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

        
        elif command == ("pyver"):
          assert sys.version_info >= (2, 5)
          print()
          print(sys.version)
          print()
          dosmainmenu()

        elif command == ("??????"):
          print()
          print("Why is this command a thing??")
          print("What is the point of this command?")
          print("What is the point of MW-CE??!?")
          print()
          time.sleep(5)
          easteregg321()
          

        
        elif command == ("hard_exit"):
          screen_clear()
          #Trys to force-exit MW-CE
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
          exit
        
        elif command == ("ddos"):
          print()
          print(f"{bcolors.WARNING}ERR0R 006: Command was disabled due to bugs{bcolors.ENDC}")
          print()
          dosmainmenu()
          #anything in this fuction under this text does not fuction at this time
          print()
          print(f"{bcolors.ROOTRED}ERR0R 008: Process termination needed{bcolors.ENDC}")
          time.sleep(2)
          print()
          print("Termination is now in process. . .")
          sys.exit()
          
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
          #Runs the file decrtpter script
          os.chdir(r"bin")
          exec(open('File_decrypter.py').read())
          os.chdir("..")
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

        elif command == ("linuxver"):
          print()
          os.name
          print()
          platform.system()
          print()
          platform.release()
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

        elif command == ("runtime"):
          start_time = time.time()
          print()
          print("--- %s seconds ---" % (time.time() - start_time))
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

        elif command == ("easteregg1"):
          print("Android is better then IOS, change my mind")
          dosmainmenu()

        else:
          print()
          print(f"{bcolors.WARNING}ERR0R 001: Invalid command{bcolors.ENDC}")
          print()
          dosmainmenu()

      dosmainmenu()
taskkill3 = ("ok")
infoofmwce()
