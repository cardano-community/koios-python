#!/usr/bin/env python
"""
TESTING SCRIPT FOR KOIOS_PYTHON USING PYTEST

Main purpose of this script is to ensure basic functionality of the koios-python library and
its features are working with the current version of the Koios REST API.

It will help test basic edge cases and ensure that the library is working as expected.

To use this script, you must have pytest installed.

You can install pytest using pip:
pip install pytest

After you have downloaded/cloned this repo and installed pytest, you can run this script
First change directory to the folder containing this repo and script then simply run the
following command in your terminal:

pytest test_koios.py


Watch the terminal for the results of the tests. :)

"""

import pytest
import koios_python

# create a new url object with your own url or use koios.rest url by default
kp = koios_python.URLs()


# START OF TESTS FOR KOIOS_PYTHON

##############################################################################
# STAKE ACCOUNT FUNCTIONS
##############################################################################

# get account list
def test_get_account_list():

    # get account list from mainnet server
    account_list_mainnet = kp.get_account_list()
    assert len(account_list_mainnet) > 0
    assert 'code' not in account_list_mainnet[0]

# get account info
def test_get_account_info():

    # get account info from mainnet server
    account_info_mainnet = kp.get_account_info("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
    if len(account_info_mainnet) > 0:
        assert 'code' not in account_info_mainnet[0]
    assert len(account_info_mainnet) > 0

# get account utxos
def test_get_account_utxos():

    account_utxos_mainnet = kp.get_account_utxos("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
    if len(account_utxos_mainnet) > 0:
        assert 'code' not in account_utxos_mainnet[0]
    assert len(account_utxos_mainnet) > 0

# get account info
def test_get_account_info_cached():

    # get account info from mainnet server
    account_info_cached_mainnet = kp.get_account_info_cached("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
    if len(account_info_cached_mainnet) > 0:
        assert 'code' not in account_info_cached_mainnet[0]
    assert len(account_info_cached_mainnet) > 0

# get account rewards
def test_get_account_rewards():

    # get account rewards from mainnet server
    account_rewards_mainnet = kp.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
    # get account rewards by epoch
    account_rewards_mainnet_epoch = kp.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", 350)
    # Check for error code in response and empty list
    if len(account_rewards_mainnet) > 0 and len(account_rewards_mainnet_epoch) > 0:
        assert 'code' not in account_rewards_mainnet[0] and 'code' not in account_rewards_mainnet_epoch[0]
    assert len(account_rewards_mainnet) > 0 and len(account_rewards_mainnet_epoch) > 0
       
# get account updates
def test_get_account_updates():

    account_updates_mainnet = kp.get_account_updates("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
    if len(account_updates_mainnet) > 0:
        assert 'code' not in account_updates_mainnet[0]
    assert len(account_updates_mainnet) > 0

# get account addresses
def get_account_addresses():

    account_addresses_mainnet = kp.get_account_updates(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",\
                                                        "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"])
    if len(account_addresses_mainnet) > 0:
        assert 'code' not in account_addresses_mainnet[0]
    assert len(account_addresses_mainnet) > 0

# get account assets
def test_get_account_assets():

    account_assets_mainnet = kp.get_account_assets("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
    if len(account_assets_mainnet) > 0:
        assert 'code' not in account_assets_mainnet[0]

# get account history
def test_get_account_history():

    account_history_mainnet = kp.get_account_history(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
                                                                        "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"])
    if len(account_history_mainnet) > 0:
        assert 'code' not in account_history_mainnet[0]


##############################################################################
# ADDRESS FUNCTIONS
##############################################################################

# get address info
def test_get_address_info():

    address_info_mainnet = kp.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
    if len(address_info_mainnet) > 0:
        assert 'code' not in address_info_mainnet[0]

# get address transactions
def test_get_address_transactions():

    address_txs_mainnet = kp.get_address_txs(["addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",
                                                                        "addr1qyfldpcvte8nkfpyv0jdc8e026cz5qedx7tajvupdu2724tlj8sypsq6p90hl40ya97xamkm9fwsppus2ru8zf6j8g9sm578cu"])
    if len(address_txs_mainnet) > 0:
        assert 'code' not in address_txs_mainnet[0]
    
    address_txs_after_block = kp.get_address_txs("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",1)
    if len(address_txs_after_block) > 0:
        assert 'code' not in address_txs_after_block[0]

# get address assets 
def test_get_address_assets():
     
    address_assets_mainnet = kp.get_address_assets("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
    if len(address_assets_mainnet) >0:
        assert 'code' not in address_assets_mainnet[0]

# Get a list of UTxO against input payment credential  
def test_get_credential_utxos():

    credentials_utxos_mainnet = kp.get_credential_utxos(["025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52",\
                                                      "13f6870c5e4f3b242463e4dc1f2f56b02a032d3797d933816f15e555"])
    if len(credentials_utxos_mainnet) > 0:
        assert 'code' not in credentials_utxos_mainnet[0]

# get payment credentials hash
def test_get_credentials():

    credentials_mainnet = kp.get_credential_txs('025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52')
    if len(credentials_mainnet) > 0:
        assert 'code' not in credentials_mainnet[0]
    
    credentials_after_block = kp.get_credential_txs('025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52',6238675)
    if len(credentials_after_block) > 0:
        assert 'code' not in credentials_after_block[0]


##############################################################################
# ASSET FUNCTIONS
##############################################################################

# get asset list of all native tokens
def test_get_asset_list():

    asset_list_mainnet = kp.get_asset_list()
    if len(asset_list_mainnet) > 0:
        assert 'code' not in asset_list_mainnet[0]

# get asset address list
def test_get_asset_address_list():

    asset_addr_list_mainnet = kp.get_asset_addresses("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
    if len(asset_addr_list_mainnet) > 0:
        assert 'code' not in asset_addr_list_mainnet[0]

# get asset address nft address
def test_get_asset_nft_address():

    asset_nft_address_mainnet = kp.get_asset_nft_address("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
    if len(asset_nft_address_mainnet) > 0:
        assert 'code' not in asset_nft_address_mainnet[0]

# get asset info
def test_get_asset_info():
        
        asset_info_mainnet = kp.get_asset_info("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
        if len(asset_info_mainnet) > 0:
            assert 'code' not in asset_info_mainnet[0]

# get asset info list of assets (bulk)
def test_get_asset_info_bulk():

    asset_info_bulk_mainnet = kp.get_asset_info_bulk([["750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"],["1d7f33bd23d85e1a25d87d86fac4f199c3197a2f7afeb662a0f34e1e","776f726c646d6f62696c65746f6b656e"]])
    if len(asset_info_bulk_mainnet) > 0:
        assert 'code' not in asset_info_bulk_mainnet[0]

    asset_info_bulk_mainnet = kp.get_asset_info_bulk([["750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b"]])
    if len(asset_info_bulk_mainnet) > 0:
        assert 'code' not in asset_info_bulk_mainnet[0]

# get asset history
def test_get_asset_history():

    asset_history_mainnet = kp.get_asset_history("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
    if len(asset_history_mainnet) > 0:
        assert 'code' not in asset_history_mainnet[0]

# get policy asset addresses
def test_get_policy_asset_addresses():

    asset_policy_asset_addresses_mainnet = kp.get_policy_asset_addresses("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501")
    if len(asset_policy_asset_addresses_mainnet) > 0:
        assert 'code' not in asset_policy_asset_addresses_mainnet[0]

# get policy asset information
def test_get_policy_asset_info():

    asset_policy_asset_info_mainnet = kp.get_policy_asset_addresses("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501")
    if len(asset_policy_asset_info_mainnet) > 0:
        assert 'code' not in asset_policy_asset_info_mainnet[0]

def test_get_policy_asset_list():

    asset_policy_asset_list_mainnet = kp.get_policy_asset_addresses("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501")
    if len(asset_policy_asset_list_mainnet) > 0:
        assert 'code' not in asset_policy_asset_list_mainnet[0]

# get asset summary
def test_get_asset_summary():

    asset_summary_mainnet = kp.get_asset_summary('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', '424f4f4b')
    if len(asset_summary_mainnet) > 0:
        assert 'code' not in asset_summary_mainnet[0]
        
# get asset transaction history
def test_get_asset_txs_history():

    asset_txs_history_mainnet = kp.get_asset_txs('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
    if len(asset_txs_history_mainnet) > 0:
        assert 'code' not in asset_txs_history_mainnet[0]


##############################################################################
# BLOCK FUNCTIONS
##############################################################################

# get list of blocks
def test_get_blocks():

        blocks_mainnet_server = kp.get_blocks()
        assert 'code' not in blocks_mainnet_server[0]

# get block info
def test_get_block_info():

    block_info_mainnet = kp.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30",
                                                            "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a",
                                                            "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"])
    if len(block_info_mainnet) > 0:
        assert 'code' not in block_info_mainnet[0]

# get block transactions
def test_get_block_txs():

    block_txs_mainnet = kp.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30"])
    if len(block_txs_mainnet) > 0:
        assert 'code' not in block_txs_mainnet[0]


##############################################################################
# EPOCH FUNCTIONS
##############################################################################

# get epoch info
def test_get_epoch_info():

    epoch_info_mainnet = kp.get_epoch_info()
    assert 'code' not in epoch_info_mainnet[0]

# get epoch params
def test_get_epoch_params():

    epoch_params_mainnet = kp.get_epoch_params()
    assert 'code' not in epoch_params_mainnet[0]

def test_get_epoch_block_protocols():

    epoch_block_protocols_mainnet = kp.get_epoch_block_protocols()
    assert 'code' not in epoch_block_protocols_mainnet[0]


##############################################################################
# NETWORK FUNCTIONS
##############################################################################

# check tip
def test_get_tip():

    tip_mainnet = kp.get_tip()
    assert 'code' not in tip_mainnet[0]

# check genesis info
def test_get_genesis():

    genesis_mainnet = kp.get_genesis()
    assert 'code' not in genesis_mainnet[0]

def test_get_totals():

    epoch_totals_mainnet = kp.get_totals()
    assert 'code' not in epoch_totals_mainnet[0]


##############################################################################
# POOL FUNCTIONS
##############################################################################

# get list of pools on the network
def test_get_pool_list():

    pool_list_mainnet = kp.get_pool_list()
    pool_list_mainnet_range = kp.get_pool_list('0-10')
    if len(pool_list_mainnet) > 0 and len(pool_list_mainnet_range) > 0:
        assert 'code' not in pool_list_mainnet[0] and 'code' not in pool_list_mainnet_range[0]

# get pool info
def test_get_pool_info():

    pool_info_mainnet = kp.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp",
                                                            "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m",
                                                            "pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"])
    if len(pool_info_mainnet) > 0:
        assert 'code' not in pool_info_mainnet[0]
    assert 'code' not in pool_info_mainnet[0]

# get pool stake snapshot
def test_get_pool_stake_snapshot():

    stake_snapshot_mainnet = kp.get_pool_stake_snapshot("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
    if len(stake_snapshot_mainnet) > 0:
        assert 'code' not in stake_snapshot_mainnet[0]

# get pool delegator information
def test_get_pool_delegators():
        
    delegator_info_mainnet = kp.get_pool_delegators("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
    if len(delegator_info_mainnet) > 0:
        assert 'code' not in delegator_info_mainnet[0]

# get pool delegator history
def test_get_pool_delegators_history():

    delegator_history_mainnet = kp.get_pool_delegators_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
    if len(delegator_history_mainnet) > 0:
        assert 'code' not in delegator_history_mainnet[0]

# get pool blocks
def test_get_pool_blocks():

    pool_blocks_mainnet = kp.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
    pool_blocks_mainnet_epoch = kp.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 350)
    if len(pool_blocks_mainnet) > 0 and len(pool_blocks_mainnet_epoch) > 0:
        assert 'code' not in pool_blocks_mainnet[0] and 'code' not in pool_blocks_mainnet_epoch[0]

# get pool history
def test_get_pool_history():

    pool_history_mainnet = kp.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
    pool_history_mainnet_epoch = kp.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 350)
    if len(pool_history_mainnet) > 0 and len(pool_history_mainnet_epoch) > 0:
        assert 'code' not in pool_history_mainnet[0] and 'code' not in pool_history_mainnet_epoch[0]

# get pool updates
def test_get_pool_updates():
   
    pool_updates_mainnet = kp.get_pool_updates()
    pool_updates_mainnet_pool = kp.get_pool_updates("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
    if len(pool_updates_mainnet) > 0 and len(pool_updates_mainnet_pool) > 0:
        assert 'code' not in pool_updates_mainnet[0] and 'code' not in pool_updates_mainnet_pool[0]

# get pool relays
def test_get_pool_relays():

    pool_relays_mainnet = kp.get_pool_relays()
    pool_relays_mainnet_range = kp.get_pool_relays('0-70')
    if len(pool_relays_mainnet) > 0 and len(pool_relays_mainnet_range) > 0:
        assert 'code' not in pool_relays_mainnet[0] and 'code' not in pool_relays_mainnet_range[0]

# get pool metadata
def test_get_pool_metadata():

    pool_metadata_mainnet = kp.get_pool_metadata()
    pool_metadata_mainnet_pool = kp.get_pool_metadata("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
    pool_metadata_mainnet_pool_list = kp.get_pool_metadata(["pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 
                                                                            "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m"])
    if len(pool_metadata_mainnet) > 0 and len(pool_metadata_mainnet_pool) > 0 and len(pool_metadata_mainnet_pool_list) > 0:
        assert 'code' not in pool_metadata_mainnet[0] and 'code' not in pool_metadata_mainnet_pool[0] and 'code' not in pool_metadata_mainnet_pool_list[0]


##############################################################################
# SCRIPT FUNCTIONS
##############################################################################

# get list of native scripts on the network
def test_get_native_script_list():

    script_list_mainnet = kp.get_native_script_list()
    script_list_mainnet_range = kp.get_native_script_list('0-10')
    if len(script_list_mainnet) > 0 and len(script_list_mainnet_range) > 0:
        assert 'code' not in script_list_mainnet[0] and 'code' not in script_list_mainnet_range[0]

# get plutus script list
def test_get_plutus_script_list():

    script_list_mainnet = kp.get_plutus_script_list()
    script_list_mainnet_range = kp.get_plutus_script_list('0-10')
    if len(script_list_mainnet) > 0 and len(script_list_mainnet_range) > 0:
        assert 'code' not in script_list_mainnet[0] and 'code' not in script_list_mainnet_range[0]

# get list of all redeemers for a given script hash
def test_get_script_redeemers():

    script_redeemers_mainnet = kp.get_script_redeemers('d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8')
    if len(script_redeemers_mainnet) > 0:
        assert 'code' not in script_redeemers_mainnet[0]

def test_get_datum_info():

    datum_info = kp.get_datum_info('818ee3db3bbbd04f9f2ce21778cac3ac605802a4fcb00c8b3a58ee2dafc17d46',
    "45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0")
    if len(datum_info) > 0:
        assert 'code' not in datum_info[0]


##############################################################################
# TRANSACTION FUNCTIONS
##############################################################################

# get transaction(s) info
def test_tx_info():
 
    tx_info_mainnet = kp.get_tx_info('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
    tx_info_mainnet_list = kp.get_tx_info(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                            'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
    if len(tx_info_mainnet) > 0 and len(tx_info_mainnet_list) > 0:
        assert 'code' not in tx_info_mainnet[0] and 'code' not in tx_info_mainnet_list[0]

# get transaction(s) utxos
def test_get_tx_utxos():

    tx_utxo_mainnet = kp.get_tx_utxos('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
    tx_utxo_mainnet_list = kp.get_tx_utxos(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                            'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
    if len(tx_utxo_mainnet) > 0 and len(tx_utxo_mainnet_list) > 0:
        assert 'code' not in tx_utxo_mainnet[0] and 'code' not in tx_utxo_mainnet_list[0]

# get transaction(s) metadata
def test_get_tx_metadata():

    tx_metadata_mainnet = kp.get_tx_metadata('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
    tx_metadata_mainnet_list = kp.get_tx_metadata(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                    'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
    if len(tx_metadata_mainnet) > 0 and len(tx_metadata_mainnet_list) > 0:
        assert 'code' not in tx_metadata_mainnet[0] and 'code' not in tx_metadata_mainnet_list[0]

# get transaction(s) metadata labels
def test_get_tx_metalabels():
                
    tx_metalables_mainnet = kp.get_tx_metalabels('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
    tx_metalables_mainnet_list = kp.get_tx_metalabels(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                        'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
    if len(tx_metalables_mainnet) > 0 and len(tx_metalables_mainnet_list) > 0:
        assert 'code' not in tx_metalables_mainnet[0] and 'code' not in tx_metalables_mainnet_list[0]

# # NOT FINISHED
# # submit_tx signed cbor
# # def test_submit_tx():
	
# # 	tx_submit = koios_python.submit_tx("file")
# # 	assert 'code' not in tx_submit[0]

# get tx status
def test_get_tx_status():

    tx_status_mainnet = kp.get_tx_status('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
    tx_status_mainnet_list = kp.get_tx_status(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
    if len(tx_status_mainnet) > 0 and len(tx_status_mainnet_list) > 0:
        assert 'code' not in tx_status_mainnet[0] and 'code' not in tx_status_mainnet_list[0]

