#!/usr/bin/env python
"""
Provides all network functions
"""
import json
import requests
from .environment import BASE_TIMEOUT, LIMIT_TIMEOUT

def get_tip(self):
    """
    Get the tip info about the latest block seen by chain.

    :return: list of block summary (limit+paginated).
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            tip = requests.get(self.TIP_URL, timeout=timeout)
            tip = json.loads(tip.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return tip


def get_genesis(self):
    """
    Get the Genesis parameters used to start specific era on chain.

    :return: list of genesis parameters used to start each era on chain.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            genesis = requests.get(self.GENESIS_URL, timeout=timeout)
            genesis = json.loads(genesis.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return genesis


def get_totals(self, epoch_no=None):
    """
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified
    epoch, all epochs if empty.

    :param int epoch_no: Epoch Number to fetch details for.
    :return: list of of supply/reserves/utxo/fees/treasury stats.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            if epoch_no is None:
                totals = requests.get(self.TOTALS_URL, timeout=10)
                totals = json.loads(totals.content)
            else:
                totals = requests.get(f"{self.TOTALS_URL}?_epoch_no={epoch_no}", timeout=timeout)
                totals = json.loads(totals.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return totals
    