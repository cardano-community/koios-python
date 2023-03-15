## Changes for API

### Deprecations

- ~~`/asset_address_list` - Renamed to asset_addresses keeping naming line with other endpoints (old endpoint will be retired in future release) #149~~
- ~~`/asset_policy_info` - Renamed to policy_asset_info keeping naming line with other endpoints (old endpoint will be retired in future release) #149~~

### New endpoints added

- ~~/asset_addresses - Equivalent of deprecated /asset_address_list #149~~
- ~~/asset_nft_address - Returns address where the specified NFT sits on #149~~
- ~~/account_utxos - Returns brief details on non-empty UTxOs associated with a given stake address #149~~
- ~~/asset_info_bulk - Bulk version of /asset_info #142~~
- ~~/asset_token_registry - Returns assets registered via token registry on github #145~~
- ~~/credential_utxos - Returns UTxOs associated with a payment credential #149~~
- /param_updates - Returns list of parameter update proposals applied to the network #149
- /policy_asset_addresses - Returns addresses with quantity for each asset on a given policy #149
- /policy_asset_info - Equivalent of deprecated /asset_policy_info but with more details in output #149
- /policy_asset_list - Returns list of asset under the given policy (including supply) #142, #149