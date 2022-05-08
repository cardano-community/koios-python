#!/usr/bin/env python

import json
import requests


def get_epoch_info(epoch_no=None):
    """
    Get the epoch information, all epochs if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of detailed summary for each epoch.
    :rtype: list
    """
    if epoch_no is None:
        info = requests.get("https://api.koios.rest/api/v0/epoch_info")
        info = json.loads(info.content)
    else:
        info = requests.get("https://api.koios.rest/api/v0/epoch_info?_epoch_no="+str(epoch_no))
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
        info = requests.get("https://api.koios.rest/api/v0/epoch_params")
        info = json.loads(info.content)
    else:
        info = requests.get("https://api.koios.rest/api/v0/epoch_params?_epoch_no="+str(epoch_no))
        info = json.loads(info.content)
    return info
