#!/usr/bin/env python
"""
Provides all urls to use
"""

# Koios Network API URL
KOIOS_URL = "https://api.koios.rest/api/v0/"

# Network URLs
TIP_URL = KOIOS_URL + "tip"
GENESIS_URL = KOIOS_URL + "genesis"
TOTALS_URL = KOIOS_URL + "totals"

# Epoch URLs
EPOCH_INFO = KOIOS_URL + "epoch_info"
EPOCH_PARAMS = KOIOS_URL + "epoch_params"

# Block URLs
BLOCKS_URL = KOIOS_URL + "blocks"
BLOCK_INFO_URL = KOIOS_URL + "block_info"
BLOCK_TXS_URL = KOIOS_URL + "block_txs?_block_hash="

# Transactions URLs
TX_INFO_URL = KOIOS_URL + "tx_info"
TX_UTXOS_URL = KOIOS_URL + "tx_utxos"
TX_METADATA_URL = KOIOS_URL + "tx_metadata"
TX_METALABELS_URL = KOIOS_URL + "tx_metalabels"
SUBMIT_TX_URL = KOIOS_URL + "submittx"
TX_STATUS_URL = KOIOS_URL + "tx_status"

