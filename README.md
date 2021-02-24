# Python Query RPC Tendermint - Client
Query rpc with python code

* You need to change RPC Server Address in utils.py
* Inside the file api.py are the query methods

## Examples

* return all validators
    > validators = get_validators()

* return the genesis block
    > genesis = get_genesis()

* return especific block
    > specific_block = get_block(96437)

* return the lastest block
    > last_block = get_last_block()


As the return is an object or dictionary, you can be more specific with the query. Example:

* return the lastest block header
     > header_last_block = last_block.get("header")

* return the lastest block height
     > height_last_block = header_last_block.get("height")



