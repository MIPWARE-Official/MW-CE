from cryptography.fernet import Fernet
key="lbeiXBZ1gIVWtTAlbXCACKEIT7B3AppqxZib-35LmQo="

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

fernet=Fernet(key)

print()
print("What file do you want to decrypt?")
print()
decfile = input("> ")

print()
print("Enter the key you will want to use")
print()
key=input("> ")
fernet=Fernet(key)
print()
print("Now decrypting file. . .")
print()
with open(decfile,'rb') as enc_file:
  encrypted=enc_file.read()

decrypted=fernet.decrypt(encrypted)

with open(decfile,'wb') as dec_file:
  dec_file.write(decrypted)

print(f"{bcolors.OKGREEN}File decrypted!{bcolors.ENDC}")
print()
