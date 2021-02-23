

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
    # print(len(json_response.get("result")))
    json_response = json_response.get("result")
    json_response = json_response.get("block")
    return json_response




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


