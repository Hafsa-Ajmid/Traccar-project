import websocket
import time
import requests
import urllib
import json
from pymongo import MongoClient
###########################################################################
# configuration
###########################################################################
email    = 'Hafsa.ajmid@gmail.com'
password = '123'
url      = 'http://160.179.202.218:56770'
###########################################################################
# mongoDB connection
###########################################################################
client = MongoClient ("mongodb+srv://tariqm:aqwzsxedcrfv@cluster0.cz3om.mongodb.net/Timestamp")
db = client["Timestamp"]
collection_currency = db["positions"]
collection_dev = db["devices"]
#########################################################################
# Get session token
###################
session = requests.Session()
params = urllib.parse.urlencode({'email': email, 'password': password})

headers = {'content-type': 'application/x-www-form-urlencoded',
           'accept': 'application/json'}

response = session.post(  url + '/api/session',data=params,headers=headers)

cookies = session.cookies.get_dict()
token= cookies['JSESSIONID']

if response.status_code == 200:
        print ("Authentication successfull, Token: "), token
else:
        print ("Authentication failed, Status:"), response.status_code
        quit()

         
# Websocket connection
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print("oooook")
    if 'position' in message[0:15]:
        data=json.loads(message)
        collection_currency.insert_one(data)
    if 'device' in message[0:15]:
        data=json.loads(message)
        collection_dev.insert_one(data)
    print(data)


def on_error(ws, error):
    print(error)

def on_close(ws):
    client.close()
    print("### closed ###")

def on_open(ws):
    def run(*args):
        while True:
            time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://160.179.202.218:56770/api/socket",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close, header = {"Cookie: JSESSIONID=" + token})
    ws.on_open = on_open
    ws.run_forever()
