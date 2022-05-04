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


def get_tx_utxos(tx_hash):
    """
    Get UTxO set (inputs/outputs) of transactions.
    params: transaction hash to search and read utxos data
    return: all info about utxos in transaction(s)
    """
    get_format = {"_tx_hashes":[tx_hash]}
    tx_utxos = requests.post( "https://api.koios.rest/api/v0/tx_utxos", json = get_format)
    tx_utxos  = json.loads(tx_utxos.content)[0]
    return tx_utxos


def get_tx_metadata(tx_hash):
    """
    Get metadata information (if any) for given transaction(s)
    params: transaction hash to search and read utxos data
    return: all info about utxos in transaction(s)
    """
    get_format = {"_tx_hashes":[tx_hash]}
    tx_metadata = requests.post( "https://api.koios.rest/api/v0/tx_metadata", json = get_format)
    tx_metadata  = json.loads(tx_metadata.content)[0]
    return tx_metadata