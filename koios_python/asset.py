#!/usr/bin/env python

import json
import requests


def get_asset_list():
    """
    Get the list of all native assets (paginated)

    :return: list with all asset list.
    :rtype: list.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_list")
    info = json.loads(info.content)
    return info


def get_asset_address_list(asset_policy, asset_name):
    """
    Get the list of all addresses holding a given asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all addresses.
    :rtype: list.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_address_list?_asset_policy=" \
        + asset_policy + "&_asset_name=" + asset_name)
    info = json.loads(info.content)
    return info


def get_asset_info(asset_policy, asset_name):
    """
    Get the information of an asset including first minting & token registry metadata.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all asset info.
    :rtype: list.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_info?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info


def get_asset_history(asset_policy, asset_name):
    """
    Get the mint/burn history of an asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset mint/burn history.
    :rtype: list.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_history?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info


def get_asset_policy_info(asset_policy):
    """
    Get the information for all assets under the same policy.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :return: list of all mint/burn transactions for an asset
    :rtype: list.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_policy_info?_asset_policy=" \
    + asset_policy)
    info = json.loads(info.content)
    return info


def get_asset_summary(asset_policy, asset_name):
    """
    Get the summary of an asset (total transactions exclude minting/total wallets include only
    wallets with asset balance).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset summary information.
    :rtype: list.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_summary?_asset_policy=" \
        + asset_policy + "&_asset_name=" + asset_name)
    info = json.loads(info.content)
    return info


def get_asset_txs(asset_policy, asset_name):
    """
    Get the list of all asset transaction hashes (newest first).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all asset hashes transactions.
    :rtype: list.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_txs?_asset_policy=" \
        + asset_policy + "&_asset_name=" + asset_name)
    info = json.loads(info.content)
    return info
    