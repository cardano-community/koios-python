#!/usr/bin/env python
"""
Provides all transactions functions
"""
import json
import requests
from .environment import *

@Exception_Handler
def get_tx_info(self, *args):
    """
    Get detailed information about transaction(s).

    :param list tx_hash: list of transaction(s) hash to search and read data.
    :return: list of all info about transaction(s).
    :rtype: list.
    """
    timeout = get_timeout()
    get_format = {"_tx_hashes": [args]}
    tx_info = requests.post(self.TX_INFO_URL, json = get_format, timeout=timeout)
    tx_info  = json.loads(tx_info.content)
    return tx_info 

# def get_tx_info(self, *args):
#     """
#     Get detailed information about transaction(s).

#     :param list tx_hash: list of transaction(s) hash to search and read data.
#     :return: list of all info about transaction(s).
#     :rtype: list.
#     """
#     timeout = BASE_TIMEOUT

#     while True:
#         try:
#             get_format = {"_tx_hashes": [args]}
#             tx_info = requests.post(self.TX_INFO_URL, json = get_format, timeout=timeout)
#             tx_info  = json.loads(tx_info.content)
#             break

#         except requests.exceptions.ReadTimeout as timeout_error:
#             print(f"Exception: {timeout_error}")
#             if timeout < LIMIT_TIMEOUT:
#                 timeout= timeout + 10
#             else:
#                 print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
#                 break
#             print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

#     return tx_info

@Exception_Handler
def get_tx_utxos(self, *args):
    """
    Get UTxO set (inputs/outputs) of transactions.

    :param list tx_hash: list of transaction(s) hash to search and read utxos data.
    :return: all info about utxos in transaction(s)
    :rtype: list.
    """
    timeout = get_timeout()
    get_format = {"_tx_hashes": [args]}
    tx_utxos = requests.post(self.TX_UTXOS_URL, json = get_format, timeout=timeout)
    tx_utxos  = json.loads(tx_utxos.content)
    return tx_utxos

# def get_tx_utxos(self, *args):
#     """
#     Get UTxO set (inputs/outputs) of transactions.

#     :param list tx_hash: list of transaction(s) hash to search and read utxos data.
#     :return: all info about utxos in transaction(s)
#     :rtype: list.
#     """
#     timeout = BASE_TIMEOUT

#     while True:
#         try:
#             get_format = {"_tx_hashes": [args]}
#             tx_utxos = requests.post(self.TX_UTXOS_URL, json = get_format, timeout=timeout)
#             tx_utxos  = json.loads(tx_utxos.content)
#             break

#         except requests.exceptions.ReadTimeout as timeout_error:
#             print(f"Exception: {timeout_error}")
#             if timeout < LIMIT_TIMEOUT:
#                 timeout= timeout + 10
#             else:
#                 print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
#                 break
#             print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

#     return tx_utxos

@Exception_Handler
def get_tx_metadata(self, *args):
    """
    Get metadata information (if any) for given transaction(s).

    :param list tx_hash: list strings of transaction(s) hash to search and read utxos data.
    :return: list of all info about utxos in transaction(s)
    :rtype: list.
    """
    timeout = get_timeout()
    get_format = {"_tx_hashes": [args]}
    tx_metadata = requests.post(self.TX_METADATA_URL, json = get_format, timeout=timeout)
    tx_metadata  = json.loads(tx_metadata.content)
    return tx_metadata

# def get_tx_metadata(self, *args):
#     """
#     Get metadata information (if any) for given transaction(s).

#     :param list tx_hash: list strings of transaction(s) hash to search and read utxos data.
#     :return: list of all info about utxos in transaction(s)
#     :rtype: list.
#     """
#     timeout = BASE_TIMEOUT

#     while True:
#         try:
#             get_format = {"_tx_hashes": [args]}
#             tx_metadata = requests.post(self.TX_METADATA_URL, json = get_format, timeout=timeout)
#             tx_metadata  = json.loads(tx_metadata.content)
#             break
#         except requests.exceptions.ReadTimeout as timeout_error:
#             print(f"Exception: {timeout_error}")
#             if timeout < LIMIT_TIMEOUT:
#                 timeout= timeout + 10
#             else:
#                 print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
#                 break
#             print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

