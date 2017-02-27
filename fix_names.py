import os
from os import listdir

def renameFile(file_name, new_name):
    os.ename(fine_name, new_name)
    print "Changed "+file_name+" into "+new_name

def createName(file_name):
    arr = list(file_name)
    arr.insert(0, "S")
    arr.insert(4, "E")
    arr[4]="_"
    new_name="".join(arr)
    return new_nam

os.chdir("/home/pi/Media/TV-Series/Adventure Time Season 1 2 3 4 5 (720p) - TinyMP4/Season-2")
for f in listdir("."):
    new_name = createName(f)
    renameFile(f, new_name)

print "Process ended succesfully"
