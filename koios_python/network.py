#!/usr/bin/env python
"""
Provides all network functions
"""
import json
import requests
# from .urls import GENESIS_URL, TIP_URL, TOTALS_URL

def get_tip(self):
    """
    Get the tip info about the latest block seen by chain.

    :return: list of block summary (limit+paginated).
    :rtype: list.
    """
    tip = requests.get(self.TIP_URL, timeout=10)
    tip = json.loads(tip.content)
    return tip


def get_genesis(self):
    """
    Get the Genesis parameters used to start specific era on chain.

    :return: list of genesis parameters used to start each era on chain.
    :rtype: list.
    """
    genesis = requests.get(self.GENESIS_URL, timeout=10)
    genesis = json.loads(genesis.content)
    return genesis


def get_totals(self, epoch_no=None):
    """
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified
    epoch, all epochs if empty.

    :param int epoch_no: Epoch Number to fetch details for.
    :return: list of of supply/reserves/utxo/fees/treasury stats.
    :rtype: list.
    """
    if epoch_no is None:
        totals = requests.get(self.TOTALS_URL, timeout=10)
        totals = json.loads(totals.content)
    else:
        totals = requests.get(f"{self.TOTALS_URL}?_epoch_no={epoch_no}", timeout=10)
        totals = json.loads(totals.content)
    return totals
    