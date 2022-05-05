#!/usr/bin/env python

#from koios_python import block, epochs #alternative if we just need some functions
import koios_python

# con la creacion de diccionarios es fácil la impresion de un campo
params = koios_python.get_epoch_params(336)
nonce = params.get("nonce")
print(f"Nonce: {nonce}")
print("\n")
print("Info Billetera: ")
print(koios_python.get_address_txs(["addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g"]))
print("\n")

#print(koios_python.get_tx_metadata("e7560a87f71adcd4b007e765ab432c5310310e036a3a8a7708c21f6dbd8a0400"))

#print(koios_python.get_tx_metalabels())

print("Info Stake key: ")
print(koios_python.get_credential_txs(["025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52",
    "13f6870c5e4f3b242463e4dc1f2f56b02a032d3797d933816f15e555"]))

print("Stake account list: ")
lista = koios_python.get_account_list()

print(lista)

print("Numero de address: "+len(lista))

print("\n")
