
from api import *

# validators = get_validators()
# genesis = get_genesis()
# last_block = get_last_block()
# header_last_block = last_block.get("block").get("header")
# height_last_block = last_block.get("block").get("header").get("height")
# hash_last_block = last_block.get("block_id").get("hash")
# time_last_block = last_block.get("block").get("header").get("time")
# proposer_address = last_block.get("block").get("header").get("proposer_address")
# #specific_block = get_block(96437)

# #not confirmed transactions
# unconfirmed_txs = get_unconfirmed_txs()


# #get min and max height block headers
# blockchain = get_blockchain()


# block_by_hash = get_block_by_hash(hash_last_block)


teste = get_net_info()

for i in teste:
    print(i.get("node_info").get("moniker"), i.get("remote_ip"))