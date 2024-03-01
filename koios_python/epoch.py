#!/usr/bin/env python
"""
Provides all epoch functions
"""
import json
import requests
from .environment import *

@Exception_Handler
def get_epoch_info(self, epoch_no=None, include_next_epoch=False):
    """
    Get the epoch information, all epochs if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of detailed summary for each epoch.
    :rtype: list
    """
    timeout = get_timeout()

    if self.BEARER is None:
    
        if epoch_no is None and include_next_epoch is False:
            info = requests.get(f"{self.EPOCH_INFO_URL}?_include_next_epoch=false", timeout=timeout)
            info = json.loads(info.content)
        if epoch_no is None and include_next_epoch is True:
            info = requests.get(f"{self.EPOCH_INFO_URL}?_include_next_epoch=true", timeout=timeout)
            info = json.loads(info.content)
        if epoch_no is not None and include_next_epoch is False:
            info = requests.get(f"{self.EPOCH_INFO_URL}?_epoch_no={epoch_no}&_include_next_epoch=false",\
                                timeout=timeout)
            info = json.loads(info.content)
        if epoch_no is not None and include_next_epoch is True:
            info = requests.get(f"{self.EPOCH_INFO_URL}?_epoch_no={epoch_no}&_include_next_epoch=true",\
                                 timeout=timeout)
            info = json.loads(info.content)
    
    else:

        if epoch_no is None and include_next_epoch is False:
            custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
            info = requests.get(f"{self.EPOCH_INFO_URL}?_include_next_epoch=false", timeout=timeout, headers=custom_headers)
            info = json.loads(info.content)
        if epoch_no is None and include_next_epoch is True:
            custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
            info = requests.get(f"{self.EPOCH_INFO_URL}?_include_next_epoch=true", timeout=timeout, headers=custom_headers)
            info = json.loads(info.content)
        if epoch_no is not None and include_next_epoch is False:
            custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
            info = requests.get(f"{self.EPOCH_INFO_URL}?_epoch_no={epoch_no}&_include_next_epoch=false",\
                                timeout=timeout, headers=custom_headers)
            info = json.loads(info.content)
        if epoch_no is not None and include_next_epoch is True:
            custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
            info = requests.get(f"{self.EPOCH_INFO_URL}?_epoch_no={epoch_no}&_include_next_epoch=true",\
                                 timeout=timeout, headers=custom_headers)
            info = json.loads(info.content)

    return info


@Exception_Handler
def get_epoch_params(self, epoch_no=None):
    """
    Get the protocol parameters for specific epoch, returns information about all epochs
    if no epoch specified.

    :param int epoch_no: epoch number to fetch details for.
    :return: list of protocol parameters for each epoch.
    :rtype: list
    """
    timeout = get_timeout()
    if self.BEARER is None:
        if epoch_no is None:
            info = requests.get(self.EPOCH_PARAMS_URL, timeout=timeout)
            info = json.loads(info.content)
        else:
            info = requests.get(f"{self.EPOCH_PARAMS_URL}?_epoch_no={epoch_no}", timeout=timeout)
            info = json.loads(info.content)
    else:
        if epoch_no is None:
            custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
            info = requests.get(self.EPOCH_PARAMS_URL, timeout=timeout, headers=custom_headers)
            info = json.loads(info.content)
        else:
            custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
            info = requests.get(f"{self.EPOCH_PARAMS_URL}?_epoch_no={epoch_no}", timeout=timeout, headers=custom_headers)
            info = json.loads(info.content)

    return info


@Exception_Handler
def get_epoch_block_protocols(self, epoch_no=None):
    """
    Get the information about block protocol distribution in epoch

    :param int epoch_no: epoch number to fetch details for.
    :return: list of distinct block protocol versions counts in epoch
    :rtype: list
    """
    timeout = get_timeout()

    if self.BEARER is None:
        if epoch_no is None:
            info = requests.get(self.EPOCH_BLOCKS_URL, timeout=timeout)
            info = json.loads(info.content)
        else:
            info = requests.get(f"{self.EPOCH_BLOCKS_URL}?_epoch_no={epoch_no}", timeout=timeout)
            info = json.loads(info.content)
    else:
        if epoch_no is None:
            custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
            info = requests.get(self.EPOCH_BLOCKS_URL, timeout=timeout, headers=custom_headers)
            info = json.loads(info.content)
        else:
            custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
            info = requests.get(f"{self.EPOCH_BLOCKS_URL}?_epoch_no={epoch_no}", timeout=timeout, headers=custom_headers)
            info = json.loads(info.content)
    
    return info