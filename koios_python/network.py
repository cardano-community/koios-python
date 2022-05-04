#!/usr/bin/env python

import json
import requests

def get_tip():
    """
    Get the tip info about the latest block seen by chain
    :return: Blockchain tip data
    """
    tip = requests.get("https://api.koios.rest/api/v0/tip")
    #confirmar que es correcto codigo 200
    #tip = tip.json
    tip = json.loads(tip.content)
    return tip


def get_genesis():
    """
    Get the Genesis parameters used to start specific era on chain
    :return: Genesis block data
    """
    genesis = requests.get("https://api.koios.rest/api/v0/genesis")
    genesis = json.loads(genesis.content)
    return genesis


def get_totals(epoch_no):
    """
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified \
    epoch, all epochs if empty
     :param stake_address: The stake addresse
    :return: Blockchain tip data
    """
    totals = requests.get("https://api.koios.rest/api/v0/totals?_epoch_no="+str(epoch_no))
    totals = json.loads(totals.content)[0]
    return totals
    