import random

print("██╗     ██╗   ██╗████████╗███████╗    ██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗")
print("██║     ██║   ██║╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║")
print("██║     ██║   ██║   ██║   ███████╗    ██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║")
print("██║     ██║   ██║   ██║   ╚════██║    ██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║")
print("███████╗╚██████╔╝   ██║   ███████║    ██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║")
print("╚══════╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝")                                                                                               
stuff = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789{[}]:;'.,/")
while 1:
  loopforinput = 1
  while loopforinput <= 1.5:
   try:
    pass_len = int(input("How long you want the pass / passes to be? : "))
    loopforinput += 1
   except ValueError:
     print("Please enter a numeric value.")

  multiplepassq = str(input("Do you need multiple passes? Y/N : "))
  if multiplepassq.lower() == "y":
    loopforinput2 = 1
    while loopforinput2 <= 1.5:
     try:
      howmanypass = int(input("How many passes? : "))
      loopforinput2 += 1
     except ValueError:
       print("Please enter a numeric value.")
    print("Ok!")
    for x in range(0, howmanypass):
     password2 = ""
     for x in range(0, pass_len):
      grabletter = random.choice(stuff)
      password2   = password2 + grabletter
     print("Password : ", password2)
  if multiplepassq.lower() == "n":
     print("Ok!")
     password = ""
     for x in range(0, pass_len):
      grabletter = random.choice(stuff)
      password  = password + grabletter
     print("Password : ", password)
