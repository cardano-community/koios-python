#!/usr/bin/env python
"""
Provides all asset functions
"""
import json
import requests
from .environment import *


@Exception_Handler
def get_asset_list(self, content_range="0-999"):
    """
    Get the list of all native assets (paginated, sorted)

    :return: list with all asset list.
    :param str content_range: number of selected elements to return
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        custom_params = {"order": "asset_name.asc"}
        asset_list = requests.get(self.ASSET_LIST_URL, headers = custom_headers, params = custom_params, timeout=timeout)
        asset_list = json.loads(asset_list.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        custom_params = {"order": "asset_name.asc"}
        asset_list = requests.get(self.ASSET_LIST_URL, headers = custom_headers, params = custom_params, timeout=timeout)
        asset_list = json.loads(asset_list.content)
        
    return asset_list


@Exception_Handler
def get_policy_asset_list(self, asset_policy, content_range="0-999"):
    """
    Get the list of asset under the given policy (including balances)

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str content_range: number of selected elements to return
    :return: list of all assets under the same policy.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        custom_params = {"order": "asset_name.asc"}
        info = requests.get(f"{self.POLICY_ASSET_LIST_URL}{asset_policy}",
                headers = custom_headers, params = custom_params, timeout = timeout)
        info = json.loads(info.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        custom_params = {"order": "asset_name.asc"}
        info = requests.get(f"{self.POLICY_ASSET_LIST_URL}{asset_policy}",
                headers = custom_headers, params = custom_params, timeout = timeout)
        info = json.loads(info.content)
        
    return info


@Exception_Handler
def get_asset_token_registry(self, content_range="0-999"):
    """
    Get a list of assets registered via token registry on Github

    :return: list of all asset token registry.
    :param str content_range: number of selected elements to return
    :rtype: list.    
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        token_registry = requests.get(self.ASSET_TOKEN_REGISTRY_URL, headers = custom_headers, timeout=timeout)
        token_registry = json.loads(token_registry.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        token_registry = requests.get(self.ASSET_TOKEN_REGISTRY_URL, headers = custom_headers, timeout=timeout)
        token_registry = json.loads(token_registry.content)

    return token_registry


@Exception_Handler
def get_asset_info(self, asset_policy, asset_name):
    """
    Get the information of an asset including first minting & token registry metadata.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all asset info.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        info = requests.get(f"{self.ASSET_INFO_URL}{asset_policy}&_asset_name={asset_name}", timeout=timeout)
        info = json.loads(info.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(f"{self.ASSET_INFO_URL}{asset_policy}&_asset_name={asset_name}", \
            headers = custom_headers, timeout=timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_asset_info_bulk(self, *asset_list):
    """
    Get the information of a list of assets including first minting & token registry metadata.
    :param list asset_list: list of assets to query.
    :return: list of all asset info.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        get_format = {"_asset_list": asset_list}
        asset_info = requests.post(self.ASSET_INFO_BULK_URL, json= get_format, timeout=timeout)
        asset_info = json.loads(asset_info.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_asset_list": asset_list}
        asset_info = requests.post(self.ASSET_INFO_BULK_URL, json= get_format, headers=custom_headers, timeout=timeout)
        asset_info = json.loads(asset_info.content)

    return asset_info


@Exception_Handler
def get_asset_utxos(self, *asset_list, extended=False, content_range="0-999"):
    """
    Get the UTXO information of a list of assets including
    
    :param list of assets
    :param bool extended: extended UTXO information
    :return: list of utxos
    :rtype: list.
    """
    if self.BEARER is None and extended is True:
        extended = "true"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range),}
        get_format = {"_asset_list": asset_list, "_extended": extended}
        utxos = requests.post(self.ASSET_UTXOS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)

    if self.BEARER is None and extended is False:
        extended = "false"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range),}
        get_format = {"_asset_list": asset_list, "_extended": extended}
        utxos = requests.post(self.ASSET_UTXOS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)

    if self.BEARER is not None and extended is True:
        extended = "true"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_asset_list": asset_list, "_extended": extended}
        utxos = requests.post(self.ASSET_UTXOS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)

    if self.BEARER is not None and extended is False:
        extended = "false"
        timeout = get_timeout()
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        get_format = {"_asset_list": asset_list, "_extended": extended}
        utxos = requests.post(self.ASSET_UTXOS_URL, json = get_format, headers = custom_headers, timeout=timeout)
        utxos = json.loads(utxos.content)

    return utxos


@Exception_Handler
def get_asset_history(self, asset_policy, asset_name, content_range="0-999"):
    """
    Get the mint/burn history of an asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset mint/burn history.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        history = requests.get(f"{self.ASSET_HISTORY_URL}{asset_policy}&_asset_name={asset_name}",
                                headers=custom_headers, timeout=timeout)
        history = json.loads(history.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        history = requests.get(f"{self.ASSET_HISTORY_URL}{asset_policy}&_asset_name={asset_name}",
                                headers=custom_headers, timeout=timeout)
        history = json.loads(history.content)

    return history


@Exception_Handler
def get_asset_addresses(self, asset_policy, asset_name, content_range="0-999"):
    """
    Get the list of all addresses holding a given asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :param str content_range: number of selected elements to return
    :return: list of all addresses.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        custom_params = {"order": "payment_address.asc"}
        info = requests.get(f"{self.ASSET_ADDRESSES_URL}{asset_policy}&_asset_name={asset_name}", \
            headers = custom_headers, params = custom_params, timeout=timeout)
        info = json.loads(info.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        custom_params = {"order": "payment_address.asc"}
        info = requests.get(f"{self.ASSET_ADDRESSES_URL}{asset_policy}&_asset_name={asset_name}", \
            headers = custom_headers, params = custom_params, timeout=timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_asset_nft_address(self, asset_policy, asset_name):
    """
    Get the address where specified NFT currently reside on.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list with payment addresses.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        info = requests.get(f"{self.ASSET_NFT_ADDRESS_URL}{asset_policy}&_asset_name={asset_name}", timeout=timeout)
        info = json.loads(info.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(f"{self.ASSET_NFT_ADDRESS_URL}{asset_policy}&_asset_name={asset_name}", \
            headers = custom_headers, timeout=timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_policy_asset_addresses(self, asset_policy, content_range="0-999"):
    """
    Get the list of addresses with quantity for each asset on the given policy

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str content_range: number of selected elements to return
    :return: list of all addresses.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
        custom_params = {"order": "asset_name.asc"}
        info = requests.get(f"{self.POLICY_ASSET_ADDRESSES_LIST_URL}{asset_policy}",
                headers = custom_headers, params = custom_params, timeout = timeout)
        info = json.loads(info.content)
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        custom_params = {"order": "asset_name.asc"}
        info = requests.get(f"{self.POLICY_ASSET_ADDRESSES_LIST_URL}{asset_policy}",
                headers = custom_headers, params = custom_params, timeout = timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_policy_asset_info(self, asset_policy):
    """
    Get the information for all assets under the same policy.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :return: list of all mint/burn transactions for an asset
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        info = requests.get(f"{self.POLICY_ASSET_INFO_URL}{asset_policy}", timeout=timeout)
        info = json.loads(info.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        info = requests.get(f"{self.POLICY_ASSET_INFO_URL}{asset_policy}", \
            headers = custom_headers, timeout=timeout)
        info = json.loads(info.content)

    return info


@Exception_Handler
def get_asset_summary(self, asset_policy, asset_name):
    """
    Get the summary of an asset (total transactions exclude minting/total wallets include only
    wallets with asset balance).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset summary information.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        summary = requests.get(f"{self.ASSET_SUMMARY_URL}{asset_policy}&_asset_name={asset_name}", timeout=timeout)
        summary = json.loads(summary.content)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        summary = requests.get(f"{self.ASSET_SUMMARY_URL}{asset_policy}&_asset_name={asset_name}", \
            headers = custom_headers, timeout=timeout)
        summary = json.loads(summary.content)

    return summary


@Exception_Handler
def get_asset_txs(self, asset_policy, asset_name, after_block=0, history=False, content_range="0-999"):
    """
    Get the list of current or all asset transaction hashes (newest first)

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset name: Asset Name in hexadecimal format (hex), empty asset name returns royalties
    :param int after_block_height: Block height for specifying time delta
    :param bool history: Include all historical transactions, setting to false includes only the non-empty ones
    :param str content_range: number of selected elements to return
    :return: list of all assets under the same policy.
    :rtype: list.
    """
    timeout = get_timeout()
    
    if self.BEARER is None and history is True:
        history = "true"
        custom_headers = {"Range": str(content_range)}
        txs = requests.get(f"{self.ASSET_TXS_URL}{asset_policy}&_asset_name={asset_name} \
                           &_after_block_height={after_block}&_history={history}",
                            headers=custom_headers, timeout=timeout)
        txs = json.loads(txs.content)

    if self.BEARER is None and history is False:
        history = "false"
        custom_headers = {"Range": str(content_range)}
        txs = requests.get(f"{self.ASSET_TXS_URL}{asset_policy}&_asset_name={asset_name} \
                           &_after_block_height={after_block}&_history={history}",
                           headers=custom_headers, timeout=timeout)
        txs = json.loads(txs.content)

    if self.BEARER is not None and history is True:
        history = "true"
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        txs = requests.get(f"{self.ASSET_TXS_URL}{asset_policy}&_asset_name={asset_name} \
                            &_after_block_height={after_block}&_history={history}",
                            headers=custom_headers, timeout=timeout)
        txs = json.loads(txs.content)

    if self.BEARER is not None and history is False:
        history = "false"
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}
        txs = requests.get(f"{self.ASSET_TXS_URL}{asset_policy}&_asset_name={asset_name} \
                            &_after_block_height={after_block}&_history={history}",
                            headers=custom_headers, timeout=timeout)
        txs = json.loads(txs.content)

    return txs
