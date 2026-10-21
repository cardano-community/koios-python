#!/usr/bin/env python
"""
Provides all governance functions
"""
import json
import requests
from .environment import *


@Exception_Handler
def get_drep_epoch_summary(self, epoch_no=None):
    """
    Get the summary of voting power and DRep count for each epoch.

    :param int epoch_no: Epoch Number to fetch details for.
    :return: list of DRep voting power summaries by epoch.
    :rtype: list.
    """
    timeout = get_timeout()

    if epoch_no is None:
        url = self.DREP_EPOCH_SUMMARY_URL
    else:
        url = f"{self.DREP_EPOCH_SUMMARY_URL}?_epoch_no={epoch_no}"

    if self.BEARER is None:
        summary = requests.get(url, timeout=timeout)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        summary = requests.get(url, timeout=timeout, headers=custom_headers)

    summary = json.loads(summary.content)
    return summary


@Exception_Handler
def get_drep_list(self, content_range="0-999"):
    """
    Get the list of all active delegated representatives (DReps).

    :return: list of all active DReps.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    drep_list = requests.get(self.DREP_LIST_URL, headers=custom_headers, timeout=timeout)
    drep_list = json.loads(drep_list.content)
    return drep_list


@Exception_Handler
def get_drep_info(self, *args):
    """
    Get the detailed information about requested delegated representatives (DReps).

    :param str args: DRep IDs in bech32 format (drep1...)
    :return: list of DRep information.
    :rtype: list.
    """
    timeout = get_timeout()
    get_format = {"_drep_ids": list(args)}

    if self.BEARER is None:
        drep_info = requests.post(self.DREP_INFO_URL, json=get_format, timeout=timeout)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        drep_info = requests.post(self.DREP_INFO_URL, json=get_format, headers=custom_headers, timeout=timeout)

    drep_info = json.loads(drep_info.content)
    return drep_info


@Exception_Handler
def get_drep_metadata(self, *args):
    """
    Get the metadata of requested delegated representatives (DReps).

    :param str args: DRep IDs in bech32 format (drep1...)
    :return: list of DRep metadata.
    :rtype: list.
    """
    timeout = get_timeout()
    get_format = {"_drep_ids": list(args)}

    if self.BEARER is None:
        drep_metadata = requests.post(self.DREP_METADATA_URL, json=get_format, timeout=timeout)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        drep_metadata = requests.post(self.DREP_METADATA_URL, json=get_format, headers=custom_headers, timeout=timeout)

    drep_metadata = json.loads(drep_metadata.content)
    return drep_metadata


@Exception_Handler
def get_drep_updates(self, drep_id=None, content_range="0-999"):
    """
    Get the updates history of a delegated representative (DRep), all DReps if empty.

    :param str drep_id: DRep ID in bech32 format (drep1...)
    :return: list of DRep updates.
    :rtype: list.
    """
    timeout = get_timeout()

    if drep_id is None:
        url = self.DREP_UPDATES_URL
    else:
        url = f"{self.DREP_UPDATES_URL}?_drep_id={drep_id}"

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    drep_updates = requests.get(url, headers=custom_headers, timeout=timeout)
    drep_updates = json.loads(drep_updates.content)
    return drep_updates


@Exception_Handler
def get_drep_history(self, drep_id=None, epoch_no=None, content_range="0-999"):
    """
    Get the delegator history of a delegated representative (DRep).

    Both filters are optional per the API spec, but the unfiltered query is too
    large for the public endpoint and returns a 504, so pass a DRep ID and/or an
    epoch number.

    :param str drep_id: DRep ID in bech32 format (drep1...)
    :param int epoch_no: Epoch Number to fetch details for.
    :return: list of DRep delegation history.
    :rtype: list.
    """
    timeout = get_timeout()

    params = []
    if drep_id is not None:
        params.append(f"_drep_id={drep_id}")
    if epoch_no is not None:
        params.append(f"_epoch_no={epoch_no}")
    url = self.DREP_HISTORY_URL if not params else f"{self.DREP_HISTORY_URL}?{'&'.join(params)}"

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    drep_history = requests.get(url, headers=custom_headers, timeout=timeout)
    drep_history = json.loads(drep_history.content)
    return drep_history


@Exception_Handler
def get_drep_voting_power_history(self, drep_id=None, epoch_no=None, content_range="0-999"):
    """
    Get the voting power history of a delegated representative (DRep).

    Both filters are optional per the API spec, but the unfiltered query is too
    large for the public endpoint and returns a 504, so pass a DRep ID and/or an
    epoch number.

    :param str drep_id: DRep ID in bech32 format (drep1...)
    :param int epoch_no: Epoch Number to fetch details for.
    :return: list of DRep voting power by epoch.
    :rtype: list.
    """
    timeout = get_timeout()

    params = []
    if drep_id is not None:
        params.append(f"_drep_id={drep_id}")
    if epoch_no is not None:
        params.append(f"_epoch_no={epoch_no}")
    url = self.DREP_VOTING_POWER_HISTORY_URL if not params \
        else f"{self.DREP_VOTING_POWER_HISTORY_URL}?{'&'.join(params)}"

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    voting_power = requests.get(url, headers=custom_headers, timeout=timeout)
    voting_power = json.loads(voting_power.content)
    return voting_power


@Exception_Handler
def get_drep_votes(self, drep_id, content_range="0-999"):
    """
    Get the votes cast by a delegated representative (DRep).

    :param str drep_id: DRep ID in bech32 format (drep1...)
    :return: list of votes cast by the DRep.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    drep_votes = requests.get(f"{self.DREP_VOTES_URL}{drep_id}", headers=custom_headers, timeout=timeout)
    drep_votes = json.loads(drep_votes.content)
    return drep_votes


