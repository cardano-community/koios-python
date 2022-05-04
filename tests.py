#!/usr/bin/env python

import json
import requests


# con la creacion de diccionarios es fácil la impresion de un campo
params = get_epoch_params(336)
nonce = params.get("nonce")
print(f"Nonce: {nonce}")

print(get_block_info("b39e3463fb83c547c2410abb39d92270dee5cda7417b10755303326df09aac86").get("epoch_slot"))
