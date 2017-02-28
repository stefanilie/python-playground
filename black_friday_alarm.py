import urllib2
import time
import vlc
import BeautifulSoup

html = ""
myTitle = ""
prev = ""

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()


def getData():
    response = urllib2.urlopen('http://www.emag.ro')
    html = response.read()
    soup = BeautifulSoup.BeautifulSoup(html)
    myTitle = soup.html.head.title
    prev = myTitle

getData()
p=vlc.MediaPlayer('alarm.mp3')

while True:
    if prev == myTitle:
        print "And another one"
        time.sleep(3)
        getData()
    elif "Black Friday 2016" in myTitle:
        print "Habemus blec friday"
        break
        p.play()

f=open('emag1.html', 'w')
deleteContent(f)
f.write(prev)

g=open('emag2.html', 'w')
deleteContent(g)
g.write(html)
