#!/usr/bin/env python
"""
Examples to check how works Koios-Python Library
"""
import pprint as pp # We recommend use pprint library to show your outputs
import koios_python # We need to install and import koios_python library
import time

#alternative if we just need some functions
#from koios_python import block, epochs

# Some examples:

## TESTENET PARAMETERS
# kp_test = koios_python.URLs(network="testnet")
# print(kp_test.url, kp_test.network)
# print(kp_test.get_account_info("stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj"))
# print(kp_test.get_native_script_list())


# kp_test = koios_python.URLs(network="mainnet")
# print(kp_test.GENESIS_URL)
# print(kp_test.url, kp_test.network)
# print(kp_test.get_tip_test_version())


############################################################
## MAINNET PARAMETERS
# Default Koios Endpoint
kp = koios_python.URLs() # We need to create an instance of the class URLs

#print(kp.get_tip())

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')

# #print(kp.get_genesis())

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')

#print(kp.get_totals())
# pprint.pp(kp.get_pool_delegators_history("pool1hrv8gtrm0dgjg6zyss5uwa4nkruzfnh5vrdkr2sayj7x2nw6mjc", 391))

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')

# check_big_account = kp.get_account_addresses(["stake1uxqh9rn76n8nynsnyvf4ulndjv0srcc8jtvumut3989cqmgjt49h6"])
# pprint.pp(check_big_account)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')

# check_big_account = kp.get_account_addresses(["stake1uxqh9rn76n8nynsnyvf4ulndjv0srcc8jtvumut3989cqmgjt49h6"])
# pprint.pp(check_big_account)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')

# get_asset_list = kp.get_asset_list(content_range="999-1999")
# print(get_asset_list)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_asset_addresses = kp.get_asset_addresses(asset_policy='750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501',asset_name='424f4f4b',content_range="0-99")
# pprint.pp(get_asset_addresses)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_asset_nft_address = kp.get_asset_nft_address(asset_policy='f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a',
#                                                asset_name='68616e646c65')
# pprint.pp(get_asset_nft_address)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_asset_info_bulk = kp.get_asset_info_bulk(["750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"],["1d7f33bd23d85e1a25d87d86fac4f199c3197a2f7afeb662a0f34e1e","776f726c646d6f62696c65746f6b656e"])
# pprint.pp(get_asset_info_bulk)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_policy_asset_addresses = kp.get_policy_asset_addresses(asset_policy='750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', content_range="0-99")
# pprint.pp(get_policy_asset_addresses)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_policy_asset_info = kp.get_policy_asset_info(asset_policy='750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501')
# pprint.pp(get_policy_asset_info)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_policy_asset_list = kp.get_policy_asset_list(asset_policy='750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501')
# pprint.pp(get_policy_asset_list)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_asset_summary = kp.get_asset_summary(asset_policy='750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', asset_name='424f4f4b')
# pprint.pp(get_asset_summary)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_asset_txs = kp.get_asset_txs(asset_policy='750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', asset_name='424f4f4b', after_block_height=50000, history=False, content_range="0-99")
# pprint.pp(get_asset_txs)

# get_asset_txs_hist_true = kp.get_asset_txs(asset_policy='750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', asset_name='424f4f4b', after_block_height=50000, history=True, content_range="0-99")
# pprint.pp(get_asset_txs_hist_true)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_address_info = kp.get_address_info("addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv","addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y")
# pprint.pp(get_address_info)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_address_txs = kp.get_address_txs("addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv","addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y",after_block=6238675)
# pprint.pp(get_address_txs)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_address_credential_utxos = kp.get_credential_utxos("025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52","025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52")
# pprint.pp(get_address_credential_utxos)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_address_assets =  kp.get_address_assets("addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv","addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y")
# pprint.pp(get_address_assets)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_address_credential_txs = kp.get_credential_txs("025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52", "13f6870c5e4f3b242463e4dc1f2f56b02a032d3797d933816f15e555", after_block=6238675)
# pprint.pp(get_address_credential_txs)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_network_params = kp.get_param_updates()
# pprint.pp(get_network_params)

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')
# get_epoch_320_info = kp.get_epoch_info(epoch_no=320, include_next_epoch=True)
# pprint.pp(get_epoch_320_info)

# get_epoch_320_info_false = kp.get_epoch_info(epoch_no=320, include_next_epoch=False)
# pprint.pp(get_epoch_320_info_false)


































############################################################
# Custom Koios Endpoint
# kp_custom_endpoint = koios_python.URLs(url="https://koios-otg.tosidrop.io/api/v0/",) # We need to create an instance of the class URLs and can specify the network if needed
# print(kp_custom_endpoint.get_tip_test_version())


############################################################
## MESASUMENT TOOLS
# To measure the speed of a function:
'''
total=0
times=3
for i in range(times):
    start = time.time()
    kp.get_account_assets("stake1u9f9v0z5zzlldgx58n8tklphu8mf7h4jvp2j2gddluemnssjfnkzz")
    #kp.get_account_assets_2("stake1u9f9v0z5zzlldgx58n8tklphu8mf7h4jvp2j2gddluemnssjfnkzz")
    #kp.get_account_assets_2("stake1u9f9v0z5zzlldgx58n8tklphu8mf7h4jvp2j2gddluemnssjfnkzz", "1000-1999")
    end = time.time()
    loop= end - start
    total += loop
total= total / times
print('Average Time: '+ str(total) + ' s')
'''
# To count number of assets in a Stake Address

