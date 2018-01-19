# PYTHON 2
import os
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

