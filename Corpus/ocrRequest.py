# PYTHON 3
import requests
import json
import os

def ocr_file(filename):
    f = {'file': open(filename, 'rb')}

    # OCR PAID MONTLY API KEY, REMEMBER TO CANCEL
    payload = {
            'apikey': 'PKMXB5865888A',
            }
    r = requests.post('https://apipro1.ocr.space/parse/image', files=f, data=payload)

    return r.content


# input and output paths
path = './images/36th/'
opath = './texts/36th/'

i = 0
failed = 0
for fname in os.listdir(path): # get all the filenames
    print ("processing file", i, "of", len(os.listdir(path)), ": ", path + fname)
    fnameshort = fname.split('.')[0] # get just the name no extension

    ofile = open(opath + fnameshort + ".txt", "w")
    filename = path + fname
    response = ocr_file (filename)
    js = json.loads(response)

    try:
        text = js["ParsedResults"][0]["ParsedText"]
        text = text.encode('utf-8')
        ofile.write(text)
    except:
        print ("failed!")
        print (js.encode('utf-8'))
        ofile.write(js.encode('utf-8'))
        failed = failed + 1

    i = i + 1


### ADDITIONAL INFORMATION AND EXAMPLES
# FOR FREE OCR API / 25 pages per day for one month
#    payload = {
#            'language': 'english',
#            'pagerange': 'allpages',
#            'tobw': 'true',
#            'outputformat': 'txt',
#            'gettext': 'true',
#            'user_name': 'AVKOEHL',
#            'license_code': 'B0BD9899-6224-4273-B777-5131F5B4FF04',
#            }
#   r = requests.post('http://www.ocrwebservice.com/restservices/processDocument?', files=f, params=payload, auth=('avkoehl', 'B0BD9899-6224-4273-B777-5131F5B4FF04'))

# FOR OCR.SPACE API / 500 pages per day
#        'apikey': '8d00f0572b88957',
#       r = requests.post('https://api.ocr.space/parse/image', files=f, data=payload)
