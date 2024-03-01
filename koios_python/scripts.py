#!/usr/bin/env python
"""
Provides all scripts functions
"""
import json
from time import sleep
import requests
from .environment import *


@Exception_Handler
def get_script_info(self, *script_hashes, content_range="0-999"):
    """
    Get list of script information for given script hashes

    :params list script_hashes: Array of script hashes in hexadecimal format (hex) to search and read data.
    :return: list of script information for given script hashes.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        get_format = {"_script_hashes": [script_hashes]}
        script_info = requests.post(self.SCRIPT_INFO_URL, json = get_format, timeout=timeout, headers=custom_headers)
        script_info = json.loads(script_info.content)

    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_script_hashes": [script_hashes]}
        script_info = requests.post(self.SCRIPT_INFO_URL, json = get_format, headers = custom_headers, timeout=timeout)
        script_info = json.loads(script_info.content)

    return script_info


@Exception_Handler
def get_native_script_list(self, content_range="0-999"):
    """
    Get list of all existing native script hashes along with their creation transaction hashes

    :param str range: paginated content range, up to  1000 records.
    return: list of native script and creation tx hash pairs.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:    
        custom_headers = {"Range": str(content_range)}
        script_list = requests.post(self.NATIVE_SCRIPT_LIST_URL, headers = custom_headers, timeout=timeout)
        script_list = json.loads(script_list.content)

    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        script_list = requests.post(self.NATIVE_SCRIPT_LIST_URL, headers = custom_headers, timeout=timeout)
        script_list = json.loads(script_list.content)
    
    return script_list


@Exception_Handler
def get_plutus_script_list(self, content_range="0-999"):
    """
    Get list of all existing Plutus script hashes along with their creation transaction hashes.

    :param str range: paginated content range, up to  1000 records.
    return: list of Plutus script and creation tx hash pairs.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        script_list = requests.post(self.PLUTUS_SCRIPT_LIST_URL, headers = custom_headers, timeout=timeout)
        script_list = json.loads(script_list.content)

    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        script_list = requests.post(self.PLUTUS_SCRIPT_LIST_URL, headers = custom_headers, timeout=timeout)
        script_list = json.loads(script_list.content)

    return script_list


@Exception_Handler
def get_script_redeemers(self, script_hash, content_range="0-999"):
    """
    Get list of all redeemers for a given script hash.

    :params string script_hash: script hash in hexadecimal format (hex) to search and read data.
    :return: list of all redeemers for a given script hash.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        script_redeemers = requests.get(self.SCRIPT_REDEEMERS_URL + script_hash, timeout=timeout, headers = custom_headers)
        script_redeemers = json.loads(script_redeemers.content)

    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        script_redeemers = requests.get(self.SCRIPT_REDEEMERS_URL + script_hash, headers = custom_headers, timeout=timeout)
        script_redeemers = json.loads(script_redeemers.content)

    return script_redeemers


@Exception_Handler
def get_script_utxos(self, script_hash, extended=False, content_range="0-999"):
    """
    Get list of all UTxOs for a given script hash

    :params string script_hash: script hash in hexadecimal format (hex) to search and read data.
    :params bool extended: extended output format, default is False.
    :return: list of all UTxOs for a given script hash.
    :rtype: list.
    """

    if self.BEARER is None and extended is False:
        extended = "false"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range)}
        utxos_list = requests.get(f"{self.SCRIPT_UTXOS_URL}{script_hash}&_extended={extended}", timeout=timeout, headers = custom_headers)
        utxos_list  = json.loads(utxos_list.content)

    if self.BEARER is None and extended is True:
        extended = "true"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range)}
        utxos_list = requests.get(f"{self.SCRIPT_UTXOS_URL}{script_hash}&_extended={extended}", timeout=timeout, headers = custom_headers)
        utxos_list  = json.loads(utxos_list.content)

    if self.BEARER is not None and extended is False:
        extended = "false"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        utxos_list = requests.get(f"{self.SCRIPT_UTXOS_URL}{script_hash}&_extended={extended}", timeout=timeout, headers = custom_headers)
        utxos_list  = json.loads(utxos_list.content)

    if self.BEARER is not None and extended is True:
        extended = "true"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        utxos_list = requests.get(f"{self.SCRIPT_UTXOS_URL}{script_hash}&_extended={extended}", timeout=timeout, headers = custom_headers)
        utxos_list  = json.loads(utxos_list.content)

    return utxos_list



@Exception_Handler
def get_datum_info(self, *datum_hash):
    '''
    Get list of datum information for given datum hashes

    :params string datum_hash: The Hash of the Plutus Data.
    :return: the actual data in json form.
    :rtype: list.
    '''
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_datum_hashes": [datum_hash]}
        datum_info = requests.post(self.DATUM_INFO_URL, json = get_format, timeout=timeout)
        datum_info = json.loads(datum_info.content)

    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_datum_hashes": [datum_hash]}
        datum_info = requests.post(self.DATUM_INFO_URL, json = get_format, headers = custom_headers, timeout=timeout)
        datum_info = json.loads(datum_info.content)

    return datum_info
