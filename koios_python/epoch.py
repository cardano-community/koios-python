#!/usr/bin/env python
"""
Provides all epoch functions
"""
import json
import requests

from koios_python.urls import *


def get_epoch_info(epoch_no=None):
    """
    Get the epoch information, all epochs if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of detailed summary for each epoch.
    :rtype: list
    """
    if epoch_no is None:
        info = requests.get(KOIOS_URL+EPOCH_INFO)
        info = json.loads(info.content)
    else:
        info = requests.get(KOIOS_URL+EPOCH_INFO+"?_epoch_no="+str(epoch_no))
        info = json.loads(info.content)
    return info


def get_epoch_params(epoch_no=None):
    """
    Get the protocol parameters for specific epoch, returns information about all epochs
    if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of protocol parameters for each epoch.
    :rtype: list
    """
    if epoch_no is None:
        info = requests.get(KOIOS_URL+EPOCH_PARAMS)
        info = json.loads(info.content)
    else:
        info = requests.get(KOIOS_URL+EPOCH_PARAMS+"?_epoch_no="+str(epoch_no))
        info = json.loads(info.content)
    return info
