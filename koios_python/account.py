#!/usr/bin/env python

import json
import requests


def get_account_list():
    """
    Get a list of all accounts.

    return: string list of account (stake address: stake1...  bech32 format) IDs
    """
    address_list = requests.get("https://api.koios.rest/api/v0/account_list")
    address_list = json.loads(address_list.content)
    return address_list
