#!/usr/bin/env python

import json
import requests


def get_pool_list():
    """
    Get a list of all currently registered/retiring (not retired) pools.

    :return: list of all registered/retiring pools.
    :rtype: list.
    """
    pool_list = requests.get("https://api.koios.rest/api/v0/pool_list")
    pool_list = json.loads(pool_list.content)
    return pool_list


def get_pool_info(pool_bech32):
    """
    Get current pool status and details for a specified pool.

    :param str pool_bech32: pool IDs in bech32 format (pool1...)
    :return: list of pool information.
    :rtype: list.
    """
    get_format = {"_pool_bech32_ids": [pool_bech32]}
    pool_list = requests.post( "https://api.koios.rest/api/v0/pool_info", json = get_format)
    pool_list  = json.loads(pool_list.content)
    return pool_list
   

def get_pool_delegators(pool_bech32, epoch_no="current"):
    """
    Get information about delegators by a given pool and optional epoch (current if omitted).

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (current if omitted).
    :return: list of pool delegators information.
    :rtype: list.
    """
    if epoch_no == "current":
        info = requests.get("https://api.koios.rest/api/v0/pool_delegators?_pool_bech32=" \
        + pool_bech32)
        info = json.loads(info.content)
    else:
        info = requests.get("https://api.koios.rest/api/v0/pool_delegators?_pool_bech32=" \
        +  pool_bech32 + "&_epoch_no=" + str(epoch_no))
        info = json.loads(info.content)
    return info


def get_pool_blocks(pool_bech32, epoch_no="beginning"):
    """
    Get information about pool stake, block and reward history in a given epoch _epoch_no
    (or all epochs that pool existed for, in descending order if no _epoch_no was provided)

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (from the beginning if omitted).
    :return: list of blocks created by pool.
    :rtype: list.s
    """
    if epoch_no == "beginning":
        info = requests.get("https://api.koios.rest/api/v0/pool_blocks?_pool_bech32=" \
        + pool_bech32)
        info = json.loads(info.content)
    else:
        info = requests.get("https://api.koios.rest/api/v0/pool_blocks?_pool_bech32=" \
        + pool_bech32 + "&_epoch_no=" + str(epoch_no))
        info = json.loads(info.content)
    return info


def get_pool_history(pool_bech32, epoch_no="history"):
    """
    Get information about all blocks minted by a given pool from the beginning (or specific epoch
    if provided).

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (from the beginning if omitted).
    :return: list of blocks created by pool.
    :rtype: list.
    """
    if epoch_no == "history":
        info = requests.get("https://api.koios.rest/api/v0/pool_history?_pool_bech32=" \
        + str(pool_bech32))
        info = json.loads(info.content)
    else:
        info = requests.get("https://api.koios.rest/api/v0/pool_history?_pool_bech32=" \
        + str(pool_bech32) + "&_epoch_no=" + str(epoch_no))
        info = json.loads(info.content)
    return info


def get_pool_updates(pool_bech32=None):
    """
    Get all pool updates for all pools or only updates for specific pool if specified.

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :return: list of historical pool updates.
    :rtype: list.
    """
    if pool_bech32 is None:
        pool_list = requests.get("https://api.koios.rest/api/v0/pool_updates")
        pool_list  = json.loads(pool_list.content)
    else:
        pool_list = requests.get("https://api.koios.rest/api/v0/pool_updates?_pool_bech32=" \
        + pool_bech32)
        pool_list  = json.loads(pool_list.content)
    return pool_list


def get_pool_relays():
    """
    Get a list of registered relays for all currently registered/retiring (not retired) pools.

    :return: list of pool relay information.
    :rtype: list.
    """
    pool_list = requests.get("https://api.koios.rest/api/v0/pool_relays")
    pool_list  = json.loads(pool_list.content)
    return pool_list


def get_pool_metadata(pool_bech32=None):
    """
    Get Metadata (on & off-chain) for all currently registered/retiring (not retired) pools.

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :return: list of pool metadata.
    :rtype: list.
    """
    if pool_bech32 is None:
        pool_list = requests.post("https://api.koios.rest/api/v0/pool_metadata")
        pool_list  = json.loads(pool_list.content)
    else:
        get_format = {"_pool_bech32_ids": [pool_bech32]}
        pool_list = requests.post("https://api.koios.rest/api/v0/pool_metadata" \
        , json = get_format)
        pool_list  = json.loads(pool_list.content)
    return pool_list
