#!/usr/bin/env python
"""
Provides all address functions
"""
import json
import requests


def get_address_info(self, *args):
    """
    Get address info - balance, associated stake address (if any) and UTxO set.

    :param str address: wallet used public address(es).
    return: list with data of this used public address.
    :rtype: list.
    """
    get_format = {"_addresses": [args] }
    addresses = requests.post(self.ADDRESS_INFO_URL, json= get_format, timeout=10)
    addresses = json.loads(addresses.content)
    return addresses


def get_address_txs(self, address_tx, after_block=0):
    """
    Get the transaction hash list of input address array, optionally filtering after specified
    block height (inclusive)

    :param tx_hash: list or single transaction hash to search and read utxos data
    :param after_block: filtering after block (inclusive) defaul is 0, from the beginning
    :return: hash list of address transactions
    """
    get_format = {"_addresses": [address_tx], "_after_block_height": str(after_block)}
    hash_list = requests.post(self.ADDRESS_TXS_URL, json = get_format, timeout=10)
    hash_list  = json.loads(hash_list.content)
    return hash_list


def get_address_assets(self, *args):
    """
    Get the list of all the assets (policy, name and quantity) for a given address.

    :param str address: wallet used public address
    return: list of all the assets
    :rtype: list.
    """
    get_format = {"_addresses": [args] }
    addresses = requests.post(self.ADDRESS_ASSETS_URL, json= get_format , timeout=10)
    addresses = json.loads(addresses.content)
    return addresses


def get_credential_txs(self, payment_credentials, after_block=0):
    """
    Get the transaction hash list of input payment credential array (stake key), optionally
    filtering after specified block height (inclusive).

    :param str payment_credentials: list address payment credential array (stake key)
    :param int after_block: filtering after block (inclusive) defaul is 0, from the beginning
    :return: hash list of address transactions.
    :rtype: list.
    """
    get_format = {"_payment_credentials":[payment_credentials], "_after_block_height": after_block}
    hash_list = requests.post(self.CREDENTIAL_TXS_URL, json = get_format, timeout=10)
    hash_list  = json.loads(hash_list.content)
    return hash_list
