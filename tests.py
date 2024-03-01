#!/usr/bin/env python
"""
Examples to check how works Koios-Python Library
"""
import pprint as pp # We recommend use pprint library to show your outputs
from koios_python  import * # We need to install and import koios_python library
# from koios_python import block, epochs # alternative if we just need some functions
import time
import os
from dotenv import load_dotenv
# load the environment variables
load_dotenv()
# Get api token
token = os.getenv("TOKEN")


##########################################################################################
## MAINNET PARAMETERS (simple TESTS)
# Public Tier with Default Koios Endpoint
#kp = URLs() # We need to create an instance of the class URLs (no bearer token) FREE TIER

# Select this if you are usinf Bearer Token. We need to create an instance of the class URLs (with bearer token)
kp = URLs(bearer=token)
#pp.pprint(kp.BEARER)

##########################################################################################
# Network Endpoint Tests
##########################################################################################
# # Get tip (no bearer token)
#pp.pprint(kp.get_tip())

# # Get tip (with bearer token)
# pp.pprint(kp_token.get_tip())

# # Get Genesis (no bearer token)
# pp.pprint(kp.get_genesis())

# # Get Genesis (with bearer token)
# pp.pprint(kp_token.get_genesis())

# # Get Totals (no bearer token)
# pp.pprint(kp.get_totals())
# pp.pprint(kp.get_totals(epoch_no=320))

# # Get Totals (with bearer token)
# pp.pprint(kp_token.get_totals())
# pp.pprint(kp_token.get_totals(epoch_no=320))

# Get Network Param Updates (no bearer token)
# pp.pprint(kp.get_param_updates())

# # Get Network Param Updates (with bearer token)
# pp.pprint(kp_token.get_param_updates())

# # Get Reserve Withdrawals (no bearer token)
# pp.pprint(kp.get_reserve_withdrawals())

# # Get Reserve Withdrawals (with bearer token)
# pp.pprint(kp_token.get_reserve_withdrawals())

# # Get Treasury Withdrawals (no bearer token)
# pp.pprint(kp.get_treasury_withdrawals())

# # Get Treasury Withdrawals (with bearer token)
# pp.pprint(kp_token.get_treasury_withdrawals())

##########################################################################################
# Epoch Endpoint Tests
##########################################################################################

# # Get Epoch Info (no bearer token)
# get_epoch_320_info = kp.get_epoch_info(epoch_no=320, include_next_epoch=True)
# pp.pprint(get_epoch_320_info)

# get_epoch_320_info_false = kp.get_epoch_info(epoch_no=320, include_next_epoch=False)
# pp.pprint(get_epoch_320_info_false)

# # Get Epoch Info (with bearer token)
# get_epoch_320_info = kp_token.get_epoch_info(epoch_no=320, include_next_epoch=True)
# pp.pprint(get_epoch_320_info)

# get_epoch_320_info_false = kp_token.get_epoch_info(epoch_no=320, include_next_epoch=False)
# pp.pprint(get_epoch_320_info_false)

# # Get Epoch Params (no bearer token)
# pp.pprint(kp.get_epoch_params(320))

# # Get Epoch Params (with bearer token)
# pp.pprint(kp_token.get_epoch_params(320))

# # Get Epoch Block Protocols (no bearer token)
# pp.pprint(kp.get_epoch_block_protocols(320))

# # Get Epoch Block Protocols (with bearer token)
# pp.pprint(kp_token.get_epoch_block_protocols(320))

##########################################################################################
# Block Endpoint Tests
##########################################################################################

# Get Block List (no bearer token)
# pp.pprint(kp.get_blocks("0-10"))

# # Get Block List (with bearer token)
# pp.pprint(kp_token.get_blocks("0-10"))

# # Get Block Info (no bearer token)
# pp.pprint(kp.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30", \
# "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a", \
# "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"]))

# # Get Block Info (with bearer token)
# pp.pprint(kp_token.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30", \
# "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a", \
# "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"]))

# # Get Block Txs (no bearer token)
# pp.pprint(kp.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30", \
# "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a", \
# "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"]))

# # Get Block Txs (with bearer token)
# pp.pprint(kp_token.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30", \
# "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a", \
# "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"]))



##########################################################################################
# Transaction Endpoint Tests
##########################################################################################

# # Get UTxO info
# pp.pprint(kp.get_utxo_info(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e#0"]))

# pp.pprint(kp.get_utxo_info(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e#0", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94#0"]))

# # Get UTxO info ( extended)
# pp.pprint(kp.get_utxo_info(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e#0", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94#0"], extended=True, content_range="0-9"))
# pp.pprint(kp.get_utxo_info(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e#0", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94#0"], extended=False, content_range="0-9"))

