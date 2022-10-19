#!/usr/bin/env python
"""
Provides all epoch functions
"""
import json
import requests
import urls as u

# from .urls import EPOCH_INFO_URL, EPOCH_PARAMS_URL 

def get_epoch_info(url,epoch_no=None):
    """
    Get the epoch information, all epochs if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of detailed summary for each epoch.
    :rtype: list
    """
    
    
    if epoch_no is None:
        info = requests.get(url, timeout=10)
        info = json.loads(info.content)
        print(info)
    else:
        info = requests.get(url + "?_epoch_no=" + str(epoch_no), timeout=10)
        info = json.loads(info.content)
        print(info)
    return info


def get_epoch_params(url,epoch_no=None):
    """
    Get the protocol parameters for specific epoch, returns information about all epochs
    if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of protocol parameters for each epoch.
    :rtype: list
    """
    if epoch_no is None:
        info = requests.get(url, timeout=10)
        info = json.loads(info.content)
    else:
        info = requests.get(url + "?_epoch_no=" + str(epoch_no), timeout=10)
        info = json.loads(info.content)
    return info
