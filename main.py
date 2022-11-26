from base64 import b64encode

from threading import Thread

from random import randint

import hashlib

from hmac import new


from uuid import uuid4

from flask import Flask,request



Hex42 = bytes.fromhex("42")

def sig(data: str):
    
    Hex93 = bytes.fromhex("f8e7a61ac3f725941e3ac7cae2d688be97f30b93")

    return b64encode( Hex42 + new( Hex93 , data.encode() ,hashlib.sha1 ).digest()).decode()

def devicId():
    data = uuid4().bytes
    Hex66 = bytes.fromhex("02b258c63559d8804321c5d5065af320358d366f")

    return ("42" + data.hex() + new( Hex66,  Hex42 + data, hashlib.sha1 ).hexdigest()).upper()

app = Flask(__name__)




"""
HOME
"""
@app.route('/', methods=['POST','GET'])
def home():


    return 'API Developed By Emp'



'''
SIG
'''


@app.route('/sig', methods=['POST'])
def s():
    try:
        request_data = request.get_json()
        data = request_data['data']
    except:
        return {
        "sig":None
    }
   

    return {
        "sig":sig(data),
    }






'''
DEVICID
'''
@app.route('/devicId', methods=['get'])
def d():
   

    return {
        "devicId":devicId(),
    } 



def Run():
	app.run(host='0.0.0.0', port=randint(2000, 9000))




def keep_alive():

	t = Thread(target=Run)
	t.start()
        

if __name__ == '__main__':
    keep_alive()