# query=kp.get_account_assets("stake1u9f9v0z5zzlldgx58n8tklphu8mf7h4jvp2j2gddluemnssjfnkzz")
# #query=kp.get_account_addresses("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg")
# d=query[0]
# print(sum([len(d[x]) for x in d if isinstance(d[x], list)]))


############################################################


#pprint.pp(kp.get_account_assets_2("stake1u9f9v0z5zzlldgx58n8tklphu8mf7h4jvp2j2gddluemnssjfnkzz", "0-999"))
# pprint.pp(kp.get_account_assets("stake1u9f9v0z5zzlldgx58n8tklphu8mf7h4jvp2j2gddluemnssjfnkzz"))
# Get Native Script List, first 11 scripts
#pprint.pp(kp.get_native_script_list())

#print(len(kp.get_native_script_list('0-10')))

# Crazy Heavy Account with large number of assets
#pprint.pp(kp.get_account_assets("stake1uxqh9rn76n8nynsnyvf4ulndjv0srcc8jtvumut3989cqmgjt49h6"))

# print('------------------------------------------------------------------------------------------------------------------------------------------------------')

# pprint.pp(kp.get_account_assets_2("stake1uxqh9rn76n8nynsnyvf4ulndjv0srcc8jtvumut3989cqmgjt49h6", "0-999"))

# Heavy Account with large number of assets
#pprint.pp(kp.get_account_assets("stake1u9f9v0z5zzlldgx58n8tklphu8mf7h4jvp2j2gddluemnssjfnkzz"))

# Address of a Stake Address Account
#pprint.pp(kp.get_account_addresses("stake1uxttvx739dt505d6sxvdykj8336utdq2q92jk3sv253zp5qalcz84"))

# Get List of Accounts from 2000 to 2999
#pprint.pp(kp.get_account_list("2000-2999"))

# Get List of All Accounts
#pprint.pp(kp.get_account_list())

# Get Stake Addres Account Histoy
#pprint.pp(kp.get_account_history("stake1uxqh9rn76n8nynsnyvf4ulndjv0srcc8jtvumut3989cqmgjt49h6"))

# print(kp_mainnet.url)

# print(genesis_info_testnet)

# pprint.pp(kp.get_epoch_info(370))

# pprint.pp(kp.get_epoch_params(370))

# pprint.pp(kp.get_epoch_block_protocols(380))

#pprint.pp(kp.get_genesis())

#pprint.pp(kp.get_asset_history("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"))
#pprint.pp(kp.get_asset_summary("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"))

# pprint.pp(kp.get_asset_txs("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b",63487))

# Get Datum information for given datum hashes of a Plutus Contracts
#pprint.pp(kp.get_datum_info('818ee3db3bbbd04f9f2ce21778cac3ac605802a4fcb00c8b3a58ee2dafc17d46',
#    "45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0"))

# pprint.pp(kp_mainnet.get_pool_stake_snapshot("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc"))

# Get info of epoch number 337:
#pprint.pp(koios_python.get_epoch_params(337))

# Get info of two transactions:
#pprint.pp(koios_python.get_tx_metadata(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e" \
# ,"0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

#Get detailed information about a specifics blocks
# pprint.pp(kp.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30", \
# "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a", \
# "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"]))

# Submit an already serialized transaction to the network from a binay file-system
#print(koios_python.submit_tx("signed.cbor"))

# Get number of confirmations of a list of hash transactions
#pprint.pp(koios_python.get_tx_status(["b50d56706c07a3c11f21fbbca3da7a3754398acb38b91a38a36cbea5c895e02f" \
# ,"0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# Get address/es info - balance, associated stake address (if any) and UTxO set.
# pprint.pp(kp.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g"))
#pprint.pp(koios_python.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g", \
#    "addr1qx6e0rnz0xmpn90d69mg3fvcjdleg30tjkxuwvztkd2m5eh9hzc5q00t5p20fy0j0cvph9rzntsf2ve6mdcpgs4s4alq84zgkh"))

# Get the full rewards history (including MIR) for a stake address, or certain epoch if specified
#print(koios_python.get_account_rewards("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg" \
# ,335))

# Get account history for a stake address
#pprint.pp(koios_python.get_account_history("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg"))

# Get the transaction hash list of input payment credential array, optionally filtering after specified block height 
# pprint.pp(kp.get_credential_txs( "025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52", 333333))

# Get the mint/burn history of an asset
#pprint.pp(koios_python.get_asset_history("d3501d9531fcc25e3ca4b6429318c2cc374dbdbcf5e99c1c1e5da1ff" \
# , "444f4e545350414d"))

# Current pool statuses and details for a specified list of pool ids
#pprint.pp(koios_python.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp", \
#"pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m", \
#"pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"]))

# Get the Pool List from the record 2001 to 3000
#pprint.pp(koios_python.get_pool_list("2001-3000"))

# Get the Asset List from the record 2001 to 3000
#pprint.pp(kp.get_asset_list("2001-3000"))

# Get Delegator List from a Pool
#pprint.pp(kp.get_pool_delegators("pool1x5dfpgp987e4jhxvgczr3wv50nv2pwd873tlx3uthvcasm422q6", "1000-2000"))

#pprint.pp(kp.get_asset_address_list("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b", "10-20"))

# Get all the information for a specified Stake Pool
#pprint.pp(koios_python.get_pool_info("pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp"))

# List of all redeemers for a given script hash.
#pprint.pp(kp.get_script_redeemers("d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8"))

#pprint.pp(kp.get_address_assets("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g"))


# Get the staking history of given stake addresses (accounts), you can add as last parameter epoch number
#pprint.pp(kp.get_account_history("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
#   "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy", 350))