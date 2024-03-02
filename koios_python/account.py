#!/usr/bin/env python
"""
Provides all account functions
"""
import json
from time import sleep
import requests
from .environment import *


@Exception_Handler
def get_account_list(self, content_range="0-999"):
    """
    Get a list of all accounts.

    :return: string list of account (stake address: stake1...  bech32 format) IDs.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        account_list = requests.get(self.ACCOUNT_LIST_URL, headers = custom_headers, timeout=timeout)
        account_list = json.loads(account_list.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        account_list = requests.get(self.ACCOUNT_LIST_URL, headers = custom_headers, timeout=timeout)
        account_list = json.loads(account_list.content)

    return account_list


@Exception_Handler
def get_account_info(self, *args):
    """
    Get the account information for given stake addresses (accounts).

    :param str args: staking address/es in bech32 format (stake1...).
    :return: list with all address data.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_stake_addresses": [args] }
        accounts_info = requests.post(self.ACCOUNT_INFO_URL, json= get_format, timeout=timeout )
        accounts_info = json.loads(accounts_info.content)
    else:
        get_format = {"_stake_addresses": [args] }
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        accounts_info = requests.post(self.ACCOUNT_INFO_URL, json= get_format, headers = custom_headers, timeout=timeout )
        accounts_info = json.loads(accounts_info.content)

    return accounts_info


@Exception_Handler
def get_account_info_cached(self, *args):
    """
    Get the account information for given stake addresses (accounts).

    :param str args: staking address/es in bech32 format (stake1...).
    :return: list with all address data.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_stake_addresses": [args] }
        accounts_info = requests.post(self.ACCOUNT_INFO_CACHED_URL, json=get_format, timeout=timeout)
        accounts_info = json.loads(accounts_info.content)
    else:
        get_format = {"_stake_addresses": [args] }
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        accounts_info = requests.post(self.ACCOUNT_INFO_CACHED_URL, json=get_format, headers = custom_headers, timeout=timeout)
        accounts_info = json.loads(accounts_info.content)

    return accounts_info


@Exception_Handler
def get_account_utxos(self, *args, content_range="0-999", extended=False):
    """
    Get a list of all UTxOs for a given stake address (account)

    :return: string list Array of account UTxOs associated with stake address.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and extended is False:
        custom_headers = {"Range": str(content_range)}
        get_format = {"_stake_addresses": [args], "_extended": "false"}
        account_utxos = requests.post(f"{self.ACCOUNT_UTXOS_URL}", timeout=timeout, json=get_format, headers=custom_headers)
        account_utxos = json.loads(account_utxos.content)

    if self.BEARER is None and extended is True:
        custom_headers = {"Range": str(content_range)}
        get_format = {"_stake_addresses": [args], "_extended": "true"}
        account_utxos = requests.post(f"{self.ACCOUNT_UTXOS_URL}", timeout=timeout, json=get_format, headers=custom_headers)
        account_utxos = json.loads(account_utxos.content)
    
    if self.BEARER is not None and extended is False:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}" }
        get_format = {"_stake_addresses": [args], "_extended": "false"}
        account_utxos = requests.post(f"{self.ACCOUNT_UTXOS_URL}", headers = custom_headers, timeout=timeout, json=get_format)
        account_utxos = json.loads(account_utxos.content)

    if self.BEARER is not None and extended is True:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}" }
        get_format = {"_stake_addresses": [args], "_extended": "true"}
        account_utxos = requests.post(f"{self.ACCOUNT_UTXOS_URL}", headers = custom_headers, timeout=timeout, json=get_format)
        account_utxos = json.loads(account_utxos.content)

    return account_utxos


