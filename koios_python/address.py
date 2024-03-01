#!/usr/bin/env python
"""
Provides all address functions
"""
import json
import requests
from .environment import *


@Exception_Handler
def get_address_info(self, *args):
    """
    Get address info - balance, associated stake address (if any) and UTxO set.

    :param str address: wallet used public address(es).
    return: list with data of this used public address.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_addresses": [args] }
        addresses = requests.post(self.ADDRESS_INFO_URL, json= get_format, timeout=timeout)
        addresses = json.loads(addresses.content)
    else:
        get_format = {"_addresses": [args] }
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        addresses = requests.post(self.ADDRESS_INFO_URL, json= get_format, timeout=timeout, headers=custom_headers)
        addresses = json.loads(addresses.content)

    return addresses


@Exception_Handler
def get_address_utxos(self, *addresses, extended=False, content_range="0-999"):
    """
    Get the UTxO set for a given address.

    :param list address: Array of Cardano payment address(es)
    :param bool extended: extended flag to toggle additional fields (optional, default is False)
    return: list of utxos
    :rtype: list.
    """

    if self.BEARER is None and extended is True:
        extended = "true"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range)}
        get_format = {"_addresses": [addresses], "_extended": extended}
        utxos = requests.post(self.ADDRESS_UTXOS_URL, json = get_format, headers=custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)

    if  self.BEARER is None and extended is False:
        extended = "false"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range)}
        get_format = {"_addresses": [addresses], "_extended": extended}
        utxos = requests.post(self.ADDRESS_UTXOS_URL, json = get_format, headers=custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)

    if self.BEARER is not None and extended is True:
        extended = "true"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_addresses": [addresses], "_extended": extended}
        utxos = requests.post(self.ADDRESS_UTXOS_URL, json = get_format, headers=custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)

    if self.BEARER is not None and extended is False:
        extended = "false"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_addresses": [addresses], "_extended": extended}
        utxos = requests.post(self.ADDRESS_UTXOS_URL, json = get_format, headers=custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)
        
    return utxos


@Exception_Handler
def get_credential_utxos(self, *payment_credentials, extended=False, content_range="0-999"):
    """
    Get a list of UTxO against input payment credential array including their balances.
    
    :param str payment_credentials
    :return: list of utxos
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and extended is True:
        extended = "true"
        custom_headers = {"Range": str(content_range)}
        get_format = {"_payment_credentials":[payment_credentials], "_extended": extended}
        utxos = requests.post(self.ADDRESS_CREDENTIAL_UTXOS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)
    
    if self.BEARER is not None and extended is True:
        extended = "true"
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_payment_credentials":[payment_credentials], "_extended": extended}
        utxos = requests.post(self.ADDRESS_CREDENTIAL_UTXOS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)

    if self.BEARER is None and extended is False:
        extended = "false"
        custom_headers = {"Range": str(content_range)}
        get_format = {"_payment_credentials":[payment_credentials], "_extended": extended}
        utxos = requests.post(self.ADDRESS_CREDENTIAL_UTXOS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)
    
    if self.BEARER is not None and extended is False:
        extended = "false"
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_payment_credentials":[payment_credentials], "_extended": extended}
        utxos = requests.post(self.ADDRESS_CREDENTIAL_UTXOS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)
    
    return utxos


@Exception_Handler
def get_address_txs(self, *address_tx, after_block=0):
    """
    Get the transaction hash list of input address array, optionally filtering after specified
    block height (inclusive)

    :param tx_hash: list or single transaction hash to search and read utxos data
    :param after_block: filtering after block (inclusive) defaul is 0, from the beginning
    :return: hash list of address transactions
    """
    timeout = get_timeout()

    if self.BEARER is None: 
        get_format = {"_addresses": [address_tx], "_after_block_height": str(after_block)}
        hash_list = requests.post(self.ADDRESS_TXS_URL, json = get_format, timeout=timeout)
        hash_list  = json.loads(hash_list.content)
    
    if self.BEARER is not None:
        get_format = {"_addresses": [address_tx], "_after_block_height": str(after_block)}
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        hash_list = requests.post(self.ADDRESS_TXS_URL, json = get_format, headers=custom_headers, timeout=timeout)
        hash_list  = json.loads(hash_list.content)

    return hash_list


@Exception_Handler
def get_credential_txs(self, *payment_credentials, after_block_height=0, content_range="0-999"):
    """
    Get the transaction hash list of input payment credential array (stake key), optionally
    filtering after specified block height (inclusive).

    :param str payment_credentials: list address payment credential array (stake key)
    :param int after_block: filtering after block (inclusive) defaul is 0, from the beginning
    :return: hash list of address transactions.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        get_format = {"_payment_credentials": [payment_credentials], "_after_block_height": str(after_block_height)}
        txs_list = requests.post(self.ADDRESS_CREDENTIAL_TXS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        txs_list = json.loads(txs_list.content)
    
    if self.BEARER is not None:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_payment_credentials": [payment_credentials], "_after_block_height": str(after_block_height)}
        txs_list = requests.post(self.ADDRESS_CREDENTIAL_TXS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        txs_list = json.loads(txs_list.content)

    return txs_list


@Exception_Handler
def get_address_assets(self, *args):
    """
    Get the list of all the assets (policy, name and quantity) for a given address.

    :param str address: wallet used public address
    return: list of all the assets
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_addresses": [args]}
        assets = requests.post(self.ADDRESS_ASSETS_URL, json = get_format, timeout=timeout)
        assets = json.loads(assets.content)

    if self.BEARER is not None:
        get_format = {"_addresses": [args]}
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        assets = requests.post(self.ADDRESS_ASSETS_URL, json = get_format, headers=custom_headers, timeout=timeout)
        assets = json.loads(assets.content)

    return assets