@Exception_Handler
def get_drep_delegators(self, drep_id, content_range="0-999"):
    """
    Get the delegators of a delegated representative (DRep).

    :param str drep_id: DRep ID in bech32 format (drep1...)
    :return: list of delegators of the DRep.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    delegators = requests.get(f"{self.DREP_DELEGATORS_URL}{drep_id}", headers=custom_headers, timeout=timeout)
    delegators = json.loads(delegators.content)
    return delegators


@Exception_Handler
def get_committee_info(self):
    """
    Get the current constitutional committee members, quorum and threshold.

    :return: list of committee information.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        committee_info = requests.get(self.COMMITTEE_INFO_URL, timeout=timeout)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        committee_info = requests.get(self.COMMITTEE_INFO_URL, timeout=timeout, headers=custom_headers)

    committee_info = json.loads(committee_info.content)
    return committee_info


@Exception_Handler
def get_committee_votes(self, cc_hot_id=None, content_range="0-999"):
    """
    Get the votes cast by a constitutional committee member, all members if empty.

    :param str cc_hot_id: Committee member hot key ID in bech32 format (cc_hot1...)
    :return: list of votes cast by the committee member.
    :rtype: list.
    """
    timeout = get_timeout()

    if cc_hot_id is None:
        url = self.COMMITTEE_VOTES_URL
    else:
        url = f"{self.COMMITTEE_VOTES_URL}?_cc_hot_id={cc_hot_id}"

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    committee_votes = requests.get(url, headers=custom_headers, timeout=timeout)
    committee_votes = json.loads(committee_votes.content)
    return committee_votes


