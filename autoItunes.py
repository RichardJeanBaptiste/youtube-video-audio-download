import pafy
import os
import re

plurl = "https://www.youtube.com/playlist?list=PLPRWtKgY2MOtotXGiOBUjigHFNnDtgue3"
playlist = pafy.get_playlist(plurl)


for x in range(len(playlist) - 1):
    try:
        #print(playlist['items'][x]['pafy'].title)
        playlist['items'][x]['pafy'].getbestaudio().download(filepath="tmp")
        #cwd = os.getcwd()
    except OSError:
        print('no video formats found...try again')
    except IndexError:
        pass


urls = os.listdir("tmp")
os.chdir("/Users/Richard/Documents/Projects/mp3-api/tmp")

for x in urls:
    asd = os.path.splitext(x)
    songTitle = asd[0]
    extension = asd[1]

    regex = re.compile('[^a-zA-Z]')
    newName = regex.sub('', asd[0])

    newFilename = newName + asd[1]
    os.rename(x,newFilename)

    try:
        a = os.getcwd() + "/" + newFilename
        string = "ffmpeg -i {curr}  '{output}'.mp3"
        string = string.format(curr=a,output=songTitle)
        os.system(string)
    except Exception:
        pass
    
    
'''
os.chdir("/Users/Richard/Documents/Projects/mp3-api/tmp")
urlsb = os.listdir("tmp")

def changeTags(x):
    try:
       print(x)
       mp3 = MP3File(x)
       mp3.album = 'Love Me Dearly'
       mp3.artist = 'Ivory Wade'
       mp3.save()
    except:
        pass
    


for x in urlsb:
    changeTags(x)
'''
