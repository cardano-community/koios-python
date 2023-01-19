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
    custom_headers = {"Range": str(content_range)}
    address_list = requests.get(self.ACCOUNT_LIST_URL, headers = custom_headers, timeout=timeout)
    address_list = json.loads(address_list.content)
    return address_list


@Exception_Handler
def get_account_info(self, *args):
    """
    Get the account information for given stake addresses (accounts).

    :param str args: staking address/es in bech32 format (stake1...).
    :return: list with all address data.
    :rtype: list.
    """
    timeout = get_timeout()
    get_format = {"_stake_addresses": [args] }
    accounts_info = requests.post(self.ACCOUNT_INFO_URL, json= get_format, timeout=timeout )
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
    get_format = {"_stake_addresses": [args] }
    accounts_info = requests.post(self.ACCOUNT_INFO_URL_CACHED, json= get_format,timeout=timeout)
    accounts_info = json.loads(accounts_info.content)
    return accounts_info


@Exception_Handler
def get_account_rewards(self, *args):
    """
    Get the full rewards history (including MIR) for given stake addresses (accounts).

    :param str args: Cardano staking address (reward account) in bech32 format (stake1...)
    :param int args: Epoch Number, has to be last parameter (optional).
    return: list with all account rewards.
    :rtype: list.
    """
    timeout = get_timeout()
    epoch = args[len(args)-1]
    if not isinstance(epoch, int):
        get_format = {"_stake_addresses": [args] }
        rewards = requests.post(self.ACCOUNT_REWARDS_URL, json= get_format, timeout=timeout)
        rewards = json.loads(rewards.content)
    else:
        get_format = {"_stake_addresses": [args], "_epoch_no": epoch}
        rewards = requests.post(self.ACCOUNT_REWARDS_URL, json= get_format, timeout=timeout)
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
    get_format = {"_stake_addresses": [args]}
    updates = requests.post(self.ACCOUNT_UPDATES_URL, json= get_format, timeout=timeout)
    updates = json.loads(updates.content)
    return updates


@Exception_Handler
def get_account_addresses(self, *args):
    """
    Get all addresses associated with given staking accounts.
    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account addresses.
    :rtype: list.
    """
    timeout = get_timeout()
    get_format = {"_stake_addresses": [args]}
    addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json= get_format, timeout=timeout)
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
    get_format = {"_stake_addresses": [args]}
    assets = requests.post(self.ACCOUNT_ASSETS_URL, json= get_format, timeout=timeout)
    assets = json.loads(assets.content)
    return assets


## Alternative to Paginate all list automatically
def get_account_assets_2(self, *args):
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
def get_account_history(self, *args):
    """
    Get the staking history of given stake addresses (accounts).
    :param str address: staking address in bech32 format (stake1...)
    return: list with all account history.
    :rtype: list.
    """
    timeout = get_timeout()
    epoch = args[len(args)-1]
    if not isinstance(epoch, int):
        get_format = {"_stake_addresses": [args] }
        history = requests.post(self.ACCOUNT_HISTORY_URL, json= get_format, timeout=timeout)
        history = json.loads(history.content)
    else:
        get_format = {"_stake_addresses": [args], "_epoch_no": epoch}
        history = requests.post(self.ACCOUNT_HISTORY_URL, json= get_format, timeout=timeout)
        history = json.loads(history.content)
    return history