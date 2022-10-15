#!/usr/bin/env python
"""
Examples to check how works Koios-Python Library
"""
import pytest
import pprint # We recommend use pprint library to show your outputs
import koios_python
from koios_python import address # We need to install and import koios_python library



##############################################################################
# ACCOUNT FUNCTIONS

# get account list
def test_get_account_list():
	account_list = koios_python.get_account_list()
	assert 'code' not in account_list[0]

# get account info
def test_get_account_info():
        account_info = koios_python.get_account_info('stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250')
        assert 'code' not in account_info[0]

# get account rewards
def test_get_account_rewards():
        account_rewards = koios_python.get_account_rewards('stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250')
        assert 'code' not in account_rewards[0]
        
# get account rewards by epoch
def test_get_account_rewards_by_epoch():
        account_rewards = koios_python.get_account_rewards('stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250', 350)
        assert 'code' not in account_rewards[0]
        
# get account updates
def test_get_account_updates():
        account_updates = koios_python.get_account_updates('stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250')
        assert 'code' not in account_updates[0]

# get account assets
def test_get_account_assets():
        account_assets = koios_python.get_account_assets('stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250')
        if len(account_assets) > 0:
                assert 'code' not in account_assets[0]
        
# get account history
def test_get_account_history():
        account_history = koios_python.get_account_history('stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250')
        assert 'code' not in account_history[0]
        

        
##############################################################################
# ADDRESS FUNCTIONS

# get address info
def test_get_address_info():
	address_info = koios_python.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
	assert 'code' not in address_info[0]

# get address transactions
def test_get_address_transactions():
        address_txs = koios_python.get_address_txs("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        assert 'code' not in address_txs[0]
        
        address_txs_after_block = koios_python.get_address_txs("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",1)
        assert 'code' not in address_txs_after_block[0]

# get address assets 
def test_get_address_assets():
        address_assets = koios_python.get_address_assets("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_assets) >0:
                assert 'code' not in address_assets[0]

# get payment credentials hash
def test_get_credentials():
        
        credentials = koios_python.get_credential_txs('025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52')
        assert 'code' not in credentials[0]
        
        credentials_after_block = koios_python.get_credential_txs('025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52',6238675)
        assert 'code' not in credentials_after_block[0]


##############################################################################
# ASSET FUNCTIONS

# get asset list of all native tokens
def test_get_asset_list():
	asset_list = koios_python.get_asset_list()
	assert 'code' not in asset_list[0]

# get asset address list
def test_get_asset_address_list():
        asset_address_list = koios_python.get_asset_address_list('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
        assert 'code' not in asset_address_list[0]

# get asset info
def test_get_asset_info():
        asset_info = koios_python.get_asset_info('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
        assert 'code' not in asset_info[0]
        
# get asset history
def test_get_asset_history():
	asset_history = koios_python.get_asset_history('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
	assert 'code' not in asset_history[0]
 
# get asset policy info
def test_get_asset_policy_info():
        asset_policy_info = koios_python.get_asset_policy_info('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501')
        assert 'code' not in asset_policy_info[0]

# get asset summary
def test_get_asset_summary():
        asset_summary = koios_python.get_asset_summary('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', '424f4f4b')
        assert 'code' not in asset_summary[0]

# get asset transaction history
def test_get_asset_txs_history():
	asset_txs_history = koios_python.get_asset_txs('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', '424f4f4b')
	assert 'code' not in asset_txs_history[0]


##############################################################################
# BLOCK FUNCTIONS

# get list of blocks
def test_get_blocks():
        blocks = koios_python.get_blocks()
        assert 'code' not in blocks[0]
        
# get block info
def test_get_block_info():
	block_info = koios_python.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30",
    						"60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a",
    						"c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"])
	assert 'code' not in block_info[0]

# get block transactions
def test_get_block_txs():
        block_txs = koios_python.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30"])
        assert 'code' not in block_txs[0]


##############################################################################
# EPOCH FUNCTIONS

# get epoch info
def test_get_epoch_info():
	epoch_info = koios_python.get_epoch_info()
	assert 'code' not in epoch_info[0]
 
# get epoch params
def test_get_epoch_params():
	epoch_params = koios_python.get_epoch_params()
	assert 'code' not in epoch_params[0]



##############################################################################
# NETWORK FUNCTIONS

# check tip
def test_get_tip():
        tip = koios_python.get_tip()
        assert 'code' not in tip[0]
        
# check genesis info
def test_get_genesis():
        genesis_info = koios_python.get_genesis()
        assert 'code' not in genesis_info[0]
        
def test_get_totals():
        epoch_totals = koios_python.get_totals()
        assert 'code' not in epoch_totals[0]


##############################################################################
# POOL FUNCTIONS

# get list of pools on the network
def test_get_pool_list():
	pool_list = koios_python.get_pool_list('0-10')
	assert 'code' not in pool_list[0]
 
# get pool info
def test_get_pool_info():
        pool_info = koios_python.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp",
    						"pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m",
    						"pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"])
        assert 'code' not in pool_info[0]
        
        
# get pool stake snapshot
def test_get_pool_stake_snapshot():
        stake_snapshot = koios_python.get_pool_stake_snapshot("pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp")
        assert 'code' not in stake_snapshot[0]    

        
# get pool delegator information
def test_get_pool_delegators():
        delegator_info = koios_python.get_pool_delegators("pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp")
        assert 'code' not in delegator_info[0]
        
# get pool delegator history
def test_get_pool_delegators_history():
        
	delegator_history = koios_python.get_pool_delegators_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
	assert 'code' not in delegator_history[0]

	delegator_history_epoch = koios_python.get_pool_delegators_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 320)
	assert 'code' not in delegator_history_epoch[0]

# get pool blocks
def test_get_pool_blocks():
	pool_blocks = koios_python.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
	assert 'code' not in pool_blocks[0]

	pool_blocks_epoch = koios_python.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 320)
	assert 'code' not in pool_blocks_epoch[0]

        
# get pool history
def test_get_pool_history():
	pool_history = koios_python.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
	assert 'code' not in pool_history[0]

	pool_history_epoch = koios_python.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 320)
	assert 'code' not in pool_history_epoch[0]

# get pool updates
def test_get_pool_updates():
	pool_updates = koios_python.get_pool_updates()
	assert 'code' not in pool_updates[0]

# get pool relays
def test_get_pool_relays():
	pool_relays = koios_python.get_pool_relays('0-10')
	assert 'code' not in pool_relays[0]
 
# get pool metadata
def test_get_pool_metadata():
	pool_metadata = koios_python.get_pool_metadata()
	assert 'code' not in pool_metadata[0]
 
	pool_metadata_id = koios_python.get_pool_metadata(["pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m"])
	assert 'code' not in pool_metadata_id[0]

##############################################################################
# SCRIPT FUNCTIONS

# get list of native scripts on the network
def test_get_native_script_list():
	script_list = koios_python.get_native_script_list('0-10')
	assert 'code' not in script_list[0]

# get plutus script list
def test_get_plutus_script_list():
	script_list = koios_python.get_plutus_script_list('0-10')
	assert 'code' not in script_list[0]

# get list of all redeemers for a given script hash
def test_get_script_redeemers():
        script_redeemers = koios_python.get_script_redeemers('d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8')
        assert 'code' not in script_redeemers[0]
        
##############################################################################
