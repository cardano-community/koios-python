#!/usr/bin/env python

#from koios_python import block, epochs #alternative if we just need some functions
import koios_python

# con la creacion de diccionarios es fácil la impresion de un campo
params = koios_python.get_epoch_params(336)
nonce = params.get("nonce")
print(f"Nonce: {nonce}")
print("\n")
print("Info Transaccion: ")
print(koios_python.get_tx_status("4766ec1e951f5ae7b46d3bdc2ea06581c9c73efce96e7b3fd584f1d8027b1513"))
print("\n")

#print(koios_python.get_tx_metadata("e7560a87f71adcd4b007e765ab432c5310310e036a3a8a7708c21f6dbd8a0400"))

#print(koios_python.get_tx_metalabels())

print(koios_python.get_address_assets("addr1q893649cdrffstcs0xmtnj3kcdw4z9cwe95rjl3lvl7dr889hzc5q00t5p20fy0j0cvph9rzntsf2ve6mdcpgs4s4alq5zld46"))

print("\n")
