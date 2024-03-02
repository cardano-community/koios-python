#!/usr/bin/env python
"""
Provides all pool functions
"""
import json
import requests
from .environment import *

@Exception_Handler
def get_pool_list(self, content_range="0-999"):
    """
    Get a list of all currently registered/retiring (not retired) pools.

    :param str range: paginated content range, up to  1000 records.
    :return: list of all registered/retiring pools.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        pool_list = requests.get(self.POOL_LIST_URL, headers = custom_headers, timeout=timeout)
        pool_list = json.loads(pool_list.content)

    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        pool_list = requests.get(self.POOL_LIST_URL, headers = custom_headers, timeout=timeout)
        pool_list = json.loads(pool_list.content)

    return pool_list


@Exception_Handler
def get_pool_info(self, *args):
    """
    Get current pool status and details for a specified pool.

    :param str args: pool IDs in bech32 format (pool1...)
    :return: list of pool information.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_pool_bech32_ids": [args] }
        pool_list = requests.post(self.POOL_INFO_URL, json = get_format, timeout=timeout)
        pool_list  = json.loads(pool_list.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_pool_bech32_ids": [args] }
        pool_list = requests.post(self.POOL_INFO_URL, json = get_format, headers = custom_headers, timeout=timeout)
        pool_list  = json.loads(pool_list.content)

    return pool_list


@Exception_Handler
def get_pool_stake_snapshot(self, pool_bech32):
    """
    Returns Mark, Set and Go stake snapshots for the selected pool, useful for leaderlog calculation

    :param str pool_bech32: Pool IDs in bech32 format (pool1...)
    :return: Array of pool stake information for 3 snapshots
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        snapshot = requests.get(self.POOL_STAKE_SNAPSHOT + pool_bech32, timeout=timeout)
        snapshot = json.loads(snapshot.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        snapshot = requests.get(self.POOL_STAKE_SNAPSHOT + pool_bech32, headers = custom_headers, timeout=timeout)
        snapshot = json.loads(snapshot.content)
    
    return snapshot


@Exception_Handler
def get_pool_delegators(self, pool_bech32, content_range="0-999"):
    """
    Return information about live delegators for a given pool.

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (current if omitted).
    :return: list of pool delegators information.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        info = requests.get(self.POOL_DELEGATORS_URL + pool_bech32, headers = custom_headers, timeout=timeout)
        info = json.loads(info.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(self.POOL_DELEGATORS_URL + pool_bech32, headers = custom_headers, timeout=timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_pool_delegators_history(self, pool_bech32, epoch_no=None, content_range="0-999"):
    """
    Return information about active delegators (incl. history) for a given pool and epoch number \
    (all epochs if not specified).

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (current if omitted).
    :return: list of pool delegators information.
    :rtype: list.
    """
    timeout = get_timeout()
    custom_headers = {"Range": str(content_range)}

    if self.BEARER is None and epoch_no is None:
        info = requests.get(self.POOL_DELEGATORS_HISTORY_URL + pool_bech32, headers=custom_headers, timeout=timeout)
        info = json.loads(info.content)

    if self.BEARER is None and epoch_no is not None:
        info = requests.get(f"{self.POOL_DELEGATORS_HISTORY_URL}{pool_bech32}&_epoch_no={epoch_no}", headers=custom_headers, timeout=timeout)
        info = json.loads(info.content)

    if self.BEARER is not None and epoch_no is None:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(self.POOL_DELEGATORS_HISTORY_URL + pool_bech32, headers=custom_headers, timeout=timeout)
        info = json.loads(info.content)

    if self.BEARER is not None and epoch_no is not None:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(f"{self.POOL_DELEGATORS_HISTORY_URL}{pool_bech32}&_epoch_no={epoch_no}", headers=custom_headers, timeout=timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_pool_blocks(self, pool_bech32, epoch_no=None, content_range="0-999"):
    """
    Return information about blocks minted by a given pool for all epochs (or _epoch_no if provided)

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (from the beginning if omitted).
    :return: list of blocks created by pool.
    :rtype: list.s
    """
    timeout = get_timeout()

    if self.BEARER is None and epoch_no is None:
        custom_headers = {"Range": str(content_range)}
        info = requests.get(self.POOL_BLOCKS_URL + pool_bech32, timeout=timeout, headers=custom_headers)
        info = json.loads(info.content)
    
    if self.BEARER is None and epoch_no is not None:
        custom_headers = {"Range": str(content_range)}
        info = requests.get(f"{self.POOL_BLOCKS_URL}{pool_bech32}&_epoch_no={epoch_no}", timeout=timeout, headers=custom_headers)
        info = json.loads(info.content)

    if self.BEARER is not None and epoch_no is None:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(self.POOL_BLOCKS_URL + pool_bech32, headers=custom_headers, timeout=timeout)
        info = json.loads(info.content)
    
    if self.BEARER is not None and epoch_no is not None:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(f"{self.POOL_BLOCKS_URL}{pool_bech32}&_epoch_no={epoch_no}", headers=custom_headers, timeout=timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_pool_history(self, pool_bech32, epoch_no=None):
    """
    Return information about pool stake, block and reward history in a given epoch _epoch_no \
    (or all epochs that pool existed for, in descending order if no _epoch_no was provided)

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (from the beginning if omitted).
    :return: list of blocks created by pool.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and epoch_no == None:
        info = requests.get(self.POOL_HISTORY_URL + pool_bech32, timeout=timeout)
        info = json.loads(info.content)

    if self.BEARER is None and epoch_no is not None:
        info = requests.get(f"{self.POOL_HISTORY_URL}{pool_bech32}&_epoch_no={epoch_no}", timeout=timeout)
        info = json.loads(info.content)

    if self.BEARER is not None and epoch_no is None:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(self.POOL_HISTORY_URL + pool_bech32, headers=custom_headers, timeout=timeout)
        info = json.loads(info.content)

    if self.BEARER is not None and epoch_no is not None:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(f"{self.POOL_HISTORY_URL}{pool_bech32}&_epoch_no={epoch_no}", headers=custom_headers, timeout=timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_pool_updates(self, pool_bech32=None):
    """
    Get all pool updates for all pools or only updates for specific pool if specified.

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :return: list of historical pool updates.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and pool_bech32 is None:
        pool_list = requests.get(self.POOL_UPDATES_URL, timeout=timeout)
        pool_list  = json.loads(pool_list.content)

    if self.BEARER is None and pool_bech32 is not None:
        pool_list = requests.get(f"{self.POOL_UPDATES_URL}?_pool_bech32={pool_bech32}", timeout=timeout)
        pool_list  = json.loads(pool_list.content)

    if self.BEARER is not None and pool_bech32 is None:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        pool_list = requests.get(self.POOL_UPDATES_URL, headers=custom_headers, timeout=timeout)
        pool_list  = json.loads(pool_list.content)

    if self.BEARER is not None and pool_bech32 is not None:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        pool_list = requests.get(f"{self.POOL_UPDATES_URL}?_pool_bech32={pool_bech32}", headers=custom_headers, timeout=timeout)
        pool_list  = json.loads(pool_list.content)

    return pool_list


@Exception_Handler
def get_pool_relays(self, content_range="0-999"):
    """
    Get a list of registered relays for all currently registered/retiring (not retired) pools.

    :param str range: paginated content range, up to  1000 records.
    :return: list of pool relay information.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        pool_list = requests.get(self.POOL_RELAYS_URL, headers = custom_headers, timeout=timeout)
        pool_list = json.loads(pool_list.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        pool_list = requests.get(self.POOL_RELAYS_URL, headers = custom_headers, timeout=timeout)
        pool_list = json.loads(pool_list.content)

    return pool_list


@Exception_Handler
def get_pool_metadata(self, *args):
    """
    Get Metadata (on & off-chain) for all currently registered/retiring (not retired) pools.

    :param str args: pool IDs in bech32 format (pool1...).
    :return: list of pool metadata.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None and len(args) != 0:
        get_format = {"_pool_bech32_ids": [args] }
        pool_list = requests.post(self.POOL_METADATA_URL, json = get_format, timeout=timeout)
        pool_list  = json.loads(pool_list.content)

    if self.BEARER is not None and len(args) != 0:
        get_format = {"_pool_bech32_ids": [args] }
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        pool_list = requests.get(self.POOL_METADATA_URL, headers = custom_headers, json = get_format, timeout=timeout)
        pool_list  = json.loads(pool_list.content)
    else:
        pool_list = None

    return pool_list

@Exception_Handler
def get_pool_registrations(self, epoch_no=None):
    """
    Get all pool registrations for all epochs (or _epoch_no if provided)

    :param str epoch_no: epoch number to get info (from the beginning if omitted).
    :return: list of pool registrations.
    :rtype: list.
    """
    timeout = get_timeout()
    if epoch_no is None:
        print(f"WARNING: epoch_no is required")
        return

    if self.BEARER is None:
        pool_list = requests.get(f"{self.POOL_REGISTRATIONS_URL}{epoch_no}", timeout=timeout)
        pool_list  = json.loads(pool_list.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        pool_list = requests.get(f"{self.POOL_REGISTRATIONS_URL}{epoch_no}", headers = custom_headers, timeout=timeout)
        pool_list  = json.loads(pool_list.content)

    return pool_list

@Exception_Handler
def get_pool_retirements(self, epoch_no=None):
    """
    Get all pool retirements for all epochs (or _epoch_no if provided)

    :param str epoch_no: epoch number to get info (from the beginning if omitted).
    :return: list of pool retirements.
    :rtype: list.
    """
    timeout = get_timeout()
    if epoch_no is None:
        print(f"WARNING: epoch_no is required")
        return
    
    if self.BEARER is None:
        pool_list = requests.get(f"{self.POOL_RETIREMENTS_URL}{epoch_no}", timeout=timeout)
        pool_list  = json.loads(pool_list.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        pool_list = requests.get(f"{self.POOL_RETIREMENTS_URL}{epoch_no}", headers = custom_headers, timeout=timeout)
        pool_list  = json.loads(pool_list.content)
    
    return pool_list