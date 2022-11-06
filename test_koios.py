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
import koios_python as kp

# create a new url object with your own url or use koios.rest url by default
kp_mainnet_server = kp.URLs()

kp_custom_server = kp.URLs(url="https://koios-otg.tosidrop.io/api/v0/")

# Koios server switching to testnet default is mainnet and this feature only works for standard Koios rest api server api.koios.rest/api/v0
kp_testnet_server = kp.URLs( network='testnet')


# START OF TESTS FOR KOIOS_PYTHON
##############################################################################
def test_check_custom_url():
        # check if custom url is working
        assert kp_custom_server.url == "https://koios-otg.tosidrop.io/api/v0/"




# test network switching by trying to switch back to mainnet
def test_network_switch():
        
        kp_test = kp.URLs(network='testnet')
        genesis_info_testnet = kp_test.get_genesis()
        # check if we are on testnet
        assert genesis_info_testnet[0]['networkid'] == 'Testnet'
        # switch back to mainnet
        kp_test = kp.URLs(network='mainnet')
        genesis_info_mainnet = kp_test.get_genesis()
        # check if we are on mainnet
        assert genesis_info_mainnet[0]['networkid'] == 'Mainnet'


##############################################################################
# ACCOUNT FUNCTIONS

# get account list
def test_get_account_list():
        # get account list from custom server
        account_list_custom = kp_custom_server.get_account_list()
        # check if we got a non empty list
        assert len(account_list_custom) > 0
        # Check for error code in response
        assert 'code' not in account_list_custom[0]
        
        # get account list from mainnet server
        account_list_mainnet = kp_mainnet_server.get_account_list()
        assert len(account_list_mainnet) > 0
        assert 'code' not in account_list_mainnet[0]
        
        # get account list from testnet server
        account_list_testnet = kp_testnet_server.get_account_list()
        assert len(account_list_testnet) > 0
        assert 'code' not in account_list_testnet[0]

