import os
import shutil

print("Please enter you command:")
print("HINT:\nCreate file - fcreate <FNAME>")
print("Delete file - fdelete <FNAME>")
print("Copy file - fcopy <FNAME> <FNAME>")
print("Move file - fmove <FNAME> <DESTINATION>")
print("Create directory - newdir <FNAME>")
print("Delete directory - deldir <FNAME>")
print("Copy directory - copydir <FNAME> <FNAME>")
print("Move directory - movedir <FNAME> <DESTINATION>")

str = input().split()
if str == []:
    print("Something wrong with command and arguments")
    exit(1)
try:
    str[1]
except:
    print("Something wrong with command and arguments")
if str[0] == "fcreate":
    fname = str[1]
    open(fname, 'a')
elif str[0] == "fdelete":
    A = os.listdir()
    if str[1] in A:
        os.remove(str[1])
        print(str[1])
    else:
        print("No such file")
elif str[0] == "newdir":
    A = os.listdir()
    try:
        os.mkdir(str[1])
    except:
        print("There is a directory with such name")
elif str[0] == "deldir":
    try:
        shutil.rmtree(str[1])
    except:
        print("There is no such directory")
elif str[0] == "fcopy":
    try:
        shutil.copy(str[1], str[2])
    except:
        print("Something went wrong")
elif str[0] == "fmove":
    try:
        shutil.move(str[1], str[2])
    except:
        print("Something went wrong")
elif str[0] == "copydir":
    try:
        shutil.copytree(str[1], str[2])
    except:
        print("Something went wrong")
elif str[0] == "movedir":
    try:
        if str[1] == str[2]:
            print("There is no need in moving")
        else:
            shutil.copytree(str[1], str[2])
            shutil.rmtree(str[1])
    except:
        print("Something went wrong")
else:
    print("Wrong command")
