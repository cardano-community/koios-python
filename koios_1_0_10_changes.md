## Changes for KOIOS API

- In this file you will find the changes we need to complete to koios_python before next release to match the current version of KOIOS API. All tasks that have been completed are the ones crossed out by a line.

### Deprecations

- ~~`/asset_address_list` - Renamed to asset_addresses keeping naming line with other endpoints (old endpoint will be retired in future release) #149~~
- ~~`/asset_policy_info` - Renamed to policy_asset_info keeping naming line with other endpoints (old endpoint will be retired in future release) #149~~

### New endpoints added

- ~~`/asset_addresses` - Equivalent of deprecated /asset_address_list #149~~
- ~~`/asset_nft_address` - Returns address where the specified NFT sits on #149~~
- ~~`/account_utxos` - Returns brief details on non-empty UTxOs associated with a given stake address #149~~
- ~~`/asset_info_bulk` - Bulk version of /asset_info #142~~
- ~~`/asset_token_registry` - Returns assets registered via token registry on github #145~~
- `/credential_utxos` - Returns UTxOs associated with a payment credential #149
- `/param_updates` - Returns list of parameter update proposals applied to the network #149
- ~~`/policy_asset_addresses` - Returns addresses with quantity for each asset on a given policy #149~~
- ~~`/policy_asset_info` - Equivalent of deprecated /asset_policy_info but with more details in output #149~~
- ~~`/policy_asset_list` - Returns list of asset under the given policy (including supply) #142, #149~~


## Data Input/Output Changes
- Input - `/account_addresses` - Add optional _first_only and _empty flags to show only first address with tx or to include empty addresses to output #149
- Input - `/epoch_info` - Add optional _include_next_epoch field to show next epoch stats if available (eg: nonce, active stake) #143
- Output (addition) - `/account_assets` , `/address_assets` , `/address_info`, `/tx_info`, `/tx_utxos` - Add decimals to output #142
- Output (addition) - `/policy_asset_info` - Add `minting_tx_hash`, `total_supply`, `mint_cnt`, `burn_cnt` and `creation_time` fields to the output #149
- Output (breaking) - `/tx_info` - Change `_invalid_before` and `_invalid_after` to text field #141
- Output (breaking/removal) - `tx_info` - Remove the field `plutus_contracts` > [array] > `outputs` as there is no logic to connect it to inputs spending #163

## Chores/epoch_info, /epoch_params - Restrict output to current epoch #149
- `/block_info` - Use `/previous_id` field to show previous/next blocks (previously was using block_id/height) #145
- `/asset_info/asset_policy_info` - Fix mint tx data to be latest #141
- Support new guild scripts revamp #1572
- Add asset token registry check 1606
- New cache table `grest.asset_info_cache` to hold mint/burn counts alongwith first/last mint tx/keys #142
- Bump to Koios 1.0.10rc #149
- Fix typo in specs for `/pool_delegators` output column `latest_delegation_tx_hash` #149
- Add indexes for ones missing after configuring cardano-db-sync 13.1.0.0 #149
- Update PostgREST to be run as `authenticator` user, whose default `statement_timeout` is set to 65s and update configs accordingly #1606
- Replace all RPC references for JSON endpoints with JSONB, this allows filtering child members of array elements using `cs.[{"key":"value"}]` in PostgREST #172
- Fix Asset Info Cache to not rely on being able to decode policy ID (bad data on IO repo) #173
- Handle Pool_list to check metadata entries that have not been populated in pool_offline_data #173
- Fix pool_updates to use pmr_id instead of pool_offline_data.id #173
- Update account_info_cached description to clarify it is effective for registered accounts #173
