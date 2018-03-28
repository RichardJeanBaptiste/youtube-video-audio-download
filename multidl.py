import pafy

def multidl(x):
    url = x
    video = pafy.new(url)
    best = video.getbest()
    bestaudio = video.getbestaudio()
    bestaudio.download()
   #best.download(quiet = False) video download

files = [] # add any amount of youtube links make sure to put each in quotation marks 

for urls in files:
    multidl(urls)