# # Get Tx Info (no bearer token)
# pp.pprint(kp.get_tx_info(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# # Get Tx Info (with bearer token)
# pp.pprint(kp_token.get_tx_info(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# # Get Tx Metadata (no bearer token)
# pp.pprint(kp.get_tx_metadata(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# # Get Tx Metadata (with bearer token)
# pp.pprint(kp_token.get_tx_metadata(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# # Get Tx Metalabels (no bearer token)
# pp.pprint(kp.get_tx_metalabels(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# # Get Tx Metalabels (with bearer token)
# pp.pprint(kp_token.get_tx_metalabels(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# # Submit Tx (no bearer token)
# Testing soon

# # Submit Tx (with bearer token)
# Testing soon

# # Get Tx Status (no bearer token)
# pp.pprint(kp.get_tx_status(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# # Get Tx Status (with bearer token)
# pp.pprint(kp_token.get_tx_status(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# # Get Tx Utxos (no bearer token)
# pp.pprint(kp.get_tx_utxos("f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"))

# # Get Tx Utxos (with bearer token)
# pp.pprint(kp_token.get_tx_utxos("f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e", \
# "0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"))

##########################################################################################
# Address Endpoint Tests
##########################################################################################

# # Get Address Info (no bearer token)
# pp.pprint(kp.get_address_info(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"]))

# # Get Address Info (with bearer token)
# pp.pprint(kp_token.get_address_info(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"]))

# # Get Address UTxOs (no bearer token)
# pp.pprint(kp.get_address_utxos(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"]))

# # Get Address UTxOs (no bearer token, extended)
# pp.pprint(kp.get_address_utxos(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"], extended=True, content_range="0-9"))
# pp.pprint(kp.get_address_utxos(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"], extended=False, content_range="0-9"))

# # Get Address UTxOs (with bearer token)
# pp.pprint(kp_token.get_address_utxos(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"]))

# # Get Address UTxOs (with bearer token, extended)
# pp.pprint(kp_token.get_address_utxos(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"], extended=True, content_range="0-9"))
# pp.pprint(kp_token.get_address_utxos(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"], extended=False, content_range="0-9"))

# # Get Address Txs (no bearer token)
# pp.pprint(kp.get_address_txs(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"],
# after_block=6238675))

# # Get Address Txs (with bearer token)
# pp.pprint(kp_token.get_address_txs(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv",\
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"],
# after_block=6238675))

# # Get Address Assets (no bearer token)
# pp.pprint(kp.get_address_assets(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv", \
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"]))

# # Get Address Assets (with bearer token)
# pp.pprint(kp_token.get_address_assets(["addr1qy2jt0qpqz2z2z9zx5w4xemekkce7yderz53kjue53lpqv90lkfa9sgrfjuz6uvt4uqtrqhl2kj0a9lnr9ndzutx32gqleeckv", \
# "addr1q9xvgr4ehvu5k5tmaly7ugpnvekpqvnxj8xy50pa7kyetlnhel389pa4rnq6fmkzwsaynmw0mnldhlmchn2sfd589fgsz9dd0y"]))

# # Get UTxOs from payment credentials (no bearer token)
# pp.pprint(kp.get_credential_utxos(["025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52", \
# "13f6870c5e4f3b242463e4dc1f2f56b02a032d3797d933816f15e555"], extended=True, content_range="0-9"))

# # Get UTxOs from payment credentials (with bearer token)
# pp.pprint(kp_token.get_credential_utxos(["025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52",
# "13f6870c5e4f3b242463e4dc1f2f56b02a032d3797d933816f15e555"], extended=False, content_range="0-9"))

# # Get Credential TXs (no bearer token)
# pp.pprint(kp.get_credential_txs("025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52", \
# "13f6870c5e4f3b242463e4dc1f2f56b02a032d3797d933816f15e555", after_block=6238675))

# # Get Credential TXs (with bearer token)
# pp.pprint(kp_token.get_credential_txs("025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52", \
# "13f6870c5e4f3b242463e4dc1f2f56b02a032d3797d933816f15e555", after_block=6238675))

##########################################################################################
# Pool Endpoint Tests
##########################################################################################

# # Get Pool List
# pp.pprint(kp.get_pool_list('0-10'))

# # Get Pool Info
# pp.pprint(kp.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp",
# "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m",
# "pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"]))

# # Get Pool Stake Snapshot
# pp.pprint(kp.get_pool_stake_snapshot("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc"))

# # Get Pool Delegators
# pp.pprint(kp.get_pool_delegators("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", content_range="0-9"))

