#!/usr/bin/env python

import json
import requests


def get_tx(tx_hash):
    """
    Get Tx data
    params:
    return: 
    """
    tx = {"_tx_hashes":[tx_hash]}
    koios_post = requests.post( "https://api.koios.rest/api/v0/tx_info", json = tx)
    koios_post = json.loads(koios_post.content)[0]
    print(koios_post)
