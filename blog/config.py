import os
import requests


base_path = os.getcwd()
base_path = base_path + "/media/documents"

def word_to_pdf(path_docx,path_result_pdf):
    file = open(path_docx, 'rb')
    data = file.read()
    res = requests.post(url='http://converter-eval.plutext.com:80/v1/00000000-0000-0000-0000-000000000000/convert',
                    data=data,
                    headers={'Content-Type': 'application/octet-stream'})
    f = open(path_result_pdf, 'wb')
    f.write(res.content)
    return path_result_pdf










