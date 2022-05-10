# Koios Python ![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue) [![PyPI - Python Version](https://img.shields.io/badge/pypi%20package-v0.1.0-green)](https://pypi.org/project/koios-python/)
![koios](https://www.koios.rest/wp-content/uploads/ct-logos/logo_db1c2ccfd12c53198baca560933d95d7_2x.png)

## Overview
**Koios Python** is Python wrapper which allow interacting with all information and parameters stored on the Cardano blockchain using [Koios REST API](https://api.koios.rest/)


## What is Koios Python? 
**Koios Python** is a library based on [Koios](https://www.koios.rest/) Elastic Query Layer for [Cardano Node](https://github.com/input-output-hk/cardano-node/) by [Cardano Community Guild Operators](https://github.com/cardano-community). <br>
**Koios** is best described as a Decentralized and Elastic RESTful query layer for exploring data on Cardano blockchain to consume within applications/wallets/explorers/etc. <p>
**Koios** is really useful for developers because resource and maintenance requirements for Cardano blockchain components (e.g. cardano-node, cardano-db-sync) are ever-growing. It also simplifies how to query complex information from the blockchain.
    
This library allows getting data from the Cardano Blockchain using a simple syntaxis in your Python code. All the querys follow Koios API REST operations.

Required Python Modules:
--------------
* https://pypi.python.org/pypi/requests

## Installation [![PyPI Latest Release](https://img.shields.io/pypi/v/koios-python.svg)](https://pypi.org/project/koios-python/)
```python
pip install koios_python
```

## Usage

```python
import koios_python
```
    
## Features
- Supported REST Services:
    - [x] Network
        - Chain Tip
        - Genesis Info
        - Historical Tokenomic Statistics
    - [x] Epoch
        - Epoch Information
        - Epoch's Protocol Parameters
    - [x] Block
        - Block List
        - Block Information
        - Block Transactions
    - [x] Transactions
        - Transaction Information
        - Transaction UTxOs
        - Transaction Metadata
        - Transaction Metadata Labels
        - Transaction Submission
        - Transaction Status (Block Confirmations)
    - [x] Address
        - Address Information
        - Address Transactions
        - Transactions from Payment Credentials
        - Address Assets
    - [x] Account
        - Account List
        - Account Information
        - Account Rewards
        - Account Updates (History)
        - Account Addresses
        - Account Assets
        - Account History
    - [x] Asset
        - Asset List
        - Asset Address List
        - Asset Information
        - Asset History
        - Asset Policy Information
        - Asset Summary
        - Asset Transaction History
    - [x] Pool
        - Pool List
        - Pool Information
        - Pool Delegators List
        - Pool Blocks
        - Pool Stake, Block and Reward History
        - Pool Updates (History)
        - Pool Relays
        - Pool Metadata
    - [x] Script
        - Native Script List
        - Plutus Script List
        - Script Redeemers

