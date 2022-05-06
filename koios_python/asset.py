#!/usr/bin/env python

import json
import requests


def get_address_info():
    """
    Get the list of all native assets (paginated)

    :return: list with all asset list.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_list")
    info = json.loads(info.content)
    return info


def get_asset_address_list(asset_policy, asset_name):
    """
    Get the list of all addresses holding a given asset.

    :param: Cardano payment/base address (bech32 encoded) for transaction's input UTxO.
    :param: asset balance on the payment address.
    :return: list of all addresses.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_address_list?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info


def get_asset_info(asset_policy, asset_name):
    """
    Get the information of an asset including first minting & token registry metadata.

    :param: Cardano payment/base address (bech32 encoded) for transaction's input UTxO.
    :param: asset balance on the payment address.
    :return: list of all asset info.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_info?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info


def get_asset_history(asset_policy, asset_name):
    """
    Get the mint/burn history of an asset.

    :param: Cardano payment/base address (bech32 encoded) for transaction's input UTxO.
    :param: asset balance on the payment address.
    :return: list of all mint/burn transactions for an asset
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_history?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info