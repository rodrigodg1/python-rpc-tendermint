# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect,session,flash

app = Flask(__name__)


from api import *


def update_info():
    #update amount validators
    validators = get_validators()
    #genesis = get_genesis()
    
    #get info about last block commited
    last_block = get_last_block()
    height_last_block = last_block.get("block").get("header").get("height")
    hash_last_block = last_block.get("block_id").get("hash")
    time_last_block = last_block.get("block").get("header").get("time")
    #split timestamp date and hour
    time_last_block = time_last_block.split('T',1)
    #split hour
    time_last_block_hour = time_last_block[1].split('.',1)
    #data and hour only
    time_last_block[1] = time_last_block_hour[0]
    
    #block proposer ID
    proposer_address = last_block.get("block").get("header").get("proposer_address")
    
    last_block_size = get_blockchain()[0].get("block_size")
    
    last_block_height = get_blockchain()[0].get("header").get("height")

    #get transactions from the latest block
    transactions_last_block = last_block.get("block").get("data")
    
    #get signatures from the latest block
    signatures_last_block = last_block.get("block").get("last_commit").get("signatures")

    #not confirmed transactions
    unconfirmed_txs = get_unconfirmed_txs()
    

    
    
    #network info
    net_info = get_net_info()
    list_net_info = []
    
    
    #network name id
    network_name = net_info[0].get("node_info").get("network")
    

    for i in net_info:
        #print(i.get("node_info").get("moniker"), i.get("remote_ip"))
        
        #tuple with moniker, ip addr and ID
        #list_net_info.append((i.get("node_info").get("moniker"), i.get("remote_ip"), i.get("node_info").get("id")))

        
        #tuple with moniker and ip addr
        
        list_net_info.append((i.get("node_info").get("moniker"), i.get("remote_ip")))
        
        #only network address
        #list_net_info.append(i.get("remote_ip"))
        
    
    return validators,height_last_block,unconfirmed_txs,time_last_block,proposer_address,hash_last_block,list_net_info,transactions_last_block,signatures_last_block,network_name,last_block_size,last_block_height






@app.route('/')
def index():
    platform = "CosmWasm"
         
    validators,height_last_block,unconfirmed_txs,time_last_block,proposer_address,hash_last_block,list_net_info,transactions_last_block,signatures_last_block,network_name,last_block_size,last_block_height = update_info()
    
    return render_template('index.html',titulo="Tendermint RPC Explorer",
                            validators= len(validators),height = height_last_block,
                            unconfirmed_txs = unconfirmed_txs,time_last_block = time_last_block,
                            proposer_address = proposer_address,hash_last_block=hash_last_block,
                            list_net_info = list_net_info,
                            transactions_last_block = transactions_last_block,
                            signatures_last_block = signatures_last_block,
                            network_name = network_name,platform = platform,
                            last_block_size = last_block_size,
                            last_block_height = last_block_height)










app.run(host='0.0.0.0',debug=True)