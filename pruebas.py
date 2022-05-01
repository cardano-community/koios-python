import json
import sys
import requests

########### KOIOS EJEMPLO GET ############################
koios_get = requests.get("https://api.koios.rest/api/v0/tip")
koios_get = json.loads(koios_get.content)
print(koios_get)
##########################################################


########### KOIOS EJEMPLO POST ###########################
#my_header ={"Accept: application/json"+"Content-Type: application/json"}
tx = {"_tx_hashes":["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e","0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]}
koios_post = requests.post( "https://api.koios.rest/api/v0/tx_info", json = tx)
koios_post = json.loads(koios_post.content)
print(koios_post)
##########################################################