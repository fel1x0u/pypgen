import random
print("██╗     ██╗   ██╗████████╗███████╗    ██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗")
print("██║     ██║   ██║╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║")
print("██║     ██║   ██║   ██║   ███████╗    ██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║")
print("██║     ██║   ██║   ██║   ╚════██║    ██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║")
print("███████╗╚██████╔╝   ██║   ███████║    ██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║")
print("╚══════╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝")                                                                                               
stuff = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789{[}]:;'.,/")
while 1:
  morect = 1
  while morect <= 1.5:
   try:
    morectf = int(input("How long you want the pass / passes to be? : "))
    morect += 1
   except ValueError:
     print("Please enter a numeric value.")

  fat = str(input("Do you need multiple passes? Y/N : "))
  if fat.lower() == "y":
    stuffnshit = 1
    while stuffnshit <= 1.5:
     try:
      big = int(input("How many passes? : "))
      stuffnshit += 1
     except ValueError:
       print("Please enter a numeric value.")
    print("Ok!")
    for x in range(0, big):
     balled = ""
     for x in range(0, fag):
      stuffed = random.choice(shit)
      balled   = balled + stuffed
     print("Password : ", balled)
  if fat.lower() == "n":
     print("Ok!")
     ball = ""
     for x in range(0, morectf):
      stuffed = random.choice(stuff)
      ball   = ball + stuffed
     print("Password : ", ball)
