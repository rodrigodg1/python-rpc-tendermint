# -*- coding: utf-8 -*-

from api import *

validators = get_validators()
genesis = get_genesis()
last_block = get_last_block()
header_last_block = last_block.get("header")
height_last_block = header_last_block.get("height")


specific_block = get_block(96437)
