#!/usr/bin/env python

import json
import requests


def get_epoch_info(epoch_no):
    """
    Get the epoch information, all epochs if no epoch specified
    param:
    return:
    """
    info = requests.get("https://api.koios.rest/api/v0/epoch_info?_epoch_no="+str(epoch_no))
    info = json.loads(info.content)[0]
    return info


def get_epoch_params(epoch_no):
    """
    Get the protocol parameters for specific epoch, returns information about all epochs \
    if no epoch specified.
    param:
    return:
    """
    info = requests.get("https://api.koios.rest/api/v0/epoch_params?_epoch_no="+str(epoch_no))
    info = json.loads(info.content)[0]
    return info
