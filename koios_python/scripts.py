#!/usr/bin/env python
"""
Provides all scripts functions
"""
import json
import requests


def get_native_script_list(self, content_range="0-999"):
    """
    Get list of all existing native script hashes along with their creation transaction hashes

    :param str range: paginated content range, up to  1000 records.
    return: list of native script and creation tx hash pairs.
    :rtype: list.
    """
    custom_headers = {"Range": str(content_range)}
    get_format = requests.post(self.NATIVE_SCRIPT_LIST_URL, headers = custom_headers, timeout=30)
    get_format = json.loads(get_format.content)
    return get_format


def get_plutus_script_list(self, content_range="0-999"):
    """
    Get list of all existing Plutus script hashes along with their creation transaction hashes.

    :param str range: paginated content range, up to  1000 records.
    return: list of Plutus script and creation tx hash pairs.
    :rtype: list.
    """
    custom_headers = {"Range": str(content_range)}
    get_format = requests.post(self.PLUTUS_SCRIPT_LIST_URL, headers = custom_headers, timeout=30)
    get_format = json.loads(get_format.content)
    return get_format


def get_script_redeemers(self, script_hash):
    """
    Get list of all redeemers for a given script hash.

    :params string script_hash: script hash in hexadecimal format (hex) to search and read data.
    :return: list of all redeemers for a given script hash.
    :rtype: list.
    """
    query = requests.get(self.SCRIPT_REDEEMERS_URL + script_hash, timeout=30)
    query  = json.loads(query.content)
    return query
