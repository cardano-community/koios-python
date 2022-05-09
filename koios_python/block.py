#!/usr/bin/env python

import json
import requests


def get_blocks():
    """
    Get summarised details about all blocks (paginated - latest first).

    :return: list of all blocks.
    :rtype: list
    """
    blocks = requests.get("https://api.koios.rest/api/v0/blocks")
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
    block = requests.post("https://api.koios.rest/api/v0/block_info", json = get_format)
    block = json.loads(block.content)
    return block


def get_block_txs(block_hash):
    """
    Get a list of all transactions included in a provided block
    :param str block_hash: block hash ID.
    :return: list of transactions hashes.
    :rtype: list
    """
    block = requests.get("https://api.koios.rest/api/v0/block_txs?_block_hash="+str(block_hash))
    block = json.loads(block.content)[0]
    return
