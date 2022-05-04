#!/usr/bin/env python

#from koios_python import block, epochs #alternative if we just need some functions
import koios_python

# con la creacion de diccionarios es fácil la impresion de un campo
params = koios_python.get_epoch_params(336)
nonce = params.get("nonce")
print(f"Nonce: {nonce}")
print("\n")
print(koios_python.get_block_info("b39e3463fb83c547c2410abb39d92270dee5cda7417b10755303326df09aac86"))
print("\n")

print(koios_python.get_tx_info("0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94").get("block_hash"))

#print(tx.get("block_hash"))
print("\n")