#!/usr/bin/env python

import json
import requests


def get_account_list():
    """
    Get a list of all accounts.
    
    return: string list of account (stake address: stake1... format) IDs
    """
    info = requests.get("https://api.koios.rest/api/v0/account_list")
    info = json.loads(info.content)
    return info
