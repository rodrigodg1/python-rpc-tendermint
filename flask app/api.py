

from utils import *


def get_block(height=None,api_code=None):
    
    resource = '/block?height='
    resource += str(height)
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    #print(response.result)
    json_response = json.loads(response)
    json_response = json_response.get("result")
    json_response = json_response.get("block")
    return json_response



def get_net_info(api_code=None):
    
    resource = '/net_info'
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    #print(response.result)
    json_response = json.loads(response)
    json_response = json_response.get("result")
    json_response = json_response.get("peers")
    return json_response




def get_genesis(api_code=None):
     
    resource = '/genesis'
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    #print(response.result)
    json_response = json.loads(response)
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
    json_response = json_response.get("result")
    return json_response



def get_block_by_hash(hash,api_code=None):

    resource = f'/block_by_hash?hash=0x{hash}'
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    json_response = json.loads(response)
    json_response = json_response.get("result")

    return json_response



def get_unconfirmed_txs(api_code=None):
    
    resource = '/num_unconfirmed_txs'
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    json_response = json.loads(response)
    json_response = json_response.get("result")
    json_response = json_response.get("total")

    return json_response


#if min and max is none,return the last 20 block headers on the blockchain
def get_blockchain(min=None,max=None,api_code=None):
    
    if max is not None and min is not None:
        resource = f'/blockchain?minHeight={min}&maxHeight={max}'
    else:
        resource = '/blockchain'
        
    if api_code is not None:
        resource += '&api_code=' + api_code
        
    print(resource)
    response = call_api(resource)
    json_response = json.loads(response)
    json_response = json_response.get("result")
    json_response = json_response.get("block_metas")

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


