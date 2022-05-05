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

print("Rewards Stake key: ")
print(koios_python.get_account_rewards("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg",334))
print("\n")
print("Info Stake key: ")
print(koios_python.get_account_info("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg"))


#print("Stake account list: ")
lista = koios_python.get_account_list()
#print(lista)
print("\n")
print(f"Numero de address:  {len(lista)}")
print("\n")
