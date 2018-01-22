# Python 3
from bs4 import BeautifulSoup #to parse/navigate the html
from  urllib.request import urlopen #to download html file

### -----------------------------------------------------------------
baseurl = 'https://memory.loc.gov/cgi-bin/ampage?collId=llcg&fileName=055/llcg055.db&recNum='

#outputfile
o = open("imagelinks.txt", "w")


image_links = []
print ("Starting the web scrape")
for i in range(2, 993):
    if (i % 50 == 0):
        print ("getting data for page# ", i)
    url = baseurl + str(i)
    source = urlopen(url).read()

    #make the html a BeautifulSoup object 
    soup = BeautifulSoup(source, 'html.parser') 

    #print all the urls on the page
    for link in soup.find_all("a"):
        if (".tif" in str(link) and "img" in str(link)):
            image_links.append(link['href'])
            print (link['href'])
print ("all information gathered")

print ("number of image links: ", len(image_links))
print ("printing all the links into outputfile: ")
for i in range (0,len(image_links)):
    print (image_links[i], file=o)