@Exception_Handler
def get_proposal_list(self, content_range="0-999"):
    """
    Get the list of all governance action proposals.

    :return: list of governance action proposals.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    proposal_list = requests.get(self.PROPOSAL_LIST_URL, headers=custom_headers, timeout=timeout)
    proposal_list = json.loads(proposal_list.content)
    return proposal_list


@Exception_Handler
def get_voter_proposal_list(self, voter_id=None, content_range="0-999"):
    """
    Get the list of all governance action proposals a voter is eligible to vote on.

    :param str voter_id: Voter ID in bech32 format (drep1..., pool1... or cc_hot1...)
    :return: list of governance action proposals.
    :rtype: list.
    """
    timeout = get_timeout()

    if voter_id is None:
        url = self.VOTER_PROPOSAL_LIST_URL
    else:
        url = f"{self.VOTER_PROPOSAL_LIST_URL}?_voter_id={voter_id}"

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    proposal_list = requests.get(url, headers=custom_headers, timeout=timeout)
    proposal_list = json.loads(proposal_list.content)
    return proposal_list


@Exception_Handler
def get_proposal_voting_summary(self, proposal_id):
    """
    Get the summary of votes cast on a governance action proposal.

    :param str proposal_id: Governance action ID in bech32 format (gov_action1...)
    :return: list with the vote tally for the proposal.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        summary = requests.get(f"{self.PROPOSAL_VOTING_SUMMARY_URL}{proposal_id}", timeout=timeout)
    else:
        custom_headers = {"Authorization": f"Bearer {self.BEARER}"}
        summary = requests.get(f"{self.PROPOSAL_VOTING_SUMMARY_URL}{proposal_id}", timeout=timeout, headers=custom_headers)

    summary = json.loads(summary.content)
    return summary


@Exception_Handler
def get_proposal_votes(self, proposal_id, content_range="0-999"):
    """
    Get the votes cast on a governance action proposal.

    :param str proposal_id: Governance action ID in bech32 format (gov_action1...)
    :return: list of votes cast on the proposal.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    proposal_votes = requests.get(f"{self.PROPOSAL_VOTES_URL}{proposal_id}", headers=custom_headers, timeout=timeout)
    proposal_votes = json.loads(proposal_votes.content)
    return proposal_votes


@Exception_Handler
def get_vote_list(self, content_range="0-999"):
    """
    Get the list of all votes cast on governance action proposals.

    :return: list of all votes.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    vote_list = requests.get(self.VOTE_LIST_URL, headers=custom_headers, timeout=timeout)
    vote_list = json.loads(vote_list.content)
    return vote_list


@Exception_Handler
def get_pool_voting_power_history(self, pool_bech32=None, epoch_no=None, content_range="0-999"):
    """
    Get the voting power history of a stake pool, all pools if empty.

    :param str pool_bech32: Pool ID in bech32 format (pool1...)
    :param int epoch_no: Epoch Number to fetch details for.
    :return: list of pool voting power by epoch.
    :rtype: list.
    """
    timeout = get_timeout()

    params = []
    if pool_bech32 is not None:
        params.append(f"_pool_bech32={pool_bech32}")
    if epoch_no is not None:
        params.append(f"_epoch_no={epoch_no}")
    url = self.POOL_VOTING_POWER_HISTORY_URL if not params \
        else f"{self.POOL_VOTING_POWER_HISTORY_URL}?{'&'.join(params)}"

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    voting_power = requests.get(url, headers=custom_headers, timeout=timeout)
    voting_power = json.loads(voting_power.content)
    return voting_power


@Exception_Handler
def get_pool_votes(self, pool_bech32, content_range="0-999"):
    """
    Get the votes cast by a stake pool.

    :param str pool_bech32: Pool ID in bech32 format (pool1...)
    :return: list of votes cast by the pool.
    :rtype: list.
    """
    timeout = get_timeout()

    if self.BEARER is None:
        custom_headers = {"Range": str(content_range)}
    else:
        custom_headers = {"Range": str(content_range), "Authorization": f"Bearer {self.BEARER}"}

    pool_votes = requests.get(f"{self.POOL_VOTES_URL}{pool_bech32}", headers=custom_headers, timeout=timeout)
    pool_votes = json.loads(pool_votes.content)
    return pool_votes
