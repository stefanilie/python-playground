import exifread
import os
from os import listdir
import argparse

parser = argparse.ArgumentParser(description = "This is a cleanup script.")
parser.add_argument('-v', '--verbose', help = "Verbose mode for this script", required =False)
args = parser.parse_args()


if args.verbose:
    print "e verbose"
print "Current work path for this folder is: " + os.path.dirname(os.path.realpath(__file__))

os.chdir("/Users/stefan.ilie/Pictures/Pictures")
cwd = os.getcwd()
print "current work directory is: " + cwd

ok = 0
for f in listdir('.'):
    if ok <4:
        pic = open(f, 'rb')

        tags = exifread.process_file(pic)

        if str(tags) != "":
            ok += 1
            for tag in tags.keys():
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                            print "Key: %s, value %s" % (tag, tags[tag])
