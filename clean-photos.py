import exifread
import os
from os import listdir
import argparse
import sys

parser = argparse.ArgumentParser(description = "This is a cleanup script.")
parser.add_argument('-v', '--verbose', help = "Verbose mode for this script", required =False)
args = parser.parse_args()


def createName(value):
    date = ""
    hour = ""
    [date, hour] = value.split(' ')

    date_values = date.split(':')
    date = date_values[0]+date_values[1]+date_values[2]
    hour_values = hour.split(':')
    hour = hour_values[0]+"_"+hour_values[1]+"_"+hour_values[2]

    newName = "WP_"+date+"_"+hour+".jpg"
    return newName

def renameFile(fileName, newName):
    os.rename(fileName, newName)
    print fileName+" successfully changed to "+newName+".jpg"

#This will check whether the image has the right resolution
def checkRes(width, length):
    if str(width) == "1456":
        if str(length) == "2592":
            return True
    elif str(width) =="2592":
        if str(length) == "1456":
            return True
    return False

def moveFile(fileName):
    try:
        path = "/Users/stefan.ilie/Pictures/Pictures/test/"
        newPath = path+"new/"+fileName
        path = path + fileName
        print path
        print newPath
        os.rename(path, newPath)
    except Exception, e:
        print "Error while moving file ", str(e)

    print "Successfully moved file %s!", fileName

if args.verbose:
    print "e verbose"
print "Current work path for this folder is: " + os.path.dirname(os.path.realpath(__file__))

os.chdir("/Users/stefan.ilie/Pictures/Pictures/test")
cwd = os.getcwd()
print "current work directory is: " + cwd

for f in listdir('.'):
    print f
    print "\n\n"
    pic = open(f, 'rb')

    tags = exifread.process_file(pic)

    if str(tags) != "":
        if 'EXIF DateTimeDigitized' in tags.keys():
            date = tags["EXIF DateTimeDigitized"]
            width = tags["EXIF ExifImageWidth"]
            length = tags["EXIF ExifImageLength"]
            if checkRes(width, length):
                print "Res ok"
                newName = createName(str(date))
                print newName
            renameFile(str(f), newName)
            moveFile(newName)
        else:
            print "Invalid file"
    else:
        print "No exifdata"

#Daca  checkImageWidth && checkImageLength
    #redenumeste fisier: WP_AAAALLZZ_HH_MM_SS
    #muta in fiserul de output
#else:
    #break

#EXIF DateTimeDigitized
#EXIF ExifImageWidth
#EXIF ExifImageLength
#Image Orientation, value Horizontal (normal)
