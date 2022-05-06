#!/usr/bin/env python

import json
import requests


def get_pool_list():
    """
    Get a list of all currently registered/retiring (not retired) pools.

    return: list of all registered/retiring pools.
    """
    pool_list = requests.get("https://api.koios.rest/api/v0/pool_list")
    pool_list = json.loads(pool_list.content)
    return pool_list