# get account info
def test_get_account_info():
        # get account info from custom server
        account_info_custom = kp_custom_server.get_account_info("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        if len(account_info_custom) > 0:
                assert 'code' not in account_info_custom[0]
        assert len(account_info_custom) > 0
        
        # get account info from mainnet server
        account_info_mainnet = kp_mainnet_server.get_account_info("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        if len(account_info_mainnet) > 0:
                assert 'code' not in account_info_mainnet[0]
        assert len(account_info_mainnet) > 0
        
        # get account info from testnet server
        account_info_testnet = kp_testnet_server.get_account_info("stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj")
        if len(account_info_testnet) > 0:
                assert 'code' not in account_info_testnet[0]
        assert len(account_info_testnet) > 0

# get account rewards
def test_get_account_rewards():
        # get account rewards from custom server
        account_rewards_custom = kp_custom_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        # get account rewards by epoch
        account_rewards_custom_epoch = kp_custom_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", 350)
        # Check for error code in response and empty list
        if len(account_rewards_custom) > 0 and len(account_rewards_custom_epoch) > 0:
                assert 'code' not in account_rewards_custom[0] and 'code' not in account_rewards_custom_epoch[0]
        assert len(account_rewards_custom) > 0 and len(account_rewards_custom_epoch) > 0

        # get account rewards from mainnet server
        account_rewards_mainnet = kp_mainnet_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        # get account rewards by epoch
        account_rewards_mainnet_epoch = kp_mainnet_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", 350)
        # Check for error code in response and empty list
        if len(account_rewards_mainnet) > 0 and len(account_rewards_mainnet_epoch) > 0:
                assert 'code' not in account_rewards_mainnet[0] and 'code' not in account_rewards_mainnet_epoch[0]
        assert len(account_rewards_mainnet) > 0 and len(account_rewards_mainnet_epoch) > 0
        
        # get account rewards from testnet server
        account_rewards_testnet = kp_testnet_server.get_account_rewards("stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj")
        # get account rewards by epoch
        account_rewards_testnet_epoch = kp_testnet_server.get_account_rewards("stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj", 200)
        # Check for error code in response and empty list
        if len(account_rewards_testnet) > 0 and len(account_rewards_testnet_epoch) > 0:
                assert 'code' not in account_rewards_testnet[0] and 'code' not in account_rewards_testnet_epoch[0]
       
# get account updates
def test_get_account_updates():

        account_updates_custom = kp_custom_server.get_account_updates("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        if len(account_updates_custom) > 0:
                assert 'code' not in account_updates_custom[0]
        assert len(account_updates_custom) > 0
        
        account_updates_mainnet = kp_mainnet_server.get_account_updates("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        if len(account_updates_mainnet) > 0:
                assert 'code' not in account_updates_mainnet[0]
        assert len(account_updates_mainnet) > 0
                
        account_updates_testnet = kp_testnet_server.get_account_updates("stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj")
        if len(account_updates_testnet) > 0:
                assert 'code' not in account_updates_testnet[0]
        
# get account assets
def test_get_account_assets():

        account_assets_custom = kp_custom_server.get_account_assets("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        if len(account_assets_custom) > 0:
                assert 'code' not in account_assets_custom[0]
        
        account_assets_mainnet = kp_mainnet_server.get_account_assets("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        if len(account_assets_mainnet) > 0:
                assert 'code' not in account_assets_mainnet[0]
        
        account_assets_testnet = kp_testnet_server.get_account_assets(["stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj",
                                                                       "stake_test1uq7g7kqeucnqfweqzgxk3dw34e8zg4swnc7nagysug2mm4cm77jrx"])
        if len(account_assets_testnet) > 0:
                assert 'code' not in account_assets_testnet[0]


        
# get account history
def test_get_account_history():

        account_history_custom = kp_custom_server.get_account_history(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
                                                                       "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"])
        if len(account_history_custom) > 0:
                assert 'code' not in account_history_custom[0]
        
        account_history_mainnet = kp_mainnet_server.get_account_history(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
                                                                         "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"])
        if len(account_history_mainnet) > 0:
                assert 'code' not in account_history_mainnet[0]
        
        account_history_testnet = kp_testnet_server.get_account_history(["stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj",
                                                                         "stake_test1uq7g7kqeucnqfweqzgxk3dw34e8zg4swnc7nagysug2mm4cm77jrx"])
        if len(account_history_testnet) > 0:
                assert 'code' not in account_history_testnet[0]

##############################################################################
# ADDRESS FUNCTIONS

# get address info
def test_get_address_info():

        address_info_custom = kp_custom_server.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_info_custom) > 0:
                assert 'code' not in address_info_custom[0]
        
        address_info_mainnet = kp_mainnet_server.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_info_mainnet) > 0:
                assert 'code' not in address_info_mainnet[0]
        
        address_info_testnet = kp_testnet_server.get_address_info("addr_test1qzx9hu8j4ah3auytk0mwcupd69hpc52t0cw39a65ndrah86djs784u92a3m5w475w3w35tyd6v3qumkze80j8a6h5tuqq5xe8y")
        if len(address_info_testnet) > 0:
                assert 'code' not in address_info_testnet[0]

# get address transactions
def test_get_address_transactions():

        address_txs_custom = kp_custom_server.get_address_txs(["addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",
                                                                        "addr1qyfldpcvte8nkfpyv0jdc8e026cz5qedx7tajvupdu2724tlj8sypsq6p90hl40ya97xamkm9fwsppus2ru8zf6j8g9sm578cu"])
        if len(address_txs_custom) > 0:
                assert 'code' not in address_txs_custom[0]
         
        address_txs_mainnet = kp_mainnet_server.get_address_txs(["addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",
                                                                          "addr1qyfldpcvte8nkfpyv0jdc8e026cz5qedx7tajvupdu2724tlj8sypsq6p90hl40ya97xamkm9fwsppus2ru8zf6j8g9sm578cu"])
        if len(address_txs_mainnet) > 0:
                assert 'code' not in address_txs_mainnet[0]
        
        address_txs_testnet = kp_testnet_server.get_address_txs(["addr_test1qzx9hu8j4ah3auytk0mwcupd69hpc52t0cw39a65ndrah86djs784u92a3m5w475w3w35tyd6v3qumkze80j8a6h5tuqq5xe8y",
                                                                          "addr_test1qrk7920v35zukhcch4kyydy6rxnhqdcvetkvngeqrvtgavw8tpzdklse3kwer7urhrlfg962m9fc8cznfcdpka5pd07sgf8n0w"])
        if len(address_txs_testnet) > 0:
                assert 'code' not in address_txs_testnet[0]
        
        address_txs_after_block = kp_mainnet_server.get_address_txs("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",1)
        if len(address_txs_after_block) > 0:
                assert 'code' not in address_txs_after_block[0]

# get address assets 
def test_get_address_assets():

        address_assets_custom = kp_custom_server.get_address_assets("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_assets_custom) >0:
                assert 'code' not in address_assets_custom[0]
                
        address_assets_mainnet = kp_mainnet_server.get_address_assets("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_assets_mainnet) >0:
                assert 'code' not in address_assets_mainnet[0]
        
        address_assets_testnet = kp_testnet_server.get_address_assets("addr_test1qrk7920v35zukhcch4kyydy6rxnhqdcvetkvngeqrvtgavw8tpzdklse3kwer7urhrlfg962m9fc8cznfcdpka5pd07sgf8n0w")
        if len(address_assets_testnet) >0:
                assert 'code' not in address_assets_testnet[0]

# get payment credentials hash
def test_get_credentials():

        credentials_custom = kp_custom_server.get_credential_txs("025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52")
        if len(credentials_custom) > 0:
                assert 'code' not in credentials_custom[0]
        
        credentials_mainnet = kp_mainnet_server.get_credential_txs('025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52')
        if len(credentials_mainnet) > 0:
                assert 'code' not in credentials_mainnet[0]
        
        credentials_testnet = kp_testnet_server.get_credential_txs('00003fac863dc2267d0cd90768c4af653572d719a79ca3b01957fa79')
        if len(credentials_testnet) > 0:
                assert 'code' not in credentials_testnet[0]
        
        credentials_after_block = kp_mainnet_server.get_credential_txs('025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52',6238675)
        if len(credentials_after_block) > 0:
                assert 'code' not in credentials_after_block[0]

        credentials_after_block_testnet = kp_testnet_server.get_credential_txs('00003fac863dc2267d0cd90768c4af653572d719a79ca3b01957fa79',2342661)
        if len(credentials_after_block_testnet) > 0:
                assert 'code' not in credentials_after_block_testnet[0]

##############################################################################
# ASSET FUNCTIONS

# get asset list of all native tokens
def test_get_asset_list():

        asset_list_custom = kp_custom_server.get_asset_list()
        if len(asset_list_custom) > 0:
                assert 'code' not in asset_list_custom[0]
        
        asset_list_mainnet = kp_mainnet_server.get_asset_list()
        if len(asset_list_mainnet) > 0:
                assert 'code' not in asset_list_mainnet[0]
        
        asset_list_testnet = kp_testnet_server.get_asset_list()
        if len(asset_list_testnet) > 0:
                assert 'code' not in asset_list_testnet[0]


# get asset address list
def test_get_asset_address_list():

        asset_addr_list_custom = kp_custom_server.get_asset_address_list("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
        if len(asset_addr_list_custom) > 0:
                assert 'code' not in asset_addr_list_custom[0]
        
        asset_addr_list_mainnet = kp_mainnet_server.get_asset_address_list("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
        if len(asset_addr_list_mainnet) > 0:
                assert 'code' not in asset_addr_list_mainnet[0]
        
        asset_addr_list_testnet = kp_testnet_server.get_asset_address_list("000327a9e427a3a3256eb6212ae26b7f53f7969b8e62d37ea9138a7b",54735465737431)
        if len(asset_addr_list_testnet) > 0:
                assert 'code' not in asset_addr_list_testnet[0]
        

# get asset info
def test_get_asset_info():

        asset_info_custom = kp_custom_server.get_asset_info("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
        if len(asset_info_custom) > 0:
                assert 'code' not in asset_info_custom[0]
        
        asset_info_mainnet = kp_mainnet_server.get_asset_info("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
        if len(asset_info_mainnet) > 0:
                assert 'code' not in asset_info_mainnet[0]
        
        asset_info_testnet = kp_testnet_server.get_asset_info("000327a9e427a3a3256eb6212ae26b7f53f7969b8e62d37ea9138a7b",54735465737431)
        if len(asset_info_testnet) > 0:
                assert 'code' not in asset_info_testnet[0]
        
# get asset history
def test_get_asset_history():

        asset_history_custom = kp_custom_server.get_asset_history("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
        if len(asset_history_custom) > 0:
                assert 'code' not in asset_history_custom[0]
        
        asset_history_mainnet = kp_mainnet_server.get_asset_history("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
        if len(asset_history_mainnet) > 0:
                assert 'code' not in asset_history_mainnet[0]
        
        asset_history_testnet = kp_testnet_server.get_asset_history("000327a9e427a3a3256eb6212ae26b7f53f7969b8e62d37ea9138a7b",54735465737431)
        if len(asset_history_testnet) > 0:
                assert 'code' not in asset_history_testnet[0]

# get asset policy info
def test_get_asset_policy_info():

        asset_policy_info_custom = kp_custom_server.get_asset_policy_info("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501")
        if len(asset_policy_info_custom) > 0:
                assert 'code' not in asset_policy_info_custom[0]
                
        
        asset_policy_info_mainnet = kp_mainnet_server.get_asset_policy_info("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501")
        if len(asset_policy_info_mainnet) > 0:
                assert 'code' not in asset_policy_info_mainnet[0]
        
        asset_policy_info_testnet = kp_testnet_server.get_asset_policy_info("000327a9e427a3a3256eb6212ae26b7f53f7969b8e62d37ea9138a7b")
        if len(asset_policy_info_testnet) > 0:
                assert 'code' not in asset_policy_info_testnet[0]
        
# get asset summary
def test_get_asset_summary():

        asset_summary_custom = kp_custom_server.get_asset_summary("750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501","424f4f4b")
        if len(asset_summary_custom) > 0:
                assert 'code' not in asset_summary_custom[0]        
        
        asset_summary_mainnet = kp_mainnet_server.get_asset_summary('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', '424f4f4b')
        if len(asset_summary_mainnet) > 0:
                assert 'code' not in asset_summary_mainnet[0]

        asset_summary_testnet = kp_testnet_server.get_asset_summary("000327a9e427a3a3256eb6212ae26b7f53f7969b8e62d37ea9138a7b",54735465737431)
        if len(asset_summary_testnet) > 0:
                assert 'code' not in asset_summary_testnet[0]

# get asset transaction history
def test_get_asset_txs_history():

        asset_txs_history_custom = kp_custom_server.get_asset_txs('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
        if len(asset_txs_history_custom) > 0:
                assert 'code' not in asset_txs_history_custom[0]
                
        asset_txs_history_mainnet = kp_mainnet_server.get_asset_txs('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
        if len(asset_txs_history_mainnet) > 0:
                assert 'code' not in asset_txs_history_mainnet[0]
        
        asset_txs_history_testnet = kp_testnet_server.get_asset_txs('000327a9e427a3a3256eb6212ae26b7f53f7969b8e62d37ea9138a7b',54735465737431)
        if len(asset_txs_history_testnet) > 0:
                assert 'code' not in asset_txs_history_testnet[0]

##############################################################################

# BLOCK FUNCTIONS

# get list of blocks
def test_get_blocks():
        
        blocks_custom_server = kp_custom_server.get_blocks()
        assert 'code' not in blocks_custom_server[0]
        
        blocks_mainnet_server = kp_mainnet_server.get_blocks()
        assert 'code' not in blocks_mainnet_server[0]
        
        blocks_testnet_server = kp_testnet_server.get_blocks()
        assert 'code' not in blocks_testnet_server[0]
        
# get block info
def test_get_block_info():
        
        block_info_custom = kp_custom_server.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30",
    						"60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a",
    						"c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"])
        if len(block_info_custom) > 0:
                assert 'code' not in block_info_custom[0]

        block_info_mainnet = kp_mainnet_server.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30",
                                                               "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a",
                                                               "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"])
        if len(block_info_mainnet) > 0:
                assert 'code' not in block_info_mainnet[0]
        
        block_info_testnet = kp_testnet_server.get_block_info(["f75fea40852ed7d7f539d008e45255725daef8553ae7162750836f279570813a",
                                                               "ff9f0c7fb1136de2cd6f10c9a140af2887f1d3614cc949bfeb262266d4c202b7",
                                                               "5ef645ee519cde94a82f0aa880048c37978374f248f11e408ac0571a9054d9d3"])
        if len(block_info_testnet) > 0:
                assert 'code' not in block_info_testnet[0]


# get block transactions
def test_get_block_txs():
        
        block_txs_custom = kp_custom_server.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30"])
        if len(block_txs_custom) > 0:
                assert 'code' not in block_txs_custom[0]
        
        block_txs_mainnet = kp_mainnet_server.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30"])
        if len(block_txs_mainnet) > 0:
                assert 'code' not in block_txs_mainnet[0]
        
        block_txs_testnet = kp_testnet_server.get_block_txs(["f75fea40852ed7d7f539d008e45255725daef8553ae7162750836f279570813a",
                                                             "ff9f0c7fb1136de2cd6f10c9a140af2887f1d3614cc949bfeb262266d4c202b7",
                                                             "5ef645ee519cde94a82f0aa880048c37978374f248f11e408ac0571a9054d9d3"])
        if len(block_txs_testnet) > 0:
                assert 'code' not in block_txs_testnet[0]

##############################################################################
# EPOCH FUNCTIONS

# get epoch info
def test_get_epoch_info():
        
        epoch_info_custom = kp_custom_server.get_epoch_info()
        assert 'code' not in epoch_info_custom[0]

        epoch_info_mainnet = kp_mainnet_server.get_epoch_info()
        assert 'code' not in epoch_info_mainnet[0]
        
        epoch_info_testnet = kp_testnet_server.get_epoch_info()
        assert 'code' not in epoch_info_testnet[0]
 
# get epoch params
def test_get_epoch_params():
        
        epoch_params_custom = kp_custom_server.get_epoch_params()
        assert 'code' not in epoch_params_custom[0]
        
        epoch_params_mainnet = kp_mainnet_server.get_epoch_params()
        assert 'code' not in epoch_params_mainnet[0]
        
        epoch_params_testnet = kp_testnet_server.get_epoch_params()
        assert 'code' not in epoch_params_testnet[0]



##############################################################################
# NETWORK FUNCTIONS

# check tip
def test_get_tip():
        
        tip_custom = kp_custom_server.get_tip()
        assert 'code' not in tip_custom[0]
        
        tip_mainnet = kp_mainnet_server.get_tip()
        assert 'code' not in tip_mainnet[0]
        
        tip_testnet = kp_testnet_server.get_tip()
        assert 'code' not in tip_testnet[0]
        
        
# check genesis info
def test_get_genesis():
        
        genesis_custom = kp_custom_server.get_genesis()
        assert 'code' not in genesis_custom[0]
        
        genesis_mainnet = kp_mainnet_server.get_genesis()
        assert 'code' not in genesis_mainnet[0]
        
        genesis_testnet = kp_testnet_server.get_genesis()
        assert 'code' not in genesis_testnet[0]
        
def test_get_totals():
        
        epoch_totals_custom = kp_custom_server.get_totals()
        assert 'code' not in epoch_totals_custom[0]
        
        epoch_totals_mainnet = kp_mainnet_server.get_totals()
        assert 'code' not in epoch_totals_mainnet[0]
        
        epoch_totals_testnet = kp_testnet_server.get_totals()
        assert 'code' not in epoch_totals_testnet[0]

##############################################################################
# POOL FUNCTIONS

# get list of pools on the network
def test_get_pool_list():

        pool_list_custom = kp_custom_server.get_pool_list()
        pool_list_custom_range = kp_custom_server.get_pool_list('0-10')
        if len(pool_list_custom) > 0 and len(pool_list_custom_range) > 0:
                assert 'code' not in pool_list_custom[0] and 'code' not in pool_list_custom_range[0]
                
        pool_list_mainnet = kp_mainnet_server.get_pool_list()
        pool_list_mainnet_range = kp_mainnet_server.get_pool_list('0-10')
        if len(pool_list_mainnet) > 0 and len(pool_list_mainnet_range) > 0:
                assert 'code' not in pool_list_mainnet[0] and 'code' not in pool_list_mainnet_range[0]
                
        pool_list_testnet = kp_testnet_server.get_pool_list()
        pool_list_testnet_range = kp_testnet_server.get_pool_list('0-10')
        if len(pool_list_testnet) > 0 and len(pool_list_testnet_range) > 0:
                assert 'code' not in pool_list_testnet[0] and 'code' not in pool_list_testnet_range[0]

 
# get pool info
def test_get_pool_info():

        pool_info_custom = kp_custom_server.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp",
    						"pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m",
    						"pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"])
        if len(pool_info_custom) > 0:
                assert 'code' not in pool_info_custom[0]
        
        pool_info_mainnet = kp_mainnet_server.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp",
                                                             "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m",
                                                             "pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"])
        if len(pool_info_mainnet) > 0:
                assert 'code' not in pool_info_mainnet[0]
        assert 'code' not in pool_info_mainnet[0]
        
        pool_info_testnet = kp_testnet_server.get_pool_info(["pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh",
                                                             "pool102x86jz7uus6p6mlw02fdw2s805kng7g6ujs6s342t5msk36tch",
                                                             "pool103qt58f9xlsr7y9anz3lnyq6cph4xh2yr4qrrtc356ldzz6ktqz"])
        if len(pool_info_testnet) > 0:
                assert 'code' not in pool_info_testnet[0]
        
        
# get pool stake snapshot
def test_get_pool_stake_snapshot():

        # stake_snapshot_custom = kp_custom_server.get_pool_stake_snapshot("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        # if len(stake_snapshot_custom) > 0:
        #         assert 'code' not in stake_snapshot_custom[0]
        
        stake_snapshot_mainnet = kp_mainnet_server.get_pool_stake_snapshot("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        if len(stake_snapshot_mainnet) > 0:
                assert 'code' not in stake_snapshot_mainnet[0]
        
        stake_snapshot_testnet = kp_testnet_server.get_pool_stake_snapshot("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh")
        if len(stake_snapshot_testnet) > 0:
                assert 'code' not in stake_snapshot_testnet[0]

# get pool delegator information
def test_get_pool_delegators():

        delegator_info_custom = kp_custom_server.get_pool_delegators("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        if len(delegator_info_custom) > 0:
                assert 'code' not in delegator_info_custom[0]
        
        delegator_info_mainnet = kp_mainnet_server.get_pool_delegators("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        if len(delegator_info_mainnet) > 0:
                assert 'code' not in delegator_info_mainnet[0]
                
        delegator_info_testnet = kp_testnet_server.get_pool_delegators("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh")
        if len(delegator_info_testnet) > 0:
                assert 'code' not in delegator_info_testnet[0]

        
# get pool delegator history
def test_get_pool_delegators_history():

        delegator_history_custom = kp_custom_server.get_pool_delegators_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        if len(delegator_history_custom) > 0:
                assert 'code' not in delegator_history_custom[0]
                
        delegator_history_mainnet = kp_mainnet_server.get_pool_delegators_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        if len(delegator_history_mainnet) > 0:
                assert 'code' not in delegator_history_mainnet[0]
        
        delegator_history_testnet = kp_testnet_server.get_pool_delegators_history("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh")
        if len(delegator_history_testnet) > 0:
                assert 'code' not in delegator_history_testnet[0]

# get pool blocks
def test_get_pool_blocks():

        pool_blocks_custom = kp_custom_server.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        pool_blocks_epoch_custom = kp_custom_server.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 350)
        if len(pool_blocks_custom) > 0 and len(pool_blocks_epoch_custom) > 0:
                assert 'code' not in pool_blocks_custom[0] and 'code' not in pool_blocks_epoch_custom[0]
        
        pool_blocks_mainnet = kp_mainnet_server.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        pool_blocks_mainnet_epoch = kp_mainnet_server.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 350)
        if len(pool_blocks_mainnet) > 0 and len(pool_blocks_mainnet_epoch) > 0:
                assert 'code' not in pool_blocks_mainnet[0] and 'code' not in pool_blocks_mainnet_epoch[0]
        
        pool_blocks_testnet = kp_testnet_server.get_pool_blocks("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh")
        pool_blocks_testnet_epoch = kp_testnet_server.get_pool_blocks("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh", 185)
        if len(pool_blocks_testnet) > 0 and len(pool_blocks_testnet_epoch) > 0:
                assert 'code' not in pool_blocks_testnet[0]
        
# get pool history
def test_get_pool_history():

        pool_history_custom = kp_custom_server.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        pool_history_custom_epoch = kp_custom_server.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 350)
        if len(pool_history_custom) > 0 and len(pool_history_custom_epoch) > 0:
                assert 'code' not in pool_history_custom[0] and 'code' not in pool_history_custom_epoch[0]
        
        pool_history_mainnet = kp_mainnet_server.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        pool_history_mainnet_epoch = kp_mainnet_server.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 350)
        if len(pool_history_mainnet) > 0 and len(pool_history_mainnet_epoch) > 0:
                assert 'code' not in pool_history_mainnet[0] and 'code' not in pool_history_mainnet_epoch[0]
        
        pool_history_testnet = kp_testnet_server.get_pool_history("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh")
        pool_history_testnet_epoch = kp_testnet_server.get_pool_history("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh", 185)
        if len(pool_history_testnet) > 0 and len(pool_history_testnet_epoch) > 0:
                assert 'code' not in pool_history_testnet[0] and 'code' not in pool_history_testnet_epoch[0]

# get pool updates
def test_get_pool_updates():

        pool_updates_custom = kp_custom_server.get_pool_updates()
        pool_updates_custom_pool = kp_custom_server.get_pool_updates("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        if len(pool_updates_custom) > 0 and len(pool_updates_custom_pool) > 0:
                assert 'code' not in pool_updates_custom[0] and 'code' not in pool_updates_custom_pool[0]
                
        pool_updates_mainnet = kp_mainnet_server.get_pool_updates()
        pool_updates_mainnet_pool = kp_mainnet_server.get_pool_updates("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        if len(pool_updates_mainnet) > 0 and len(pool_updates_mainnet_pool) > 0:
                assert 'code' not in pool_updates_mainnet[0] and 'code' not in pool_updates_mainnet_pool[0]
                
        pool_updates_testnet = kp_testnet_server.get_pool_updates()
        pool_updates_testnet_pool = kp_testnet_server.get_pool_updates("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh")
        if len(pool_updates_testnet) > 0 and len(pool_updates_testnet_pool) > 0:
                assert 'code' not in pool_updates_testnet[0] and 'code' not in pool_updates_testnet_pool[0]

# get pool relays
def test_get_pool_relays():

        pool_relays_custom = kp_custom_server.get_pool_relays()
        pool_relays_custom_range = kp_custom_server.get_pool_relays('0-70')
        if len(pool_relays_custom) > 0 and len(pool_relays_custom_range) > 0:
                assert 'code' not in pool_relays_custom[0] and 'code' not in pool_relays_custom_range[0]
                
        pool_relays_mainnet = kp_mainnet_server.get_pool_relays()
        pool_relays_mainnet_range = kp_mainnet_server.get_pool_relays('0-70')
        if len(pool_relays_mainnet) > 0 and len(pool_relays_mainnet_range) > 0:
                assert 'code' not in pool_relays_mainnet[0] and 'code' not in pool_relays_mainnet_range[0]
                
        pool_relays_testnet = kp_testnet_server.get_pool_relays()
        pool_relays_testnet_range = kp_testnet_server.get_pool_relays('0-70')
        if len(pool_relays_testnet) > 0 and len(pool_relays_testnet_range) > 0:
                assert 'code' not in pool_relays_testnet[0] and 'code' not in pool_relays_testnet_range[0]
 
# get pool metadata
def test_get_pool_metadata():

        pool_metadata_custom = kp_custom_server.get_pool_metadata()
        pool_metadata_custom_pool = kp_custom_server.get_pool_metadata("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        pool_metadata_custom_pool_list = kp_custom_server.get_pool_metadata(["pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 
                                                                             "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m"])
        if len(pool_metadata_custom) > 0 and len(pool_metadata_custom_pool) > 0 and len(pool_metadata_custom_pool_list) > 0:
                assert 'code' not in pool_metadata_custom[0] and 'code' not in pool_metadata_custom_pool[0] and 'code' not in pool_metadata_custom_pool_list[0]
        
        pool_metadata_mainnet = kp_mainnet_server.get_pool_metadata()
        pool_metadata_mainnet_pool = kp_mainnet_server.get_pool_metadata("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
        pool_metadata_mainnet_pool_list = kp_mainnet_server.get_pool_metadata(["pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 
                                                                               "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m"])
        if len(pool_metadata_mainnet) > 0 and len(pool_metadata_mainnet_pool) > 0 and len(pool_metadata_mainnet_pool_list) > 0:
                assert 'code' not in pool_metadata_mainnet[0] and 'code' not in pool_metadata_mainnet_pool[0] and 'code' not in pool_metadata_mainnet_pool_list[0]
                
        pool_metadata_testnet = kp_testnet_server.get_pool_metadata()
        pool_metadata_testnet_pool = kp_testnet_server.get_pool_metadata("pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh")
        pool_metadata_testnet_pool_list = kp_testnet_server.get_pool_metadata(["pool102llj7e7a0mmxssjvjkv2d6lppuh6cz6q9xwc3tsksn0jqwz9eh",
                                                                               "pool102x86jz7uus6p6mlw02fdw2s805kng7g6ujs6s342t5msk36tch"])
        if len(pool_metadata_testnet) > 0 and len(pool_metadata_testnet_pool) > 0 and len(pool_metadata_testnet_pool_list) > 0:
                assert 'code' not in pool_metadata_testnet[0] and 'code' not in pool_metadata_testnet_pool[0] and 'code' not in pool_metadata_testnet_pool_list[0]


##############################################################################
# SCRIPT FUNCTIONS

# get list of native scripts on the network
def test_get_native_script_list():
        
        script_list_custom = kp_custom_server.get_native_script_list()
        script_list_custom_range = kp_custom_server.get_native_script_list('0-10')
        if len(script_list_custom) > 0 and len(script_list_custom_range) > 0:
                assert 'code' not in script_list_custom[0] and 'code' not in script_list_custom_range[0]
        
        script_list_mainnet = kp_mainnet_server.get_native_script_list()
        script_list_mainnet_range = kp_mainnet_server.get_native_script_list('0-10')
        if len(script_list_mainnet) > 0 and len(script_list_mainnet_range) > 0:
                assert 'code' not in script_list_mainnet[0] and 'code' not in script_list_mainnet_range[0]
        
        script_list_testnet = kp_testnet_server.get_native_script_list()
        script_list_testnet_range = kp_testnet_server.get_native_script_list('0-10')
        if len(script_list_testnet) > 0 and len(script_list_testnet_range) > 0:
                assert 'code' not in script_list_testnet[0] and 'code' not in script_list_testnet_range[0]

# get plutus script list
def test_get_plutus_script_list():
        
        script_list_custom = kp_custom_server.get_plutus_script_list()
        script_list_custom_range = kp_custom_server.get_plutus_script_list('0-10')
        if len(script_list_custom) > 0 and len(script_list_custom_range) > 0:
                assert 'code' not in script_list_custom[0] and 'code' not in script_list_custom_range[0]
                
        script_list_mainnet = kp_mainnet_server.get_plutus_script_list()
        script_list_mainnet_range = kp_mainnet_server.get_plutus_script_list('0-10')
        if len(script_list_mainnet) > 0 and len(script_list_mainnet_range) > 0:
                assert 'code' not in script_list_mainnet[0] and 'code' not in script_list_mainnet_range[0]
        
        script_list_testnet = kp_testnet_server.get_plutus_script_list()
        script_list_testnet_range = kp_testnet_server.get_plutus_script_list('0-10')
        if len(script_list_testnet) > 0 and len(script_list_testnet_range) > 0:
                assert 'code' not in script_list_testnet[0] and 'code' not in script_list_testnet_range[0]


# get list of all redeemers for a given script hash
def test_get_script_redeemers():
        
        # script_redeemers_custom = kp_custom_server.get_script_redeemers('d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8')
        # if len(script_redeemers_custom) > 0:
        #         assert 'code' not in script_redeemers_custom[0]
        
        script_redeemers_mainnet = kp_mainnet_server.get_script_redeemers('d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8')
        if len(script_redeemers_mainnet) > 0:
                assert 'code' not in script_redeemers_mainnet[0]
        
        script_redeemers_testnet = kp_testnet_server.get_script_redeemers('9a3910acc1e1d49a25eb5798d987739a63f65eb48a78462ffae21e6f')
        if len(script_redeemers_testnet) > 0:
                assert 'code' not in script_redeemers_testnet[0]
      

##############################################################################
# TRANSACTION FUNCTIONS

# get transaction(s) info
def test_tx_info():
        
        tx_info_custom = kp_custom_server.get_tx_info('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_info_custom_list = kp_custom_server.get_tx_info(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                            'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_info_custom) > 0 and len(tx_info_custom_list) > 0:
                assert 'code' not in tx_info_custom[0] and 'code' not in tx_info_custom_list[0]
                
        tx_info_mainnet = kp_mainnet_server.get_tx_info('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_info_mainnet_list = kp_mainnet_server.get_tx_info(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                              'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_info_mainnet) > 0 and len(tx_info_mainnet_list) > 0:
                assert 'code' not in tx_info_mainnet[0] and 'code' not in tx_info_mainnet_list[0]
                
        tx_info_testnet = kp_testnet_server.get_tx_info('928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b')
        tx_info_testnet_list = kp_testnet_server.get_tx_info(['928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b',
                                                              'c7e96e4cd6aa9e3afbc7b32d1e8023daf4197931f1ea61d2bdfc7a2e5e017cf1'])
        if len(tx_info_testnet) > 0 and len(tx_info_testnet_list) > 0:
                assert 'code' not in tx_info_testnet[0] and 'code' not in tx_info_testnet_list[0]

# get transaction(s) utxos
def test_get_tx_utxos():
        
        tx_utxos_custom = kp_custom_server.get_tx_utxos('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_utxos_custom_list = kp_custom_server.get_tx_utxos(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                              'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_utxos_custom) > 0 and len(tx_utxos_custom_list) > 0:
                assert 'code' not in tx_utxos_custom[0] and 'code' not in tx_utxos_custom_list[0]
        
        tx_utxo_mainnet = kp_mainnet_server.get_tx_utxos('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_utxo_mainnet_list = kp_mainnet_server.get_tx_utxos(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                               'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_utxo_mainnet) > 0 and len(tx_utxo_mainnet_list) > 0:
                assert 'code' not in tx_utxo_mainnet[0] and 'code' not in tx_utxo_mainnet_list[0]
        
        tx_utxo_testnet = kp_testnet_server.get_tx_utxos('928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b')
        tx_utxo_testnet_list = kp_testnet_server.get_tx_utxos(['928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b',
                                                               'c7e96e4cd6aa9e3afbc7b32d1e8023daf4197931f1ea61d2bdfc7a2e5e017cf1'])
        if len(tx_utxo_testnet) > 0 and len(tx_utxo_testnet_list) > 0:
                assert 'code' not in tx_utxo_testnet[0] and 'code' not in tx_utxo_testnet_list[0]

# get transaction(s) metadata
def test_get_tx_metadata():
        
        tx_metadata_custom = kp_custom_server.get_tx_metadata('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_metadata_custom_list = kp_custom_server.get_tx_metadata(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                    'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_metadata_custom) > 0 and len(tx_metadata_custom_list) > 0:
                assert 'code' not in tx_metadata_custom[0] and 'code' not in tx_metadata_custom_list[0]
                
        tx_metadata_mainnet = kp_mainnet_server.get_tx_metadata('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_metadata_mainnet_list = kp_mainnet_server.get_tx_metadata(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                      'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_metadata_mainnet) > 0 and len(tx_metadata_mainnet_list) > 0:
                assert 'code' not in tx_metadata_mainnet[0] and 'code' not in tx_metadata_mainnet_list[0]
                
        tx_metadata_testnet = kp_testnet_server.get_tx_metadata('928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b')
        tx_metadata_testnet_list = kp_testnet_server.get_tx_metadata(['928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b',
                                                                      'c7e96e4cd6aa9e3afbc7b32d1e8023daf4197931f1ea61d2bdfc7a2e5e017cf1'])
        if len(tx_metadata_testnet) > 0 and len(tx_metadata_testnet_list) > 0:
                assert 'code' not in tx_metadata_testnet[0] and 'code' not in tx_metadata_testnet_list[0]

# get transaction(s) metadata labels
def test_get_tx_metalabels():
        
        tx_metalables_custom = kp_custom_server.get_tx_metalabels('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_metalables_custom_list = kp_custom_server.get_tx_metalabels(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                        'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_metalables_custom) > 0 and len(tx_metalables_custom_list) > 0:
                assert 'code' not in tx_metalables_custom[0] and 'code' not in tx_metalables_custom_list[0]
                
        tx_metalables_mainnet = kp_mainnet_server.get_tx_metalabels('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_metalables_mainnet_list = kp_mainnet_server.get_tx_metalabels(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                          'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_metalables_mainnet) > 0 and len(tx_metalables_mainnet_list) > 0:
                assert 'code' not in tx_metalables_mainnet[0] and 'code' not in tx_metalables_mainnet_list[0]
                
        tx_metalables_testnet = kp_testnet_server.get_tx_metalabels('928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b')
        tx_metalables_testnet_list = kp_testnet_server.get_tx_metalabels(['928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b',
                                                                          'c7e96e4cd6aa9e3afbc7b32d1e8023daf4197931f1ea61d2bdfc7a2e5e017cf1'])
        if len(tx_metalables_testnet) > 0 and len(tx_metalables_testnet_list) > 0:
                assert 'code' not in tx_metalables_testnet[0] and 'code' not in tx_metalables_testnet_list[0]

# # NOT FINISHED
# # submit_tx signed cbor
# # def test_submit_tx():
	
# # 	tx_submit = koios_python.submit_tx("file")
# # 	assert 'code' not in tx_submit[0]

# get tx status
def test_get_tx_status():
        
        tx_status_custom = kp_custom_server.get_tx_status('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_status_custom_list = kp_custom_server.get_tx_status(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_status_custom) > 0 and len(tx_status_custom_list) > 0:
                assert 'code' not in tx_status_custom[0] and 'code' not in tx_status_custom_list[0]
                
        tx_status_mainnet = kp_mainnet_server.get_tx_status('0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94')
        tx_status_mainnet_list = kp_mainnet_server.get_tx_status(['0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94',
                                                                  'f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e'])
        if len(tx_status_mainnet) > 0 and len(tx_status_mainnet_list) > 0:
                assert 'code' not in tx_status_mainnet[0] and 'code' not in tx_status_mainnet_list[0]
                
        tx_status_testnet = kp_testnet_server.get_tx_status('928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b')
        tx_status_testnet_list = kp_testnet_server.get_tx_status(['928052b80bfc23801da525a6bf8f805da36f22fa0fd5fec2198b0746eb82b72b',
                                                                  'c7e96e4cd6aa9e3afbc7b32d1e8023daf4197931f1ea61d2bdfc7a2e5e017cf1'])
        if len(tx_status_testnet) > 0 and len(tx_status_testnet_list) > 0:
                assert 'code' not in tx_status_testnet[0] and 'code' not in tx_status_testnet_list[0]
