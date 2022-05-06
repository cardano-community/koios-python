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

    :param: string with asset Policy ID in hexadecimal format (hex).
    :param: string with Asset Name in hexadecimal format (hex).
    :return: list of all addresses.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_address_list?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info


def get_asset_info(asset_policy, asset_name):
    """
    Get the information of an asset including first minting & token registry metadata.

    :param: string with asset policy ID in hexadecimal format (hex).
    :param: string with asset name in hexadecimal format (hex).
    :return: list of all asset info.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_info?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info


def get_asset_history(asset_policy, asset_name):
    """
    Get the mint/burn history of an asset.

    :param: string with asset policy ID in hexadecimal format (hex).
    :param: string with asset name in hexadecimal format (hex).
    :return: list of asset mint/burn history
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_history?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info


def get_asset_policy_info(asset_policy):
    """
    Get the information for all assets under the same policy.

    :param: string with asset Policy ID in hexadecimal format (hex).
    :return: list of all mint/burn transactions for an asset
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_policy_info?_asset_policy=" + str(asset_policy))
    info = json.loads(info.content)
    return info


def get_asset_summary(asset_policy, asset_name):
    """
    Get the summary of an asset (total transactions exclude minting/total wallets include only wallets with asset balance).

    :param: string with asset Policy ID in hexadecimal format (hex).
    :param: string with asset Name in hexadecimal format (hex).
    :return: list of asset summary information.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_summary?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info


def get_asset_txs(asset_policy, asset_name):
    """
    Get the list of all asset transaction hashes (newest first).

    :param: string with asset Policy ID in hexadecimal format (hex).
    :param: string with Asset Name in hexadecimal format (hex).
    :return: list of all asset hashes transactions.
    """
    info = requests.get("https://api.koios.rest/api/v0/asset_txs?_asset_policy=" \
        + str(asset_policy) + "&_asset_name=" + str(asset_name))
    info = json.loads(info.content)
    return info
    