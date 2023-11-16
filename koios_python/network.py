#!/usr/bin/env python
"""
Provides all network functions
"""
import json
import requests
from .environment import *

@Exception_Handler
def get_tip(self):
    """
    Get the tip info about the latest block seen by chain.

    :return: list of block summary (limit+paginated).
    :rtype: list.
    """
    timeout = get_timeout()
    tip = requests.get(self.TIP_URL, timeout=timeout)
    tip = json.loads(tip.content)
    return tip


@Exception_Handler
def get_genesis(self):
    """
    Get the Genesis parameters used to start specific era on chain.

    :return: list of genesis parameters used to start each era on chain.
    :rtype: list.
    """
    timeout = get_timeout()
    genesis = requests.get(self.GENESIS_URL, timeout=timeout)
    genesis = json.loads(genesis.content)
    return genesis


@Exception_Handler
def get_totals(self, epoch_no=None):
    """
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified
    epoch, all epochs if empty.

    :param int epoch_no: Epoch Number to fetch details for.
    :return: list of of supply/reserves/utxo/fees/treasury stats.
    :rtype: list.
    """
    timeout = get_timeout()
    if epoch_no is None:
        totals = requests.get(self.TOTALS_URL, timeout=timeout)
        totals = json.loads(totals.content)
    else:
        totals = requests.get(f"{self.TOTALS_URL}?_epoch_no={epoch_no}", timeout=timeout)
        totals = json.loads(totals.content)
    return totals

@Exception_Handler
def get_param_updates(self, content_range="0-57"):
    """
    Get all parameter update proposals submitted to the chain starting Shelley era

    :return: list of protocol parameters starting from Shelley era.
    :rtype: list
    """
    timeout = get_timeout()
    custom_headers = {"Range": str(content_range)}
    network_params = requests.get(self.NETWORK_PARAM_UPDATES_URL, headers=custom_headers, timeout=timeout)
    network_params = json.loads(network_params.content)
    return network_params
    
@Exception_Handler
def get_treasury_withdrawals(self, content_range="0-999"):
    """
    Get all treasury withdrawals from the chain starting Shelley era

    :return: list of treasury withdrawals starting from Shelley era.
    :rtype: list
    """
    timeout = get_timeout()
    custom_headers = {"Range": str(content_range)}
    treasury_withdrawals = requests.get(self.TREASURY_WITHDRAWALS_URL, headers=custom_headers, timeout=timeout)
    treasury_withdrawals = json.loads(treasury_withdrawals.content)
    return treasury_withdrawals

@Exception_Handler
def get_reserve_withdrawals(self, content_range="0-999"):
    """
    Get all reserve withdrawals from the chain starting Shelley era

    :return: list of reserve withdrawals starting from Shelley era.
    :rtype: list
    """
    timeout = get_timeout()
    reserve_withdrawals = requests.get(self.RESERVE_WITHDRAWALS_URL, timeout=timeout)
    reserve_withdrawals = json.loads(reserve_withdrawals.content)
    return reserve_withdrawals