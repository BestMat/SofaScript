import os
print("SofaScript.js - Simplified JavaScript with Terminal")
print("<<< - Run a file")
x = input("Enter the file name: ")
f = open(x,"r")
d = (f.read())
a = "node " + x
os.system('cmd /k' + a)