@Exception_Handler
def get_account_txs(self, stake_address, after_block=None):
    """
    Get the transaction hash list of input payment credential array (stake key), optionally
    filtering after specified block height (inclusive).

    :param str stake_address: str stake address (stake1...)
    :param int after_block: filtering after block (inclusive) defaul is None, from the beginning
    :return: list of address transactions.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and after_block is None:
        get_format = {"_stake_address": stake_address}
        txs_list = requests.post(self.ACCOUNT_TX_URL, json = get_format, timeout=timeout)
        txs_list = json.loads(txs_list.content)

    if self.BEARER is None and after_block is not None:
        get_format = {"_stake_address": stake_address, "_after_block_height": after_block}
        txs_list = requests.post(self.ACCOUNT_TXS_URL, json = get_format, timeout=timeout)
        txs_list = json.loads(txs_list.content)

    if self.BEARER is not None and after_block is None:
        get_format = {"_stake_address": stake_address}
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        txs_list = requests.post(self.ACCOUNT_TX_URL, json = get_format, headers = custom_headers, timeout=timeout)
        txs_list = json.loads(txs_list.content)

    if self.BEARER is not None and after_block is not None:
        get_format = {"_stake_address": stake_address, "_after_block_height": after_block}
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        txs_list = requests.post(self.ACCOUNT_TXS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        txs_list = json.loads(txs_list.content)

    return txs_list


@Exception_Handler
def get_account_rewards(self, *args, epoch_no=None):
    """
    Get the full rewards history (including MIR) for given stake addresses (accounts).

    :param str args: Cardano staking address (reward account) in bech32 format (stake1...)
    :param int args: Epoch Number, has to be last parameter (optional).
    return: list with all account rewards.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and epoch_no is None:
        get_format = {"_stake_addresses": [args] }
        rewards = requests.post(self.ACCOUNT_REWARDS_URL, json= get_format, timeout=timeout)
        rewards = json.loads(rewards.content)
    
    if self.BEARER is None and epoch_no is not None:
        get_format = {"_stake_addresses": [args], "_epoch_no": str(epoch_no)}
        rewards = requests.post(self.ACCOUNT_REWARDS_URL, json= get_format, timeout=timeout)
        rewards = json.loads(rewards.content)

    if self.BEARER is not None and epoch_no is None:
        get_format = {"_stake_addresses": [args] }
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        rewards = requests.post(self.ACCOUNT_REWARDS_URL, json= get_format, headers = custom_headers, timeout=timeout)
        rewards = json.loads(rewards.content)

    if self.BEARER is not None and epoch_no is not None:
        get_format = {"_stake_addresses": [args], "_epoch_no": str(epoch_no)}
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        rewards = requests.post(self.ACCOUNT_REWARDS_URL, json= get_format, headers = custom_headers, timeout=timeout)
        rewards = json.loads(rewards.content)

    return rewards


@Exception_Handler
def get_account_updates(self, *args):
    """
    Get the account updates (registration, deregistration, delegation and withdrawals) for given \
    stake addresses (accounts)

    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account updates.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_stake_addresses": [args]}
        updates = requests.post(self.ACCOUNT_UPDATES_URL, json= get_format, timeout=timeout)
        updates = json.loads(updates.content)
    else:
        get_format = {"_stake_addresses": [args]}
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        updates = requests.post(self.ACCOUNT_UPDATES_URL, json= get_format, headers = custom_headers, timeout=timeout)
        updates = json.loads(updates.content)

    return updates


@Exception_Handler
def get_account_addresses(self, *args, content_range="0-999", first_only=False, empty=False):
    """
    Get all addresses associated with given staking accounts.
    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account addresses.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and first_only is False and empty is False:
        custom_headers = {"Range": str(content_range)}
        get_format = {"_stake_addresses": [args], "_first_only": "false", "_empty": "false"}
        addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, timeout=timeout, headers=custom_headers)
        addresses = json.loads(addresses.content)

    if self.BEARER is None and first_only is True and empty is False:
        custom_headers = {"Range": str(content_range)}
        get_format = {"_stake_addresses": [args], "_first_only": "true", "_empty": "false"}
        addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, timeout=timeout, headers=custom_headers)
        addresses = json.loads(addresses.content)

    if self.BEARER is None and first_only is False and empty is True:
        custom_headers = {"Range": str(content_range)}
        get_format = {"_stake_addresses": [args], "_first_only": "false", "_empty": "true"}
        addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, timeout=timeout, headers=custom_headers)
        addresses = json.loads(addresses.content)

    if self.BEARER is None and first_only is True and empty is True:
        custom_headers = {"Range": str(content_range)}
        get_format = {"_stake_addresses": [args], "_first_only": "true", "_empty": "true"}
        addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, timeout=timeout, headers=custom_headers)
        addresses = json.loads(addresses.content)

    if self.BEARER is not None and first_only is False and empty is False:
        get_format = {"_stake_addresses": [args], "_first_only": "false", "_empty": "false"}
        custom_headers = {"Range": str(content_range) ,"Authorization": f"Bearer {self.BEARER}"}
        addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, headers = custom_headers, timeout=timeout)
        addresses = json.loads(addresses.content)

    if self.BEARER is not None and first_only is True and empty is False:
        get_format = {"_stake_addresses": [args], "_first_only": "true", "_empty": "false"}
        custom_headers = {"Range": str(content_range) ,"Authorization": f"Bearer {self.BEARER}"}
        addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, headers = custom_headers, timeout=timeout)
        addresses = json.loads(addresses.content)

    if self.BEARER is not None and first_only is False and empty is True:
        get_format = {"_stake_addresses": [args], "_first_only": "false", "_empty": "true"}
        custom_headers = {"Range": str(content_range) ,"Authorization": f"Bearer {self.BEARER}"}
        addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, headers = custom_headers, timeout=timeout)
        addresses = json.loads(addresses.content)

    if self.BEARER is not None and first_only is True and empty is True:
        get_format = {"_stake_addresses": [args], "_first_only": "true", "_empty": "true"}
        custom_headers = {"Range": str(content_range) ,"Authorization": f"Bearer {self.BEARER}"}
        addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, headers = custom_headers, timeout=timeout)
        addresses = json.loads(addresses.content)

    return addresses