# # Get Pool Delegators History
# pp.pprint(kp.get_pool_delegators_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", epoch_no=320))

# # Get Pool Metadata
# pp.pprint(kp.get_pool_metadata())
# pp.pprint(kp.get_pool_metadata("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc"))

# # Get Pool Relays
# pp.pprint(kp.get_pool_relays())
# pp.pprint(kp.get_pool_relays('0-70'))

# # Get Pool Updates
# pp.pprint(kp.get_pool_updates("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc"))

##########################################################################################
# Asset Endpoint Tests
##########################################################################################

# # Get Asset List (no bearer token)
# pp.pprint(kp.get_asset_list(content_range="0-9"))

# # Get Asset List (with bearer token)
# pp.pprint(kp_token.get_asset_list(content_range="0-9"))

# # Get Policy Asset List (no bearer token)
# pp.pprint(kp.get_policy_asset_list("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","0-9"))

# # Get Policy Asset List (with bearer token)
# pp.pprint(kp_token.get_policy_asset_list("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","0-9"))

# # Get Asset Token Registry (no bearer token)
# pp.pprint(kp.get_asset_token_registry("0-9"))

# # Get Asset Token Registry (with bearer token)
# pp.pprint(kp_token.get_asset_token_registry("0-9"))

# # Get Asset Information (Bulk) (no bearer token)
# pp.pprint(kp.get_asset_info_bulk(["750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"], \
# ["f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a","6b6f696f732e72657374"]))

# # Get Asset Information (Bulk) (with bearer token)
# pp.pprint(kp_token.get_asset_info_bulk(["750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"], \
# ["f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a","6b6f696f732e72657374"]))

# # Get Asset UTxOs (no bearer token, extended=False)
# pp.pprint(kp.get_asset_utxos(["750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"], \
# ["f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a","6b6f696f732e72657374"], extended=False))

# # Get Asset UTxOs (no bearer token, extended=True)
# pp.pprint(kp.get_asset_utxos(["750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"], \
# ["f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a","6b6f696f732e72657374"], extended=True, content_range="0-9"))

# # Get Asset History (no bearer token)
# pp.pprint(kp.get_asset_history("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b" \
# , content_range="0-9"))

# # Get Asset History (with bearer token)
# pp.pprint(kp_token.get_asset_history("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b" \
# , content_range="0-9"))

# # Get Asset Addresses (no bearer token)
# pp.pprint(kp.get_asset_addresses("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b" \
# , content_range="0-9"))

# # Get Asset Addresses (with bearer token)
# pp.pprint(kp_token.get_asset_addresses("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b" \
# , content_range="0-9"))

# # Get Asset NFT Address (no bearer token)
# pp.pprint(kp.get_asset_nft_address("f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a", "68616e646c65"))

# # Get Asset NFT Address (with bearer token)
# pp.pprint(kp_token.get_asset_nft_address("f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a", "68616e646c65"))

# # Get Policy Asset Adress List (no bearer token)
# pp.pprint(kp.get_policy_asset_addresses("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", content_range="0-9"))

# # Get Policy Asset Adress List (with bearer token)
# pp.pprint(kp_token.get_policy_asset_addresses("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", content_range="0-9"))

# # Get Policy Asset Info (no bearer token)
# pp.pprint(kp.get_policy_asset_info("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501"))

# # Get Policy Asset Info (with bearer token)
# pp.pprint(kp_token.get_policy_asset_info("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501"))

# # Get Asset Summary (no bearer token)
# pp.pprint(kp.get_asset_summary("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b"))

# # Get Asset Summary (with bearer token)
# pp.pprint(kp_token.get_asset_summary("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b"))

# # Get Asset Transactions (no bearer token)
# pp.pprint(kp.get_asset_txs("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b", after_block=50000,\
# content_range="0-9"))

# # Get Asset Transactions (with bearer token)
# pp.pprint(kp_token.get_asset_txs("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501", "424f4f4b", after_block=50000,\
# content_range="0-9"))

##########################################################################################
# Account Endpoint Tests
##########################################################################################

# # Get Account List (no bearer token)
# pp.pprint(kp.get_account_list(content_range="0-9"))

# # Get Account List (with bearer token)
# pp.pprint(kp_token.get_account_list(content_range="0-9"))

# # Get Account Info (no bearer token)
# pp.pprint(kp.get_account_info(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"]))

# # Get Account Info (with bearer token)
# pp.pprint(kp_token.get_account_info(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"]))

# # Get Account Info Cached (no bearer token)
# pp.pprint(kp.get_account_info_cached(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"]))

# # Get Account Info Cached (with bearer token)
# pp.pprint(kp_token.get_account_info_cached(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"]))

