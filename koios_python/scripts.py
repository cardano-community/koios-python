#!/usr/bin/env python
"""
Provides all scripts functions
"""
import json
from time import sleep
import requests
from .environment import *

@Exception_Handler
def get_native_script_list(self, content_range="0-999"):
    """
    Get list of all existing native script hashes along with their creation transaction hashes

    :param str range: paginated content range, up to  1000 records.
    return: list of native script and creation tx hash pairs.
    :rtype: list.
    """
    timeout = get_timeout()
    custom_headers = {"Range": str(content_range)}
    get_format = requests.post(self.NATIVE_SCRIPT_LIST_URL, headers = custom_headers, timeout=timeout)
    get_format = json.loads(get_format.content)
    return get_format


@Exception_Handler
def get_plutus_script_list(self, content_range="0-999"):
    """
    Get list of all existing Plutus script hashes along with their creation transaction hashes.

    :param str range: paginated content range, up to  1000 records.
    return: list of Plutus script and creation tx hash pairs.
    :rtype: list.
    """
    timeout = get_timeout()
    custom_headers = {"Range": str(content_range)}
    get_format = requests.post(self.PLUTUS_SCRIPT_LIST_URL, headers = custom_headers, timeout=timeout)
    get_format = json.loads(get_format.content)
    return get_format


@Exception_Handler
def get_script_redeemers(self, script_hash):
    """
    Get list of all redeemers for a given script hash.

    :params string script_hash: script hash in hexadecimal format (hex) to search and read data.
    :return: list of all redeemers for a given script hash.
    :rtype: list.
    """
    timeout = get_timeout()
    query = requests.get(self.SCRIPT_REDEEMERS_URL + script_hash, timeout=timeout)
    query  = json.loads(query.content)
    return query


@Exception_Handler
def get_datum_info(self, *datum_hash):
    '''
    Get list of datum information for given datum hashes

    :params string datum_hash: The Hash of the Plutus Data.
    :return: the actual data in json form.
    :rtype: list.
    '''
    timeout = get_timeout()
    custom_headers = {"_datum_hashes": [datum_hash]}
    get_format = requests.post(self.DATUM_INFO_URL, json = custom_headers, timeout=timeout)
    get_format = json.loads(get_format.content)
    return get_format