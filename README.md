
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

### Governance

Conway-era governance queries: delegated representatives (DReps), the
constitutional committee, governance action proposals and the votes cast on them.

```python
from koios_python import URLs

kp = URLs()
```

**DReps**

```python
# List DReps, and look up one or more of them
kp.get_drep_list()
kp.get_drep_info("drep1ygqzg3ed7rdqeg3343jw0fptqzc3lqtk3rvnnmgq64rj85sxd4sr4")
kp.get_drep_metadata("drep1ygqzg3ed7rdqeg3343jw0fptqzc3lqtk3rvnnmgq64rj85sxd4sr4")

# Registration updates, delegators and votes for a single DRep
kp.get_drep_updates("drep1ygqzg3ed7rdqeg3343jw0fptqzc3lqtk3rvnnmgq64rj85sxd4sr4")
kp.get_drep_delegators("drep1ygqzg3ed7rdqeg3343jw0fptqzc3lqtk3rvnnmgq64rj85sxd4sr4")
kp.get_drep_votes("drep1ygqzg3ed7rdqeg3343jw0fptqzc3lqtk3rvnnmgq64rj85sxd4sr4")

# Voting power, per epoch
kp.get_drep_epoch_summary()                 # totals across all DReps
kp.get_drep_epoch_summary(epoch_no=653)
kp.get_drep_history(drep_id="drep1ygq...")
kp.get_drep_voting_power_history(drep_id="drep1ygq...", epoch_no=653)
```

> `get_drep_history` and `get_drep_voting_power_history` accept both filters
> optionally, but the unfiltered query is too large for the public endpoint and
> returns a 504. Pass a DRep ID and/or an epoch number.

**Constitutional committee**

```python
kp.get_committee_info()                     # members, quorum and threshold
kp.get_committee_votes()                    # votes by every member
kp.get_committee_votes("cc_hot1qde96n2yfxvx2pc4xm25va9ssqezh5mxhc2n8rdjyxq8kvgwwujd9")
```

**Proposals and votes**

```python
kp.get_proposal_list()
kp.get_vote_list()                          # every vote cast, across proposals

proposal = "gov_action105mjyzm3spjppny2m776lwk5jnsuu07uva9tz0yg5u4nkf770rvsql5raht"
kp.get_proposal_voting_summary(proposal)    # the tally
kp.get_proposal_votes(proposal)             # the individual votes

# Proposals a given voter is eligible to vote on (DRep, pool or committee member)
kp.get_voter_proposal_list("drep1ygqzg3ed7rdqeg3343jw0fptqzc3lqtk3rvnnmgq64rj85sxd4sr4")
```

**Stake pools as voters**

```python
pool = "pool1z5uqdk7dzdxaae5633fqfcu2eqzy3a3rgtuvy087fdld7yws0xt"
kp.get_pool_votes(pool)
kp.get_pool_voting_power_history(pool_bech32=pool)
kp.get_pool_voting_power_history(epoch_no=653)
```

All of the above take the usual `content_range` argument for pagination, e.g.
`kp.get_proposal_list(content_range="0-99")`.

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

    - [x] Governance
        - DRep Epoch Summary
        - DRep List
        - DRep Information
        - DRep Metadata
        - DRep Updates
        - DRep Delegators History
        - DRep Voting Power History
        - DRep Votes
        - DRep Delegators
        - Committee Information
        - Committee Votes
        - Proposal List
        - Voter's Proposal List
        - Proposal Voting Summary
        - Proposal Votes
        - Vote List
        - Pool Voting Power History
        - Pool Votes

    - [x] Ogmios
        - Query

