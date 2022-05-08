#!/usr/bin/env python

import json
import requests

def get_tip():
    """
    Get the tip info about the latest block seen by chain.

    :return: list of block summary (limit+paginated).
    :rtype: list.
    """
    tip = requests.get("https://api.koios.rest/api/v0/tip")
    tip = json.loads(tip.content)
    return tip


def get_genesis():
    """
    Get the Genesis parameters used to start specific era on chain.

    :return: list of genesis parameters used to start each era on chain.
    :rtype: list.
    """
    genesis = requests.get("https://api.koios.rest/api/v0/genesis")
    genesis = json.loads(genesis.content)
    return genesis


def get_totals(epoch_no=None):
    """
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified
    epoch, all epochs if empty.

    :param int epoch_no: Epoch Number to fetch details for.
    :return: list of of supply/reserves/utxo/fees/treasury stats.
    :rtype: list.
    """
    if epoch_no is None:
        totals = requests.get("https://api.koios.rest/api/v0/totals")
        totals = json.loads(totals.content)
    else:
        totals = requests.get("https://api.koios.rest/api/v0/totals?_epoch_no="+str(epoch_no))
        totals = json.loads(totals.content)
    return totals
    