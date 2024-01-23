#!/usr/bin/env python
"""
Provides all address functions
"""
import json
import requests
from .environment import *


@Exception_Handler
def query(self, query, *params):
    """
    Query the current tip of the Network.

    :param str query: query to search and read data from Ogmios.
    :param dict params: parameters to search and read data.
    :return: list of all info about query.
    :rtype: list.
    """
    print(f"Querying {self.url}...")
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"jsonrpc": "2.0", "method": query}
        tip = requests.post(self.url, json = get_format, timeout=timeout)
        tip  = json.loads(tip.content)
    else:
        get_format = {"jsonrpc": "2.0", "method": query}
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        tip = requests.post(self.url, json = get_format, timeout=timeout, headers=custom_headers)

    return tip