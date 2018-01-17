# PYTHON 2
import os
import nltk


##
path = './texts/36th/'

## sort the files into filelist
filelist = os.listdir(path)
filelist = sorted(filelist)

# page breaks weeks: 0 - 9
pages = ["00250023", "00970095", "01830181", "02120210", "02650263", "03530351", "04850483", "05870585", "07210719", "00930091"]
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

# Now in texts[0] is all the text up to 00250023 and texts[1] has 00250023 to 00970095 and so on
# need to tokenize each element in texts and then calculate word frequencies, will use nltk

