"""This module corresponds to functionality documented
at https://blockchain.info/api/charts_api

"""



import json
import sys


class APIException(Exception):
    def __init__(self, message, code):
        Exception.__init__(self, message)
        self.code = code


BASE_URL = "https://rpc.musselnet.cosmwasm.com"
TIMEOUT = 10




py_version = sys.version_info[0]
if py_version >= 3:
    # Python 3.0 and later
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.parse import urlencode
else:
    # Python 2.x
    from urllib2 import urlopen
    from urllib2 import HTTPError
    from urllib import urlencode


def call_api(resource, data=None, base_url=None):
    base_url = BASE_URL if base_url is None else base_url
    try:
        payload = None if data is None else urlencode(data)
        if py_version >= 3 and payload is not None:
            payload = payload.encode('UTF-8')
        response = urlopen(base_url + resource, payload, timeout=TIMEOUT).read()
        return handle_response(response)
            
    except HTTPError as e:
        raise APIException(handle_response(e.read()), e.code)


def handle_response(response):
    # urllib returns different types in Python 2 and 3 (str vs bytes)
    if isinstance(response, str):
        return response
    else:
        return response.decode('utf-8')



def get_genesis(api_code=None):
    
    
    resource = '/genesis'
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    #print(response.result)
    json_response = json.loads(response)
    # print(len(json_response.get("result")))
    json_response = json_response.get("result")
    json_response = json_response.get("genesis")
    return json_response


def get_last_block(api_code=None):
    
    
    resource = '/block'
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    #print(response.result)
    json_response = json.loads(response)
    # print(len(json_response.get("result")))
    json_response = json_response.get("result")
    json_response = json_response.get("block")
    return json_response





def get_validators(api_code=None):
    
    
    resource = '/validators'
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    #print(response.result)
    json_response = json.loads(response)
    # print(len(json_response.get("result")))
    json_response = json_response.get("result")
    json_response = json_response.get("validators")
    #json_object = json.dumps(json_response,indent=4) 
    #test = json_response.validators
    return json_response




# class Stats:
#     def __init__(self, s):
#         self.validators = s['validators']
#         # self.trade_volume_btc = s['trade_volume_btc']
#         # self.miners_revenue_usd = s['miners_revenue_usd']
#         # self.btc_mined = s['n_btc_mined']
#         # self.trade_volume_usd = s['trade_volume_usd']
#         # self.difficulty = s['difficulty']
#         # self.minutes_between_blocks = s['minutes_between_blocks']
#         # self.number_of_transactions = s['n_tx']
#         # self.hash_rate = s['hash_rate']
#         # self.timestamp = s['timestamp']
#         # self.mined_blocks = s['n_blocks_mined']
#         # self.blocks_size = s['blocks_size']
#         # self.total_fees_btc = s['total_fees_btc']
#         # self.total_btc_sent = s['total_btc_sent']
#         # self.estimated_btc_sent = s['estimated_btc_sent']
#         # self.total_btc = s['totalbc']
#         # self.total_blocks = s['n_blocks_total']
#         # self.next_retarget = s['nextretarget']
#         # self.estimated_transaction_volume_usd = s['estimated_transaction_volume_usd']
#         # self.miners_revenue_btc = s['miners_revenue_btc']
#         # self.market_price_usd = s['market_price_usd']


# class Chart:
#     def __init__(self, c):
#         self.status = c['status']
#         self.name = c['name']
#         self.unit = c['unit']
#         self.period = c['period']
#         self.description = c['description']
#         self.values = [Point(point) for point in c['values']]


# class Point:
#     def __init__(self, p):
#         self.x = p['x']
#         self.y = p['y']
