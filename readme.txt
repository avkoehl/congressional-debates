Written for python3

Running list of modules needed:

    os
    math
    json
    requests
    nltk



All of the data can be found on box.
  For now, just the images of the 36th session are available:
    https://ucdavis.app.box.com/folder/42738561427
  The ocrd text output files are available:
    https://ucdavis.app.box.com/folder/45108850690


The order in which these scripts are run:

  // Get and Read in the Dataset
  [1] getimagelinks.py    
  [2] downloadimages.py  
  [3] ocrRequest.py
  [4] readCorpus.py

  ---

  // Analysis to be run 
  [5] frequency.py
  [6] syntactic.py
  [7] distributional.py
 

General Hierarchy of File List:

  readme.txt

  /TimeSeries
    frequency.py
    syntactic.py
    distributional.py

  /Corpus
    getimagelinks.py
    downloadimages.py
    ocrRequest.py
    readCorpus.py

    texts.pkl

    /Images
    /Text
    /ngrams









