#!/usr/bin/env python
"""
Provides all urls used in the library
"""

class URLs:
    # imported like class methods
    from .epoch import get_epoch_info, get_epoch_params

    def __init__(self, url='https://api.koios.rest/api/v0/', network=None):
        self.url = url
        self.network = network
        
        # # Network URLs
        self.TIP_URL = url + "tip"
        self.GENESIS_URL = url + "genesis"
        self.TOTALS_URL = url + "totals"
        # Epoch URLs
        self.EPOCH_INFO_URL = url + "epoch_info"
        self.EPOCH_PARAMS_URL = url + "epoch_params"
        
        # Block URLs

# # Network URLs
# TIP_URL = KOIOS_URL + "tip"
# GENESIS_URL = KOIOS_URL + "genesis"
# TOTALS_URL = KOIOS_URL + "totals"

# Epoch URLs
# EPOCH_INFO_URL = KOIOS_URL + "epoch_info"
# EPOCH_PARAMS_URL = KOIOS_URL + "epoch_params"

# # Block URLs
# BLOCKS_URL = KOIOS_URL + "blocks"
# BLOCK_INFO_URL = KOIOS_URL + "block_info"
# BLOCK_TXS_URL = KOIOS_URL + "block_txs"

# # Transactions URLs
# TX_INFO_URL = KOIOS_URL + "tx_info"
# TX_UTXOS_URL = KOIOS_URL + "tx_utxos"
# TX_METADATA_URL = KOIOS_URL + "tx_metadata"
# TX_METALABELS_URL = KOIOS_URL + "tx_metalabels"
# SUBMIT_TX_URL = KOIOS_URL + "submittx"
# TX_STATUS_URL = KOIOS_URL + "tx_status"

# # Address URLs
# ADDRESS_INFO_URL = KOIOS_URL + "address_info"
# ADDRESS_TXS_URL = KOIOS_URL + "address_txs"
# ADDRESS_ASSETS_URL = KOIOS_URL + "address_assets"
# CREDENTIAL_TXS_URL = KOIOS_URL + "credential_txs"

# # Account URLs
# ACCOUNT_LIST_URL = KOIOS_URL + "account_list"
# ACCOUNT_INFO_URL = KOIOS_URL + "account_info"
# ACCOUNT_REWARDS_URL = KOIOS_URL + "account_rewards"
# ACCOUNT_UPDATES_URL = KOIOS_URL + "account_updates"
# ACCOUNT_ADDRESES_URL = KOIOS_URL + "account_addresses"
# ACCOUNT_ASSETS_URL = KOIOS_URL + "account_assets"
# ACCOUNT_HISTORY_URL = KOIOS_URL + "account_history"

# # Asset URLs
# ASSET_LIST_URL = KOIOS_URL + "asset_list"
# ASSET_ADDRESS_LIST_URL = KOIOS_URL +  "asset_address_list?_asset_policy="
# ASSET_INFO_URL = KOIOS_URL + "asset_info?_asset_policy="
# ASSET_HISTORY_URL = KOIOS_URL + "asset_history?_asset_policy="
# ASSET_POLICY_INFO_URL = KOIOS_URL + "asset_policy_info?_asset_policy="
# ASSET_SUMMARY_URL = KOIOS_URL + "asset_summary?_asset_policy="
# ASSET_TXS_URL = KOIOS_URL + "asset_txs?_asset_policy="

# # Pool URLs
# POOL_LIST_URL = KOIOS_URL + "pool_list"
# POOL_INFO_URL = KOIOS_URL + "pool_info"
# POOL_STAKE_SNAPSHOT = KOIOS_URL + "pool_stake_snapshot?_pool_bech32="
# POOL_DELEGATORS_URL = KOIOS_URL + "pool_delegators?_pool_bech32="
# POOL_DELEGATORS_HISTORY_URL = KOIOS_URL + "pool_delegators_history?_pool_bech32="
# POOL_BLOCKS_URL = KOIOS_URL + "pool_blocks?_pool_bech32="
# POOL_HISTORY_URL = KOIOS_URL + "pool_history?_pool_bech32="
# POOL_UPDATES_URL = KOIOS_URL + "pool_updates"
# POOL_RELAYS_URL = KOIOS_URL + "pool_relays"
# POOL_METADATA_URL = KOIOS_URL + "pool_metadata"

# # Scripts URLs
# NATIVE_SCRIPT_LIST_URL = KOIOS_URL + "native_script_list"
# PLUTUS_SCRIPT_LIST_URL = KOIOS_URL + "plutus_script_list"
# SCRIPT_REDEEMERS_URL = KOIOS_URL + "script_redeemers"
