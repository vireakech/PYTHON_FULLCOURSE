'''
kinda file in python :
'r' read
'w' write
'a' append
'b' binary (rb'read binary',wb'qrite binary')
'''
lines=["My name is tek \n","Hi my name is jane\n","hi my name is \n"] # if we use this code it ez and fast
file_object = open(file="test.txt",mode='w')
#file_object.write("Hello my name is tek \n") # we can use like this and it hard and long time
#file_object.write("I'm 16 year old \n")
#file_object.write("I live in pmj village cvr commune pnp distic bmc province")
file_object.writelines(lines) 
