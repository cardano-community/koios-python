#!/usr/bin/env python
"""
Provides all epoch functions
"""
import json
import requests

def get_epoch_info(self, epoch_no=None):
    """
    Get the epoch information, all epochs if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of detailed summary for each epoch.
    :rtype: list
    """
    if epoch_no is None:
        info = requests.get(self.EPOCH_INFO_URL, timeout=10)
        print(self.EPOCH_INFO_URL)
        info = json.loads(info.content)
    else:
        info = requests.get(f"{self.EPOCH_INFO_URL}?_epoch_no={epoch_no}", timeout=10)
        print(self.EPOCH_INFO_URL)
        info = json.loads(info.content)
    return info


def get_epoch_params(self, epoch_no=None):
    """
    Get the protocol parameters for specific epoch, returns information about all epochs
    if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of protocol parameters for each epoch.
    :rtype: list
    """
    if epoch_no is None:
        info = requests.get(self.EPOCH_PARAMS_URL, timeout=10)
        info = json.loads(info.content)
    else:
        info = requests.get(f"{self.EPOCH_PARAMS_URL}?_epoch_no={epoch_no}", timeout=10)
        info = json.loads(info.content)
    return info


def get_epoch_block_protocols(self, epoch_no=None):
    """
    Get the information about block protocol distribution in epoch

    :param int epoch_no: epoch number to fetch details for.
    :return: list of distinct block protocol versions counts in epoch
    :rtype: list
    """
    if epoch_no is None:
        info = requests.get(self.EPOCH_BLOCKS_URL, timeout=10)
        info = json.loads(info.content)
    else:
        info = requests.get(f"{self.EPOCH_BLOCKS_URL}?_epoch_no={epoch_no}", timeout=10)
        info = json.loads(info.content)
    return info
