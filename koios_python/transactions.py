#!/usr/bin/env python

import json
import requests


def get_tx_info(tx_hash):
    """
    Get detailed information about transaction(s)
    params: transaction hash to search and read data
    return: all info about transaction(s)
    """
    get_format = {"_tx_hashes":[tx_hash]}
    tx_info = requests.post( "https://api.koios.rest/api/v0/tx_info", json = get_format)
    tx_info  = json.loads(tx_info.content)[0]
    return tx_info