#     return tx_metadata

@Exception_Handler
def get_tx_metalabels(self, content_range="0-999"):
    """
    Get a list of all transaction metalabels.

    :param str range: paginated content range, up to  1000 records.
    :return: list of metalabels transactions
    """
    timeout = get_timeout()
    custom_headers = {"Range": str(content_range)}
    tx_metalabels = requests.get(self.TX_METALABELS_URL, headers \
    = custom_headers, timeout=timeout)
    tx_metalabels  = json.loads(tx_metalabels.content)
    return tx_metalabels

# def get_tx_metalabels(self, content_range="0-999"):
#     """
#     Get a list of all transaction metalabels.

#     :param str range: paginated content range, up to  1000 records.
#     :return: list of metalabels transactions
#     """
#     timeout = BASE_TIMEOUT

#     while True:
#         try:
#             custom_headers = {"Range": str(content_range)}
#             tx_metalabels = requests.get(self.TX_METALABELS_URL, headers \
#             = custom_headers, timeout=timeout)
#             tx_metalabels  = json.loads(tx_metalabels.content)
#             break

#         except requests.exceptions.ReadTimeout as timeout_error:
#             print(f"Exception: {timeout_error}")
#             if timeout < LIMIT_TIMEOUT:
#                 timeout= timeout + 10
#             else:
#                 print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
#                 break
#             print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

#     return tx_metalabels

@Exception_Handler
def submit_tx(self, file):
    """
    Submit an already serialized transaction to the network. You have to serialized the transaction
    file with: xxd -r -p <<< $(jq .cborHex signed.txt) > signed.cbor

    :param file: a file with raw binary serialized transaction on the file-system.
    :return: hex transaction ID (if is successful )
    """
    timeout = get_timeout()
    with open(file, "rb") as cbor_tx:
        cbor_tx = cbor_tx.read()
    cbor_header = {'Content-Type': 'application/cbor'}
    submit = requests.post(self.SUBMIT_TX_URL, headers = cbor_header, \
        data = cbor_tx, timeout=timeout)
    submit  = json.loads(submit.content)
    return submit
    

# def submit_tx(self, file):
#     """
#     Submit an already serialized transaction to the network. You have to serialized the transaction
#     file with: xxd -r -p <<< $(jq .cborHex signed.txt) > signed.cbor

#     :param file: a file with raw binary serialized transaction on the file-system.
#     :return: hex transaction ID (if is successful )
#     """
#     with open(file, "rb") as cbor_tx:
#         cbor_tx = cbor_tx.read()
#     cbor_header = {'Content-Type': 'application/cbor'}
#     submit = requests.post(self.SUBMIT_TX_URL, headers = cbor_header, \
#         data = cbor_tx, timeout=25)
#     submit  = json.loads(submit.content)
#     return submit

@Exception_Handler
def get_tx_status(self, *args):
    """
    Get the number of block confirmations for a given transaction hash list.

    :param list tx_hash: list of transaction(s) hash to search and read utxos data.
    :return: list of all info about utxos in transaction(s)
    :rtype: list.
    """
    timeout = get_timeout()
    get_format = {"_tx_hashes": [args]}
    tx_status = requests.post(self.TX_STATUS_URL, json = get_format, timeout=timeout)
    tx_status  = json.loads(tx_status.content)
    return tx_status

# def get_tx_status(self, *args):
#     """
#     Get the number of block confirmations for a given transaction hash list.

#     :param list tx_hash: list of transaction(s) hash to search and read utxos data.
#     :return: list of all info about utxos in transaction(s)
#     :rtype: list.
#     """
#     timeout = BASE_TIMEOUT

#     while True:
#         try:
#             get_format = {"_tx_hashes": [args]}
#             tx_status = requests.post(self.TX_STATUS_URL, json = get_format, timeout=timeout)
#             tx_status  = json.loads(tx_status.content)
#             break

#         except requests.exceptions.ReadTimeout as timeout_error:
#             print(f"Exception: {timeout_error}")
#             if timeout < LIMIT_TIMEOUT:
#                 timeout= timeout + 10
#             else:
#                 print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
#                 break
#             print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

#     return tx_status
    