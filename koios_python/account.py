#!/usr/bin/env python
"""
Provides all account functions
"""
import json
import requests
from .urls import ACCOUNT_ADDRESES_URL, ACCOUNT_ASSETS_URL, ACCOUNT_HISTORY_URL, \
    ACCOUNT_INFO_URL, ACCOUNT_LIST_URL, ACCOUNT_REWARDS_URL, ACCOUNT_UPDATES_URL

def get_account_list():
    """
    Get a list of all accounts.

    :return: string list of account (stake address: stake1...  bech32 format) IDs.
    :rtype: list.
    """
    address_list = requests.get(ACCOUNT_LIST_URL)
    address_list = json.loads(address_list.content)
    return address_list


def get_account_info(address):
    """
    Get the account info of any (payment or staking) address.

    :param str address: staking address in bech32 format (stake1...).
    :return: list with all address data.
    :rtype: list.
    """
    info = requests.get(ACCOUNT_INFO_URL + address)
    info = json.loads(info.content)
    return info


def get_account_rewards(address, epoch=None):
    """
    Get the full rewards history (including MIR) for a stake address, or certain epoch if specified.

    :param str address: Cardano staking address (reward account) in bech32 format (stake1...)
    :param int epoch: epoch (optional).
    return: list with all account rewards.
    :rtype: list.
    """
    if epoch is None:
        info = requests.get(ACCOUNT_REWARDS_URL +str(address))
        info = json.loads(info.content)
    else:
        info = requests.get(ACCOUNT_REWARDS_URL + str(address)+"&_epoch_no=" + str(epoch))
        info = json.loads(info.content)
    return info


def get_account_updates(address):
    """
    Get the account updates (registration, deregistration, delegation and withdrawals).

    :param str address: staking address in bech32 format (stake1...)
    :return: list with all account updates.
    :rtype: list.
    """
    info = requests.get(ACCOUNT_UPDATES_URL + address)
    info = json.loads(info.content)
    return info


def get_account_addresses(address):
    """
    Get all addresses associated with an account.

    :param str address: staking address in bech32 format (stake1...)
    :return: list with all account addresses.
    :rtype: list.
    """
    info = requests.get(ACCOUNT_ADDRESES_URL + address)
    info = json.loads(info.content)
    return info


def get_account_assets(address):
    """
    Get the native asset balance of an account.

    :param str address: staking address in bech32 format (stake1...)
    :return: list with all account assets.
    :rtype: list.
    """
    info = requests.get(ACCOUNT_ASSETS_URL + address)
    info = json.loads(info.content)
    return info


def get_account_history(address):
    """
    Get the staking history of an account.

    :param str address: staking address in bech32 format (stake1...)
    return: list with all account history.
    :rtype: list.
    """
    info = requests.get(ACCOUNT_HISTORY_URL + address)
    info = json.loads(info.content)
    return info
