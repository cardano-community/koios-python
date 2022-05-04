# Koios Python ![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue) 

## Overview
**Koios Python** is Python wrapper which allow interacting with all information and parameters stored on the Cardano blockchain using [Koios REST API](https://api.koios.rest/)


## What is Koios Python? 
**Koios Python** is a library based on [Koios](https://www.koios.rest/) Elastic Query Layer for [Cardano Node](https://github.com/input-output-hk/cardano-node/) by [Cardano Community Guild Operators](https://github.com/cardano-community). <br>
**Koios** is best described as a Decentralized and Elastic RESTful query layer for exploring data on Cardano blockchain to consume within applications/wallets/explorers/etc. <br>
Resource and maintenance requirements for Cardano blockchain components (e.g. cardano-node, cardano-db-sync) are ever-growing. Along with that, every builder needs to identify how to query complex information from the chain.

This library allows getting data from the Cardano Blockchain using a simple syntaxis in your Python code. All the querys follow REST operations:

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
        - Transaction Submission (in progress...)
        - Transaction Status (Block Confirmations)
    - [ ] Address
        - Address Information
        - Address Transactions
        - Transactions from Payment Credentials
        - Address Assets
    - [ ] Account
        - Account List
        - Account Information
        - Account Rewards
        - Account Updates (History)
        - Account Addresses
        - Account Assets
        - Account History
    - [ ] Asset
        - Asset List
        - Asset Address List
        - Asset Information
        - Asset History
        - Asset Policy Information
        - Asset Summary
        - Asset Transaction History
    - [ ] Pool
        - Pool List
        - Pool Information
        - Pool Delegators List
        - Pool Blocks
        - Pool Stake, Block and Reward History
        - Pool Updates (History)
        - Pool Relays
        - Pool Metadata
    - [ ] Script
        - Native Script List
        - Plutus Script List
        - Script Redeemers








