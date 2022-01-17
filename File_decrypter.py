from cryptography.fernet import Fernet
key="lbeiXBZ1gIVWtTAlbXCACKEIT7B3AppqxZib-35LmQo="


fernet=Fernet(key)

print()
print("What file do you want to decrypt?")
print()
decfile = input("> ")
print()
print("Now decrypting file. . .")
print()
with open(decfile,'rb') as enc_file:
  encrypted=enc_file.read()

decrypted=fernet.decrypt(encrypted)

with open(decfile,'wb') as dec_file:
  dec_file.write(decrypted)
