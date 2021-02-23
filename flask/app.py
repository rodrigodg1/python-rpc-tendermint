# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect,session,flash

app = Flask(__name__)


from api import *


def update_info():
    validators = get_validators()
    #genesis = get_genesis()
    last_block = get_last_block()
    height_last_block = last_block.get("block").get("header").get("height")
    hash_last_block = last_block.get("block_id").get("hash")
    time_last_block = last_block.get("block").get("header").get("time")
    proposer_address = last_block.get("block").get("header").get("proposer_address")


    #not confirmed transactions
    unconfirmed_txs = get_unconfirmed_txs()
    

    
    
    #network info
    net_info = get_net_info()
    list_net_info = []

    for i in net_info:
        #print(i.get("node_info").get("moniker"), i.get("remote_ip"))
        
        #only network address
        list_net_info.append(i.get("remote_ip"))
        
    
    return validators,height_last_block,unconfirmed_txs,time_last_block,proposer_address,hash_last_block,list_net_info



@app.route('/')
def index():
         
    validators,height_last_block,unconfirmed_txs,time_last_block,proposer_address,hash_last_block,list_net_info = update_info()
    
    return render_template('index.html',titulo="CosmWasm Explorer",
                            validators= len(validators),height = height_last_block,
                            unconfirmed_txs = unconfirmed_txs,time_last_block = time_last_block,
                            proposer_address = proposer_address,hash_last_block=hash_last_block,
                            list_net_info = list_net_info)

@app.route('/info')
def info():

    return render_template('index.html', validators= len(validators),height = height_last_block)

app.run(host='0.0.0.0',debug=True)