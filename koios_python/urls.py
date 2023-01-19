#!/usr/bin/env python
"""
Provides all urls used in the library
"""

class URLs:
    # imported like class methods
    from .epoch import get_epoch_info, get_epoch_params, get_epoch_block_protocols
    from .network import get_tip, get_genesis, get_totals
    from .block import get_blocks, get_block_info, get_block_txs
    from .address import get_address_info, get_address_txs, get_address_assets, get_credential_txs
    from .account import get_account_info, get_account_info_cached, get_account_list, get_account_rewards, get_account_updates, get_account_addresses, get_account_assets, get_account_history, get_account_assets_2
    from .asset import get_asset_list, get_asset_address_list, get_asset_info, get_asset_history, get_asset_policy_info, get_asset_summary, get_asset_txs
    from .pool import get_pool_list, get_pool_info, get_pool_stake_snapshot, get_pool_delegators, get_pool_delegators_history, get_pool_blocks, get_pool_history, get_pool_updates, get_pool_relays, get_pool_metadata
    from .scripts import get_native_script_list, get_plutus_script_list, get_script_redeemers, get_datum_info
    from .transactions import get_tx_info, get_tx_utxos, get_tx_metadata, get_tx_metalabels, submit_tx, get_tx_status


    def __init__(self, url='https://api.koios.rest/api/v0/', network='mainnet'):
        
        self.url = url
        self.network = network

        # change subdomain to network name then change the rest of urls to use the new subdomain
        if self.network == 'preview' or self.network == 'preprod':
            # replace mainnet subdomain with "testnet" subdomain
            self.url = self.url.replace(self.url.split('.')[0], self.network)
            # add https:// to the url
            self.url = 'https://' + self.url
        elif self.network == 'mainnet':
            self.url = url


        # Network URLs
        self.TIP_URL = self.url + "tip"
        self.GENESIS_URL = self.url + "genesis"
        self.TOTALS_URL = self.url + "totals"
        # Epoch URLs
        self.EPOCH_INFO_URL = self.url + "epoch_info"
        self.EPOCH_PARAMS_URL = self.url + "epoch_params"
        self.EPOCH_BLOCKS_URL = self.url + "epoch_block_protocols"
        # Block URLs
        self.BLOCKS_URL = self.url + "blocks"
        self.BLOCK_INFO_URL = self.url + "block_info"
        self.BLOCK_TXS_URL = self.url + "block_txs"
        # Transaction URLs
        self.TX_INFO_URL = self.url + "tx_info"
        self.TX_UTXOS_URL = self.url + "tx_utxos"
        self.TX_METADATA_URL = self.url + "tx_metadata"
        self.TX_METALABELS_URL = self.url + "tx_metalabels"
        self.SUBMIT_TX_URL = self.url + "submittx"
        self.TX_STATUS_URL = self.url + "tx_status"
        # Address URLs
        self.ADDRESS_INFO_URL = self.url + "address_info"
        self.ADDRESS_TXS_URL = self.url + "address_txs"
        self.ADDRESS_ASSETS_URL = self.url + "address_assets"
        self.CREDENTIAL_TXS_URL = self.url + "credential_txs"
        # Account URLs
        self.ACCOUNT_LIST_URL = self.url + "account_list?offset="
        self.ACCOUNT_INFO_URL = self.url + "account_info"
        self.ACCOUNT_INFO_URL_CACHED = self.url + "account_info_cached"
        self.ACCOUNT_REWARDS_URL = self.url + "account_rewards"
        self.ACCOUNT_UPDATES_URL = self.url + "account_updates"
        self.ACCOUNT_ADDRESSES_URL = self.url + "account_addresses"
        #self.ACCOUNT_ASSETS_URL = self.url + "account_assets?offset="
        self.ACCOUNT_ASSETS_URL = self.url + "account_assets"
        self.ACCOUNT_HISTORY_URL = self.url + "account_history"
        # Asset URLs
        self.ASSET_LIST_URL = self.url + "asset_list"
        self.ASSET_ADDRESS_LIST_URL = self.url +  "asset_address_list?_asset_policy="
        self.ASSET_INFO_URL = self.url + "asset_info?_asset_policy="
        self.ASSET_HISTORY_URL = self.url + "asset_history?_asset_policy="
        self.ASSET_POLICY_INFO_URL = self.url + "asset_policy_info?_asset_policy="
        self.ASSET_SUMMARY_URL = self.url + "asset_summary?_asset_policy="
        self.ASSET_TXS_URL = self.url + "asset_txs?_asset_policy="

        # Pool URLs
        self.POOL_LIST_URL = self.url + "pool_list"
        self.POOL_INFO_URL = self.url + "pool_info"
        self.POOL_STAKE_SNAPSHOT = self.url + "pool_stake_snapshot?_pool_bech32="
        self.POOL_DELEGATORS_URL = self.url + "pool_delegators?_pool_bech32="
        self.POOL_DELEGATORS_HISTORY_URL = self.url + "pool_delegators_history?_pool_bech32="
        self.POOL_BLOCKS_URL = self.url + "pool_blocks?_pool_bech32="
        self.POOL_HISTORY_URL = self.url + "pool_history?_pool_bech32="
        self.POOL_UPDATES_URL = self.url + "pool_updates"
        self.POOL_RELAYS_URL = self.url + "pool_relays"
        self.POOL_METADATA_URL = self.url + "pool_metadata"

        # Scripts URLs
        self.NATIVE_SCRIPT_LIST_URL = self.url + "native_script_list"
        self.PLUTUS_SCRIPT_LIST_URL = self.url + "plutus_script_list"
        self.SCRIPT_REDEEMERS_URL = self.url + "script_redeemers?_script_hash="
        self.DATUM_INFO_URL = self.url + "datum_info"
