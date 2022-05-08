#!/usr/bin/env python

import json
import requests


def get_native_script_list():
    """
    Get list of all existing native script hashes along with their creation transaction hashes

    return: list of native script and creation tx hash pairs.
    :rtype: list.
    """
    get_format = requests.post( "https://api.koios.rest/api/v0/native_script_list")
    get_format  = json.loads(get_format.content)
    return get_format


def get_plutus_script_list():
    """
    Get list of all existing Plutus script hashes along with their creation transaction hashes.

    return: list of Plutus script and creation tx hash pairs.
    :rtype: list.
    """
    get_format = requests.post( "https://api.koios.rest/api/v0/plutus_script_list")
    get_format  = json.loads(get_format.content)
    return get_format


def get_script_redeemers(script_hash):
    """
    Get list of all redeemers for a given script hash.

    :params string script_hash: script hash in hexadecimal format (hex) to search and read data.
    :return: list of all redeemers for a given script hash.
    :rtype: list.
    """
    query = requests.get( "https://api.koios.rest/api/v0/script_redeemers?_script_hash="+ script_hash )
    query  = json.loads(query.content)
    return query
