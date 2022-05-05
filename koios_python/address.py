#!/usr/bin/env python

import json
import requests


def get_address_info(address):
    """
    Get address info - balance, associated stake address (if any) and UTxO set
    param: wallet used public address
    return: list with data of this used public address
    """
    info = requests.get("https://api.koios.rest/api/v0/address_info?_address="+str(address))
    info = json.loads(info.content)
    return info


def get_address_txs(tx_hash, after_block=0):
    """
    Get the number of block confirmations for a given transaction hash list.

    :param tx_hash: list or single transaction hash to search and read utxos data
    :param after_block: filtering after block (inclusive) defaul is 0, from the beginning
    :return: hash list of address transactions
    """
    get_format = {"_addresses":[tx_hash], "_after_block_height": after_block}
    hash_list = requests.post( "https://api.koios.rest/api/v0/address_txs", json = get_format)
    hash_list  = json.loads(hash_list.content)
    return hash_list


def get_address_assets(address):
    """
    Get the list of all the assets (policy, name and quantity) for a given address.

    param: wallet used public address
    return: list of all the assets
    """
    info = requests.get("https://api.koios.rest/api/v0/address_assets?_address="+str(address))
    info = json.loads(info.content)
    return info


def get_credential_txs(payment_credentials, after_block=0):
    """
    Get the transaction hash list of input payment credential array (stake key), optionally 
    filtering after specified block height (inclusive).

    :param payment_credentials: list address payment credential array (stake key)
    :param after_block: filtering after block (inclusive) defaul is 0, from the beginning
    :return: hash list of address transactions
    """
    get_format = {"_payment_credentials":[payment_credentials], "_after_block_height": after_block}
    hash_list = requests.post( "https://api.koios.rest/api/v0/credential_txs", json = get_format)
    hash_list  = json.loads(hash_list.content)
    return hash_list