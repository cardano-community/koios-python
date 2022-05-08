#!/usr/bin/env python

#from koios_python import block, epochs #alternative if we just need some functions
import koios_python



# Get info of epoch number 338:
#print(koios_python.get_epoch_params(338))

# Get info of two transactions:
#print(koios_python.get_tx_metadata(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e","0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# Submit an already serialized transaction to the network from a binay file-system
#print(koios_python.submit_tx("signed.cbor"))

# Get number of confirmations of a list of hash transactions
#print(koios_python.get_tx_status(["b50d56706c07a3c11f21fbbca3da7a3754398acb38b91a38a36cbea5c895e02f","0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

address = "addr1qx7pv34j2lzt4mwrcs2w0ljpdsj7cqkn2rvxukjtk0yjynh9hzc5q00t5p20fy0j0cvph9rzntsf2ve6mdcpgs4s4alqp2pah2"
print(koios_python.get_address_info(address))