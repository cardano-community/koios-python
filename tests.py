#!/usr/bin/env python

#from koios_python import block, epochs #alternative if we just need some functions
import koios_python

# con la creacion de diccionarios es fácil la impresion de un campo
params = koios_python.get_epoch_params()
nonce = params[40].get("nonce")
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
print("Ultima funcion: ")
#print(koios_python.get_account_history("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg"))

#print("Stake account list: ")
#lista = koios_python.get_asset_txs("d3501d9531fcc25e3ca4b6429318c2cc374dbdbcf5e99c1c1e5da1ff","444f4e545350414d")
#print(lista)

#lista = koios_python.get_script_redeemers("d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8")
#print(lista)
#print(len(lista))

#print(koios_python.submit_tx("signed.cbor"))

print(koios_python.get_epoch_params(338))