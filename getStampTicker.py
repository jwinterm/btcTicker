import requests
import json

# Set URL for bitstamp ticker info
URL = 'https://www.bitstamp.net/api/ticker/'
# Headers, because headers
headers = {'content-type': 'application/json'}


def GetTicker(serverURL=URL):
    """Try and get last block info and return formatted text"""
    # print('Attempting {0} RPC call'.format(CheckLastBlock.__name__))
    try:
        resp = requests.get(serverURL, headers=headers)
        output = json.loads(resp.text)
        print(output)
        last_price = float(output[u'last'])
        time_stamp = int(output[u'timestamp'])
        return last_price, time_stamp


    except:
        #Return out of sync if bitmonerod is not ready
        message = "error"
        return message, message


if __name__ == "__main__":
   GetTicker()