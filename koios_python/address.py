#!/usr/bin/env python

import json
import requests


def get_address_info():
    """Get summarised details about all blocks (paginated - latest first)"""
    blocks = requests.get("https://api.koios.rest/api/v0/blocks")
    blocks = json.loads(blocks.content)
    return blocks
