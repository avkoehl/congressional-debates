# PYTHON 2
import os
from nltk import word_tokenize
import math
import pickle


##
path = './texts/36th/'

## sort the files into filelist
filelist = os.listdir(path)
filelist = sorted(filelist)

# page breaks weeks: 0 - 9
pages = ["00250023", "00970095", "01830181",
        "02120210", "02650263", "03530351", 
        "04850483", "05870585", "07210719", 
        "09930991"]

# Coresponding Dates for weeks 0 - 9
dates = ["Dec 03 - Dec 09", "Dec 10 - Dec 16", "Dec 17 - Dec 23", 
        "Dec 24 - Dec 30", "Dec 31 - Jan 06", "Jan 07 - Jan 13", 
        "Jan 14 - Jan 20", "Jan 21 - Jan 27", "Jan 28 - Feb 03", 
        "Feb 10 - Feb 17"]

files = []


pb = 0
fnames = []
texts = []
text = []

for i in range(0, len(filelist)):

    full = filelist[i]
    num = full.split('.')[0]
    fnames.append(full)



    with open(path + full, 'r') as myfile:
        text.append(myfile.read().replace('\n', '').replace('\r', ''))

    if (num == pages[pb]):
        files.append(" ".join(fnames))
        texts.append(" ".join(text))
        pb = pb + 1
        fnames = []
        text = []


with open('texts.pkl', 'wb') as f:
   pickle.dump(texts, f)

