import secrets
import keyword 
import sys

print("██╗     ██╗   ██╗████████╗███████╗    ██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗")
print("██║     ██║   ██║╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║")
print("██║     ██║   ██║   ██║   ███████╗    ██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║")
print("██║     ██║   ██║   ██║   ╚════██║    ██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║")
print("███████╗╚██████╔╝   ██║   ███████║    ██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║")
print("╚══════╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝")                                                                                               
stuff = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789{[}]:;'.,/")
close_program = False
while 1:
  while 1:
   try:
    pass_len = int(input("How long you want the pass / passes to be? : "))
    break 
   except ValueError:
     print("Please enter a numeric value.")
   clde_program = input('Close program? Y/N ')
   if clde_program == 'y':
        print('CLOSING PROGRAM')
        sys.exit(0)
   else:
        print('Continuing.')
        continue

  multiplepassq = str(input("Do you need multiple passes? Y/N : "))
  if multiplepassq.lower() == "y":
    while 1:
     try:
      howmanypass = int(input("How many passes? : "))
      break
     except ValueError:
       print("Please enter a numeric value.")
    print("Ok!")
    for x in range(0, howmanypass):
     password2 = ""
     for x in range(0, pass_len):
      grabletter = secrets.choice(stuff)
      password2   = password2 + grabletter
     print("Password : ", password2)
  if multiplepassq.lower() == "n":
     print("Ok!")
     password = ""
     for x in range(0, pass_len):
      grabletter = secrets.choice(stuff)
      password  = password + grabletter
     print("Password : ", password)
