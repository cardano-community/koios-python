#!/usr/bin/env python
"""
Provides all block functions
"""
import json
import requests
from .environment import *

@Exception_Handler
def get_blocks(self,content_range="0-999"):
    """
    Get summarised details about all blocks (paginated - latest first).

    :param str range: paginated content range, up to  1000 records.
    :return: list of all blocks.
    :rtype: list
    """
    blocks = requests.get(self.BLOCKS_URL)
    blocks = json.loads(blocks.content)
    return blocks 

# def get_blocks(self,content_range="0-999"):
    """
    Get summarised details about all blocks (paginated - latest first).

    :param str range: paginated content range, up to  1000 records.
    :return: list of all blocks.
    :rtype: list
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            custom_headers = {"Range": str(content_range)}
            blocks = requests.get(self.BLOCKS_URL, headers = custom_headers, timeout=timeout)
            blocks = json.loads(blocks.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return blocks

@Exception_Handler
def get_block_info(self,*block_hash):
    """
    Get detailed information about a specific block or blocks

    :param str block_hash: block/s hash ID.
    :return:  list of detailed block information.
    :rtype: list
    """
    get_format = {"_block_hashes":[block_hash]}
    block = requests.post(self.BLOCK_INFO_URL, json = get_format)
    block = json.loads(block.content)
    return block

# def get_block_info(self,*block_hash):
    """
    Get detailed information about a specific block or blocks

    :param str block_hash: block/s hash ID.
    :return:  list of detailed block information.
    :rtype: list
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            get_format = {"_block_hashes":[block_hash]}
            block = requests.post(self.BLOCK_INFO_URL, json = get_format, timeout=timeout)
            block = json.loads(block.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return block

@Exception_Handler
def get_block_txs(self,*block_hash):
    """
    Get a list of all transactions included in a provided block.

    :param str block_hash: block hash ID.
    :return: list of transactions hashes.
    :rtype: list
    """
    get_format = {"_block_hashes":[block_hash]}
    txs = requests.post(self.BLOCK_TXS_URL, json = get_format)
    txs = json.loads(txs.content)
    return txs

# def get_block_txs(self,*block_hash):
    """
    Get a list of all transactions included in a provided block.

    :param str block_hash: block hash ID.
    :return: list of transactions hashes.
    :rtype: list
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            get_format = {"_block_hashes":[block_hash]}
            txs = requests.post(self.BLOCK_TXS_URL, json = get_format, timeout=timeout)
            txs = json.loads(txs.content)
            break
        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return txs
