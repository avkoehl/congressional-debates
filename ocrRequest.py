# PYTHON 2
import requests
import json

def ocr_file(filename):

    f = {'file': open(filename, 'rb')}


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
    #r = requests.post('http://www.ocrwebservice.com/restservices/processDocument?', files=f, params=payload, auth=('avkoehl', 'B0BD9899-6224-4273-B777-5131F5B4FF04'))


    # FOR OCR.SPACE API / 500 pages per day
    payload = {
            'apikey': '8d00f0572b88957',
            }
    r = requests.post('https://api.ocr.space/parse/image', files=f, data=payload)

    return r.content


# process the text file and get the json result
text_file = ocr_file('test.jpg')
json = json.loads(text_file)


print (json)
