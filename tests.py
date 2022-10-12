#!/usr/bin/env python
"""
Examples to check how works Koios-Python Library
"""
import pprint # We recommend use pprint library to show your outputs
import koios_python # We need to install and import koios_python library


#alternative if we just need some functions
#from koios_python import block, epochs

# Some examples:

# Get info of epoch number 337:
#pprint.pp(koios_python.get_epoch_params(337))

# Get info of two transactions:
#pprint.pp(koios_python.get_tx_metadata(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e" \
# ,"0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

#Get detailed information about a specifics blocks
#pprint.pp(koios_python.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30", \
#"60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a", \
#"c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"]))

# Submit an already serialized transaction to the network from a binay file-system
#print(koios_python.submit_tx("signed.cbor"))

# Get number of confirmations of a list of hash transactions
#pprint.pp(koios_python.get_tx_status(["b50d56706c07a3c11f21fbbca3da7a3754398acb38b91a38a36cbea5c895e02f" \
# ,"0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# Get address/es info - balance, associated stake address (if any) and UTxO set.
#pprint.pp(koios_python.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g"))
#pprint.pp(koios_python.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g", \
#    "addr1qx6e0rnz0xmpn90d69mg3fvcjdleg30tjkxuwvztkd2m5eh9hzc5q00t5p20fy0j0cvph9rzntsf2ve6mdcpgs4s4alq84zgkh"))

# Get the full rewards history (including MIR) for a stake address, or certain epoch if specified
#print(koios_python.get_account_rewards("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg" \
# ,335))

# Get account history for a stake address
#pprint.pp(koios_python.get_account_history("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg"))

# Get the transaction hash list of input payment credential array, optionally filtering after specified block height 
#pprint.pp(koios_python.get_credential_txs( "025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52", 333333))

# Get the mint/burn history of an asset
#pprint.pp(koios_python.get_asset_history("d3501d9531fcc25e3ca4b6429318c2cc374dbdbcf5e99c1c1e5da1ff" \
# , "444f4e545350414d"))

# Current pool statuses and details for a specified list of pool ids
#pprint.pp(koios_python.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp", \
#"pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m", \
#"pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"]))

# Get the Pool List from the record 2001 to 3000
#pprint.pp(koios_python.get_pool_list("2001-3000"))

# Get all the information for a specified Stake Pool
#pprint.pp(koios_python.get_pool_info("pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp"))

# List of all redeemers for a given script hash.
#pprint.pp(koios_python.get_script_redeemers("d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8"))

#pprint.pp(koios_python.get_address_assets("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g"))


# Get the staking history of given stake addresses (accounts), you can add as last parameter epoch number
#pprint.pp(koios_python.get_account_history("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
#    "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy", 350))


pprint.pp(koios_python.get_totals())