# # Get UTxOs from Stake Addresses/Accounts (no bearer token)
# pp.pprint(kp.get_account_utxos(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"], extended=False, content_range="0-9"))

# # Get UTxOs from Stake Addresses/Accounts (with bearer token)
# pp.pprint(kp_token.get_account_utxos(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"], extended=True, content_range="0-9"))

# # Get Account Txs (no bearer token)
# pp.pprint(kp.get_account_txs("stake1u8yxtugdv63wxafy9d00nuz6hjyyp4qnggvc9a3vxh8yl0ckml2uz", after_block=50000))

# # Get Account Txs (with bearer token)
# pp.pprint(kp_token.get_account_txs("stake1u8yxtugdv63wxafy9d00nuz6hjyyp4qnggvc9a3vxh8yl0ckml2uz", after_block=50000))

# # Get Account Rewards (no bearer token)
# pp.pprint(kp.get_account_rewards(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"], epoch_no=409))

# # Get Account Rewards (with bearer token)
# pp.pprint(kp_token.get_account_rewards(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"], epoch_no=409))

# # Get Account Updates (no bearer token)
# pp.pprint(kp.get_account_updates(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"]))

# # Get Account Updates (with bearer token)
# pp.pprint(kp_token.get_account_updates(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", \
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"]))

# # Get Account Addresses (no bearer token)
# pp.pprint(kp.get_account_addresses(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", \
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"], content_range="0-9", first_only=False, 
# empty=False))

# # Get Account Addresses (with bearer token)
# pp.pprint(kp_token.get_account_addresses(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", \
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"], content_range="0-9", first_only=False,
# empty=False))

# # Get Account Assets (no bearer token)
# pp.pprint(kp.get_account_assets(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"]))

# # Get Account Assets (with bearer token)
# pp.pprint(kp_token.get_account_assets(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
# "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"]))

# # Get Account History (no bearer token)
# pp.pprint(kp.get_account_history("stake1u8yxtugdv63wxafy9d00nuz6hjyyp4qnggvc9a3vxh8yl0ckml2uz", \
# content_range="0-9", epoch_no=409))

# # Get Account History (with bearer token)
# pp.pprint(kp_token.get_account_history("stake1u8yxtugdv63wxafy9d00nuz6hjyyp4qnggvc9a3vxh8yl0ckml2uz", \
# content_range="0-9", epoch_no=409))

##########################################################################################
# Script Endpoint Tests
##########################################################################################

# # Get Script Info (no bearer token)
# pp.pprint(kp.get_script_info(["bd2119ee2bfb8c8d7c427e8af3c35d537534281e09e23013bca5b138", \
# "c0c671fba483641a71bb92d3a8b7c52c90bf1c01e2b83116ad7d4536"]))

# # Get Script Info (with bearer token)
# pp.pprint(kp_token.get_script_info(["bd2119ee2bfb8c8d7c427e8af3c35d537534281e09e23013bca5b138", \
# "c0c671fba483641a71bb92d3a8b7c52c90bf1c01e2b83116ad7d4536"]))

# # Get Native Script List (no bearer token)
# pp.pprint(kp.get_native_script_list(content_range="0-9"))

# # Get Native Script List (with bearer token)
# pp.pprint(kp_token.get_native_script_list(content_range="0-9"))

# # Get Plutus Script List (no bearer token)
# pp.pprint(kp.get_plutus_script_list(content_range="0-9"))

# # Get Plutus Script List (with bearer token)
# pp.pprint(kp_token.get_plutus_script_list(content_range="0-9"))

# # Get Script UTxOs (no bearer token)
# pp.pprint(kp.get_script_utxos(script_hash="d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8", extended=False))

# # Get Script UTxOs (with bearer token)
# pp.pprint(kp_token.get_script_utxos(script_hash="d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8", extended=True))

# # Get Script Redeemers (no bearer token)
# pp.pprint(kp.get_script_redeemers(script_hash="d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8"))

# # Get Script Redeemers (with bearer token)
# pp.pprint(kp_token.get_script_redeemers(script_hash="d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8"))

# # Get Datum Info (no bearer token)
# pp.pprint(kp.get_datum_info(["818ee3db3bbbd04f9f2ce21778cac3ac605802a4fcb00c8b3a58ee2dafc17d46", \
# "45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0"]))

# # Get Datum Info (with bearer token)
# pp.pprint(kp_token.get_datum_info(["818ee3db3bbbd04f9f2ce21778cac3ac605802a4fcb00c8b3a58ee2dafc17d46", \
# "45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0"]))

##########################################################################################
# End of Simple Testing
##########################################################################################




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
# Heavy/Large data tests
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