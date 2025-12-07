python_dic = {
    "name"   : "TEK",
    "age"    : "19",
    "email:" : "kechzenzer@gmail.com"
}
python_dic["name"] = "nhoa keavireakech" #change the items in the dict
print(python_dic["name"] + " " + python_dic["age"] + " " + python_dic["email:"] )
phone = input("Phone :")
numbers = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
}
ouput = ""
for i in phone:
    ouput += numbers.get(i,"!") + " "
print(ouput)
