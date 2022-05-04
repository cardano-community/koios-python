#!/usr/bin/env python

#from koios_python import block, epochs #alternative if we just need some functions
import koios_python

# con la creacion de diccionarios es fácil la impresion de un campo
params = koios_python.get_epoch_params(336)
nonce = params.get("nonce")
print(f"Nonce: {nonce}")

print(koios_python.get_block_info("b39e3463fb83c547c2410abb39d92270dee5cda7417b10755303326df09aac86"))