@Exception_Handler
def get_account_assets(self, *args):
    """
    Get the native asset balance of given accounts.
    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account assets.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_stake_addresses": [args]}
        assets = requests.post(self.ACCOUNT_ASSETS_URL, json= get_format, timeout=timeout)
        assets = json.loads(assets.content)
    else:
        get_format = {"_stake_addresses": [args]}
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        assets = requests.post(self.ACCOUNT_ASSETS_URL, json= get_format, headers = custom_headers, timeout=timeout)
        assets = json.loads(assets.content)
        
    return assets


## Alternative to Paginate all list automatically
def get_account_assets_paginated(self, *args):
    """
    Get the native asset balance of given accounts.
    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account assets.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT
    offset= OFFSET
    retriyng_time = RETRYING_TIME
    total_assets= []

    while True:
        while True:
            try:
                get_format = {"_stake_addresses": [args]}
                assets = requests.post(self.ACCOUNT_ASSETS_URL + str(offset), json= get_format, timeout=timeout)
                assets = json.loads(assets.content)
                break

            except requests.exceptions.ReadTimeout as timeout_error:
                print(f"Exception: {timeout_error}")
                if timeout < LIMIT_TIMEOUT:
                    timeout= timeout + 10
                else:
                    print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                    break
                print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

            except json.decoder.JSONDecodeError as decode_error:
                print(f"Exception Decode: Payload too heavy. {decode_error}")
                sleep(SLEEP_TIME)
                retriyng_time += 1
                print(f"Retriyng one more time...({retriyng_time} times)")
                if retriyng_time >= LIMIT_RETRYING_TIMES:
                    print("Reached limit of attempts")
                    break

        total_assets += assets
        if len(total_assets) < 1000:
            break
        offset += len(total_assets)

    return total_assets


@Exception_Handler
def get_account_history(self, *args, epoch_no=None, content_range="0-999"):
    """
    Get the staking history of given stake addresses (accounts).
    :param str address: staking address in bech32 format (stake1...)
    return: list with all account history.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and epoch_no is None:
        get_format = {"_stake_addresses": [args] }
        custom_headers = {"Range": str(content_range)}
        history = requests.post(self.ACCOUNT_HISTORY_URL, json= get_format, timeout=timeout, headers=custom_headers)
        history = json.loads(history.content)
    
    if self.BEARER is None and epoch_no is not None:
        get_format = {"_stake_addresses": [args], "_epoch_no": str(epoch_no)}
        custom_headers = {"Range": str(content_range)}
        history = requests.post(self.ACCOUNT_HISTORY_URL, json= get_format, timeout=timeout, headers=custom_headers)
        history = json.loads(history.content)

    if self.BEARER is not None and epoch_no is None:
        get_format = {"_stake_addresses": [args] }
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        history = requests.post(self.ACCOUNT_HISTORY_URL, json= get_format, headers = custom_headers, timeout=timeout)
        history = json.loads(history.content)
    
    if self.BEARER is not None and epoch_no is not None:
        get_format = {"_stake_addresses": [args], "_epoch_no": str(epoch_no)}
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        history = requests.post(self.ACCOUNT_HISTORY_URL, json= get_format, headers = custom_headers, timeout=timeout)
        history = json.loads(history.content)

    return history

