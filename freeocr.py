# PYTHON 2
import requests
import json

def ocr_file(filename):

    f = {'file': open(filename, 'rb')}
    payload = {
            'language': 'english',
            'pagerange': 'allpages',
            'tobw': 'true',
            'outputformat': 'txt',
            'gettext': 'true',
            'user_name': 'AVKOEHL',
            'license_code': 'B0BD9899-6224-4273-B777-5131F5B4FF04',
            }
    r = requests.post('http://www.ocrwebservice.com/restservices/processDocument?', files=f, params=payload, auth=('avkoehl', 'B0BD9899-6224-4273-B777-5131F5B4FF04'))

    return r.content


# Use examples:
text_file = ocr_file('test.jpg')
json = json.loads(text_file)


print (json["OCRText"])
