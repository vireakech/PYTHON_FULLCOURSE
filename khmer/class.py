class Displayable:
    def display(self):
        raise NotImplementedError("Subclasses must implement display()")

print("=============CAR FOR YOUTH==============")
class Moto(Displayable):
    def __init__(self, mode, model, year, owner, address, zip_code):
        self.mode, self.model, self.year = mode, model, year
        self.owner, self.address, self.zip_code = owner, address, zip_code
    def display(self):
        return f"MODE:{self.mode}\nMODEL:{self.model}\nYEAR:{self.year}\nOWNER:{self.owner}\nADDRESS:{self.address}\nZIP:{self.zip_code}"
print(Moto("Honda", "Today", "2016", "Tek", "PCC", "1001").display())

print("============MOTO FOR YOUTH==============")
class Car(Moto):
    def __init__(self, mode, model, year, owner, address):
        super().__init__(mode, model, year, owner, address, zip_code="N/A")
    def display(self):
        return f"{self.mode}\n{self.model}\n{self.year}\n{self.owner}\n{self.address}"
print(Car("NISSAN", "GTR", "2024", "Teknevercare", "PCC").display())

print("==============TIME=====================")
class Time(Displayable):
    def __init__(self, am, pm):
        self.am, self.pm = am, pm
    def display(self):
        t = input("Choose time (AM/PM): ")
        return self.am if t == "AM" else self.pm if t == "PM" else "Invalid time"
print(Time("1-3AM\n3-5AM", "7-9PM\n9-11PM").display())

print("==============LOCATION=================")
class Place(Displayable):
    def __init__(self, tk, tt, ss):
        self.places = {"tk": tk, "toultompung": tt, "sensok": ss}
    def display(self):
        p = input("Choose cinema (tk/toultompung/sensok): ")
        if p in self.places:
            return self.places[p] if input("Y/N: ") == "Y" else "Thank"
        return "NO VALID PLACE"
print(Place("DAYOFF", "DAYON", "DAYOFF").display())

print("=========Thanks for using us==========")
class Drink(Displayable):
    def __init__(self, cocacola, sting, bacus):
        self.stock = {"cocacola": cocacola, "sting": sting, "bacus": bacus}
    def display(self):
        d = input("Drink (cocacola/sting/bacus): ")
        return f"Quantity: {self.stock[d]}" if d in self.stock else "NO VALID DRINK"
print(Drink(1000, 500, 700).display())

class CinemaTK(Displayable):
    def __init__(self, *chairs):
        self.chairs = chairs
    def display(self):
        c = input("Choose seat (seat1-seat5): ")
        idx = {"seat1":0, "seat2":1, "seat3":2, "seat4":3, "seat5":4}.get(c)
        if idx is not None:
            return self.chairs[idx] if input("Y/N: ") == "Y" else "Thank"
        return "Seat limit 1-5"
cinema = CinemaTK("Success", "Already", "Success", "Already", "Success")
print(cinema.display())

print("============BANK IN CAMBODIA============")
class Company(Displayable):
    def __init__(self, aclida, lolc):
        self.banks = {"aclida": f"{aclida}$", "lolc": f"{lolc} rail"}
    def display(self):
        b = input("Choose bank (aclida/lolc): ")
        return self.banks.get(b, "Enter valid bank")
print(Company(200, 100).display())
