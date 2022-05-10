#!/usr/bin/env python
"""
Provides all block functions
"""
import json
import requests
from .urls import BLOCK_INFO_URL, BLOCK_TXS_URL, BLOCKS_URL

def get_blocks(content_range="0-999"):
    """
    Get summarised details about all blocks (paginated - latest first).

    :param str range: paginated content range, up to  1000 records.
    :return: list of all blocks.
    :rtype: list
    """
    custom_headers = {"Range": str(content_range)}
    blocks = requests.get(BLOCKS_URL, headers = custom_headers)
    blocks = json.loads(blocks.content)
    return blocks


def get_block_info(block_hash):
    """
    Get detailed information about a specific block.

    :param str block_hash: block hash ID.
    :return:  list of detailed block information.
    :rtype: list
    """
    get_format = {"_block_hashes":[block_hash]}
    block = requests.post(BLOCK_INFO_URL, json = get_format)
    block = json.loads(block.content)
    return block


def get_block_txs(block_hash):
    """
    Get a list of all transactions included in a provided block.

    :param str block_hash: block hash ID.
    :return: list of transactions hashes.
    :rtype: list
    """
    block = requests.get(BLOCK_TXS_URL + str(block_hash))
    block = json.loads(block.content)
    return block
