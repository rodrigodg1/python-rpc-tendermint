# -*- coding: utf-8 -*-

from api import *

validators = get_validators()
genesis = get_genesis()
last_block = get_last_block()
test = last_block.get("header")
