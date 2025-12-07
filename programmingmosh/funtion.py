import random as r
while True :
    guest = input("Enter number :")
    willrandom = r.randint(1,5)
    if guest == willrandom :
        print("Truv")
    else :
        print("Khos")
