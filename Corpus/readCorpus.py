# PYTHON 3
import os
import pickle
import re


##
path = '../Raw/Text/36th/'

## sort the files into filelist
filelist = os.listdir(path)
filelist = sorted(filelist)

# page breaks weeks: 0 - 9
pages = ["00250023", "00970095", "01830181",
        "02120210", "02650263", "03530351", 
        "04850483", "05870585", "07210719", 
        "09930991"]


pb = 0
texts = []
text = []
for i in range(0, len(filelist)):
    full = filelist[i]
    num = full.split('.')[0]
    with open(path + full, 'r') as myfile:
        text.append(myfile.read().replace('\n', '').replace('\r', ''))


    if (num == pages[pb]):
        texts.append(" ".join(text))
        pb = pb + 1
        text = []


for i in range(0, len(texts)):
    doc = re.split('\W+' , texts[i])
    ngram = ""
    sentences = []
    for j in range(0, len(doc)):
        ngram = ngram + " " + doc[j]
        if j % 5 == 0 and j > 0:
            sentences.append(ngram)
            ngram = ""

    with open("./weeks/" + str(i) + ".txt", "w") as f:
        f.writelines( "%s\n" % item for item in sentences)



