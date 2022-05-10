#!/usr/bin/env python
"""
Provides all address functions
"""
import json
import requests

from koios_python.urls import ADDRESS_ASSETS_URL, ADDRESS_INFO_URL, ADDRESS_TXS_URL, \
    CREDENTIAL_TXS_URL

def get_address_info(address):
    """
    Get address info - balance, associated stake address (if any) and UTxO set.

    :param str address: wallet used public address(es).
    return: list with data of this used public address.
    :rtype: list.
    """
    info = requests.get(ADDRESS_INFO_URL + "?_address=" + address)
    info = json.loads(info.content)
    return info


def get_address_txs(address_tx, after_block=0):
    """
    Get the transaction hash list of input address array, optionally filtering after specified
    block height (inclusive)

    :param tx_hash: list or single transaction hash to search and read utxos data
    :param after_block: filtering after block (inclusive) defaul is 0, from the beginning
    :return: hash list of address transactions
    """
    get_format = {"_addresses": [address_tx], "_after_block_height": str(after_block)}
    hash_list = requests.post( ADDRESS_TXS_URL, json = get_format)
    hash_list  = json.loads(hash_list.content)
    return hash_list


def get_address_assets(address):
    """
    Get the list of all the assets (policy, name and quantity) for a given address.

    :param str address: wallet used public address
    return: list of all the assets
    :rtype: list.
    """
    info = requests.get(ADDRESS_ASSETS_URL + "?_address=" + address)
    info = json.loads(info.content)
    return info


def get_credential_txs(payment_credentials, after_block=0):
    """
    Get the transaction hash list of input payment credential array (stake key), optionally
    filtering after specified block height (inclusive).

    :param str payment_credentials: list address payment credential array (stake key)
    :param int after_block: filtering after block (inclusive) defaul is 0, from the beginning
    :return: hash list of address transactions.
    :rtype: list.
    """
    get_format = {"_payment_credentials":[payment_credentials], "_after_block_height": after_block}
    hash_list = requests.post( CREDENTIAL_TXS_URL, json = get_format)
    hash_list  = json.loads(hash_list.content)
    return hash_list
    