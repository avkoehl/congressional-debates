Written for python2 and python3. Eventually should be reworked to only be python3!

Running list of modules needed:

  Python3
    urllib

  Python2.7 
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
  [1] getimagelinks.py    -Python3
  [2] downloadimages.py   -Python3
  [3] ocrRequest.py
  [4] readCorpus.py

  ---

  // Analysis to be run 
  [5] frequency.py
  [6] posdist.py
  [7] cpdetection.py








