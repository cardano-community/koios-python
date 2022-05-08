#!/usr/bin/env python

import json
import requests


def get_tx_info(tx_hash):
    """
    Get detailed information about transaction(s).

    :param str tx_hash: transaction hash to search and read data
    :return: list of all info about transaction(s)
    """
    get_format = {"_tx_hashes":[tx_hash]}
    tx_info = requests.post( "https://api.koios.rest/api/v0/tx_info", json = get_format)
    tx_info  = json.loads(tx_info.content)[0]
    return tx_info


def get_tx_utxos(tx_hash):
    """
    Get UTxO set (inputs/outputs) of transactions.

    :param str tx_hash: transaction hash to search and read utxos data
    :return: all info about utxos in transaction(s)
    """
    get_format = {"_tx_hashes":[tx_hash]}
    tx_utxos = requests.post("https://api.koios.rest/api/v0/tx_utxos", json = get_format)
    tx_utxos  = json.loads(tx_utxos.content)[0]
    return tx_utxos


def get_tx_metadata(tx_hash):
    """
    Get metadata information (if any) for given transaction(s).

    :param str tx_hash: transaction hash to search and read utxos data
    :return: list of all info about utxos in transaction(s)
    """
    get_format = {"_tx_hashes":[tx_hash]}
    tx_metadata = requests.post("https://api.koios.rest/api/v0/tx_metadata", json = get_format)
    tx_metadata  = json.loads(tx_metadata.content)[0]
    return tx_metadata

def get_tx_metalabels():
    """
    Get a list of all transaction metalabels.

    :param: None
    :return: list of metalabels transactions
    """
    tx_metalabels = requests.get("https://api.koios.rest/api/v0/tx_metalabels")
    tx_metalabels  = json.loads(tx_metalabels.content)
    return tx_metalabels

######## HAY QUE PROBARLA CON UNA TRANSACCION
def submit_tx(file):
    """
    Submit an already serialized transaction to the network. You have to serialized the transaction
    file with: xxd -r -p <<< $(jq .cborHex signed.txt) > signed.cbor

    :param file: a file with raw binary serialized transaction on the file-system.
    :return: hex transaction ID (if is successful )
    """
    cbor_tx = open(file, "rb")
    cbor_tx = cbor_tx.read()
    cbor_header = {'Content-Type': 'application/cbor'}
    submit = requests.post("https://api.koios.rest/api/v0/submittx", headers = cbor_header, data = cbor_tx)
    submit  = json.loads(submit.content)
    return submit


def get_tx_status(tx_hash):
    """
    Get the number of block confirmations for a given transaction hash list.

    :param str tx_hash: transaction hash to search and read utxos data
    :return: status of transaction(s)
    """
    get_format = {"_tx_hashes":[tx_hash]}
    tx_status = requests.post( "https://api.koios.rest/api/v0/tx_status", json = get_format)
    tx_status  = json.loads(tx_status.content)[0]
    return tx_status