# Python 3
import urllib.request

### -----------------------------------------------------------------
baseurl = 'https://memory.loc.gov'

#imagelinksfile
i = open("links.txt", "r")

images = []
for line in i:
    images.append(line.rstrip())


print ("Starting the downloads")
for i in range(0, len(images)):
    if (i % 100 == 0):
        print ("getting image for page# ", i)
    url = baseurl + images[i] 
    img = (images[i].split('/'))[-1]
    print (url)
    
    #download image at that url
    urllib.request.urlretrieve(url, img )






