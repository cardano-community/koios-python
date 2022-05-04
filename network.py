#!/usr/bin/env python

import json
import requests

########### NETWORK ############################
def get_tip():
    """
    Get the tip info about the latest block seen by chain
    :return: Blockchain tip data
    """
    tip = requests.get("https://api.koios.rest/api/v0/tip")
    #confirmar que es correcto codigo 200
    #tip = tip.json
    tip = json.loads(tip.content)
    return tip


def get_genesis():
    """
    Get the Genesis parameters used to start specific era on chain
    :return: Genesis block data
    """
    genesis = requests.get("https://api.koios.rest/api/v0/genesis")
    genesis = json.loads(genesis.content)
    return genesis


def get_totals(epoch_no):
    """
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified \
    epoch, all epochs if empty
     :param stake_address: The stake addresse
    :return: Blockchain tip data
    """
    totals = requests.get("https://api.koios.rest/api/v0/totals?_epoch_no="+str(epoch_no))
    totals = json.loads(totals.content)[0]
    return totals


########### EPOCHS ###########################
def get_epoch_info(epoch_no):
    """Get the epoch information, all epochs if no epoch specified"""
    info = requests.get("https://api.koios.rest/api/v0/epoch_info?_epoch_no="+str(epoch_no))
    info = json.loads(info.content)[0]
    return info


def get_epoch_params(epoch_no):
    """Get the protocol parameters for specific epoch, returns information about all epochs \
    if no epoch specified"""
    info = requests.get("https://api.koios.rest/api/v0/epoch_params?_epoch_no="+str(epoch_no))
    info = json.loads(info.content)[0]
    return info


########### BLOCK ###########################
def get_blocks():
    """Get summarised details about all blocks (paginated - latest first)"""
    blocks = requests.get("https://api.koios.rest/api/v0/blocks")
    blocks = json.loads(blocks.content)
    return blocks


def get_block_info(block_hash):
    """Get detailed information about a specific block"""
    format = {"_block_hashes":[block_hash]}
    block = requests.post("https://api.koios.rest/api/v0/block_info", json = format)
    block = json.loads(block.content)[0]
    return block


def get_block_txs(block_hash):
    """Get a list of all transactions included in a provided block"""
    block = requests.get("https://api.koios.rest/api/v0/block_txs?_block_hash="+str(block_hash))
    block = json.loads(block.content)[0]
    return block


########### TRANSACTIONS ###########################
#my_header ={"Accept: application/json"+"Content-Type: application/json"}
def get_tx(tx_hash):
    """Get Tx data"""
    tx = {"_tx_hashes":[tx_hash]}
    koios_post = requests.post( "https://api.koios.rest/api/v0/tx_info", json = tx)
    koios_post = json.loads(koios_post.content)[0]
    print(koios_post)


# con la creacion de diccionarios es fácil la impresion de un campo
params = get_epoch_params(336)
nonce = params.get("nonce")
print(f"Nonce: {nonce}")

print(get_block_info("b39e3463fb83c547c2410abb39d92270dee5cda7417b10755303326df09aac86").get("epoch_slot"))


