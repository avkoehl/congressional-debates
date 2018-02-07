Written for python3

Running list of modules needed:

    requests
    nltk
    matplotlib
    gensim
    numpy 


All of the data can be found on box as well as in the repo
  For now, just the images of the 36th session are available:
    https://ucdavis.app.box.com/folder/42738561427
  The ocrd text output files are available:
    https://ucdavis.app.box.com/folder/45108850690


The order in which these scripts are run:

  // Get the Dataset

  [1] Download images
      /Raw/getimagelinks.py    
      /Raw/downloadimages.py  

  [2] Run OCR
      /Raw/ocrRequest.py

  --- 

  // Process the Dataset into desired form

  [1] Preprocess raw text
      to be done skipping for now

  [2] Process text into desired time segments
      readCorpus.py


  ---

  // Generate the Time Series 

  [1] frequency
      /TimeSeries/frequency.py

  [2] syntactic
      /TimeSeries/syntactic.py

  [3] distributional 
      /TimeSeries/distributional/gensim_models.py
      /TimeSeries/distriubtional/distributional.py

  ---
  
  // Change Point Detection

      to be done

 

Hierarchy of File List:

  readme.txt

  /TimeSeries
    frequency.py
    syntactic.py
    /distributional/
      /models/
        all models (binary files)
      distributional.py
      gensim_models.py

  /Corpus/
    readcorpus.py
    weeks/
      all weeks.txt


  /Raw
    getimagelinks.py
    downloadimages.py
    ocrRequest.py
    links.txt
    Images/
      36th/
        all the images
      command.sh
    Text/
      36th/
        all the text files (!some are binary! --to be fixed)

      36th_texts.tar








