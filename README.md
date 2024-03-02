
![Logo-Python-Koios](https://github.com/cardano-community/koios-python/assets/82296005/46656e85-e292-4975-99df-e03dd1f4f9ae)


# Koios Python ![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue) [![PyPI - Python Version](https://img.shields.io/badge/pypi%20package-v2.0.0-green)](https://pypi.org/project/koios-python/)

## Overview
**Koios Python** is Python wrapper which allow interacting with all information and parameters stored on the Cardano blockchain using [Koios REST API](https://api.koios.rest/)


## What is Koios Python? 
**Koios Python** is a library based on [Koios](https://www.koios.rest/) Elastic Query Layer for [Cardano Node](https://github.com/input-output-hk/cardano-node/) by [Cardano Community Guild Operators](https://github.com/cardano-community). <br>
**Koios** is best described as a Decentralized and Elastic RESTful query layer for exploring data on Cardano blockchain to consume within applications/wallets/explorers/etc. <p>
**Koios** is really useful for developers because resource and maintenance requirements for Cardano blockchain components (e.g. cardano-node, cardano-db-sync) are ever-growing. It also simplifies how to query complex information from the blockchain.
    
This library allows getting data from the Cardano Blockchain using a simple syntaxis in your Python code. All the querys follow Koios API REST operations.

Required Python Modules
--------------
* https://pypi.python.org/pypi/requests

## Installation [![PyPI Latest Release](https://img.shields.io/badge/pypi%20package-v2.0.0-green)](https://pypi.org/project/koios-python/)
```python
pip install koios_python
```
    
## Upgrade to the last Version
```python
pip install --upgrade koios_python
```
    
## Usage
Import to your python file this library:
    
```python
import koios_python
```

You can read all info about how works this library in our [Wiki](https://github.com/cardano-community/koios-python/wiki)
    
## TODO
- [x] Managing errors 
- [x] Inside functions 
- [x] Pagination (most functions have it added)
- [x] User Inputs
- [x] Timeouts
- [x] Ordering
- [ ] Adding Vertical Filtering
- [ ] Adding Async methods



## Features  
- Supported REST Services:
    - [x] Network
        - Chain Tip
        - Genesis Info
        - Historical Tokenomic Statistics
        - Param Update Proposals
        - Reserve Withdrawals
        - Treasury Withdrawals
          
    - [x] Epoch
        - Epoch Information
        - Epoch's Protocol Parameters
        - Epoch Blocks Protocol
          
    - [x] Block
        - Block List
        - Block Information
        - Block Transactions
          
    - [x] Transactions
        - UTxO Information
        - Transaction Information
        - Transaction UTxOs [Deprecated]
        - Transaction Metadata
        - Transaction Metadata Labels
        - Transaction Submit
        - Transaction Status (Block Confirmations)
          
    - [x] Stake Account
        - Account List
        - Account Information
        - Account Information Cached
        - UTxOs for Stake Addresses (accounts)
        - Account Transactions
        - Account Rewards
        - Account Updates (History)
        - Account Addresses
        - Account Assets
        - Account History

    - [x] Address
        - Address Information
        - Address UTxOs
        - Address Transactions
        - Transactions from Payment Credentials
        - Address Assets
          
    - [x] Asset
        - Asset List
        - Policy Asset List
        - Asset Token Registry
        - Asset Information (Bulk)
        - Asset Information
        - Asset UTxOs
        - Asset History
        - Asset Addresses
        - NFT Address
        - Policy Asset Address List
        - Policy Asset Information
        - Asset Summary
        - Asset Transactions
        - Asset Policy Information [DEPRECATED]
        - Asset Address List [DEPRECATED]

    - [x] Pool
        - Pool List
        - Pool Information
        - Pool Stake Snapshot
        - Pool Delegators List
        - Pool Delegators History
        - Pool Blocks
        - Pool Stake, Block and Reward History
        - Pool Updates (History)
        - Pool Registrations
        - Pool Retirements
        - Pool Relays
        - Pool Metadata
          
    - [x] Script
        - Script Information
        - Native Script List
        - Plutus Script List
        - Script Redeemers
        - Script UTxOs
        - Datum Information

    - [x] Ogmios
        - Query

