class cinima_tk():
    def __init__(self,chair1,chair2,chair3,chair4,chair5,):
        self.chair1 = chair1
        self.chair2 = chair2
        self.chair3 = chair3
        self.chair4 = chair4
        self.chair5 = chair5
    def cinima_display(self):
        while True :
            input_chair = input("Please chosse the seat of seat1 seat2 seat3 seat4 seat5 :")
            if input_chair ==  "seat1":
                input_enter = input("Y/N :")
                if input_enter == "Y":
                    print(f"The seat is :{self.chair1}")
                else :
                    print("Thank")
                break
            elif input_chair ==  "seat2":
                input_enter = input("Y/N :")
                if input_enter == "Y":
                    print(f"The seat is :{self.chair2}")
                else :
                    print("Thank")
                break
            elif input_chair ==  "seat3":
                input_enter = input("Y/N :")
                if input_enter == "Y":
                    print(f"The seat is :{self.chair3}")
                else :
                    print("Thank")
                break
            elif input_chair ==  "seat4":
                input_enter = input("Y/N :")
                if input_enter == "Y":
                    print(f"The seat is :{self.chair4}")
                else :
                    print("Thank")
                break
            elif input_chair ==  "seat5":
                input_enter = input("Y/N :")
                if input_enter == "Y":
                    print(f"The seat is :{self.chair5}")
                else :
                    print("Thank")
                break
            else :
                return f"The limit of the seat is 1 - 5"
Cinima = cinima_tk("Sucessful","The seat is already","successful","The seat is already","successful")
print(Cinima.cinima_display())
print("============BANK IN THE CAMBODIA============")
class comapany:
    def __init__(self,aclida,lolc,):
        self.aclida = aclida
        self.lolc = lolc
    def main_bank(self):
        input_money = input("Choose the bank:" )
        if input_money == "aclida":
            return f"{self.aclida}$"
        elif input_money == "lolc":
            return f"{self.lolc}​ rail"
        else :
            return "Enter tha valid bank acc"
Comapany = comapany(float("200"),float("100"))
print(Comapany.main_bank())
print(Cinima.cinima_display())
list = []
rank = Comapany.main_bank()
rank2 = Cinima.cinima_display()
for i in rank,rank2():
    rank3 = list.append()
    print(rank3)