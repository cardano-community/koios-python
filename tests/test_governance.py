"""Offline tests for the Governance endpoints: no request leaves the process."""
from unittest import mock

import pytest

from koios_python import URLs

BASE = URLs().url

DREP = "drep1ytnzpxevx4wwnv77uadwxj3t7w2yvedlp6yvcdr7fgr9s7c4gtcg5"
POOL = "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
PROPOSAL = "gov_action1k2jertppnnndejjcglszfqq4yzw8evzrd2nt66rr6rd3t3yr0e8q9nsd3h8"
CC_HOT = "cc_hot1qgqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpqq6k"

# (method, args, kwargs, HTTP verb, URL, JSON body)
CASES = [
    ("get_drep_epoch_summary", (), {}, "get", "drep_epoch_summary", None),
    ("get_drep_epoch_summary", (), {"epoch_no": 540}, "get", "drep_epoch_summary?_epoch_no=540", None),
    ("get_drep_list", (), {}, "get", "drep_list", None),
    ("get_drep_info", (DREP,), {}, "post", "drep_info", {"_drep_ids": [DREP]}),
    ("get_drep_metadata", (DREP,), {}, "post", "drep_metadata", {"_drep_ids": [DREP]}),
    ("get_drep_updates", (), {}, "get", "drep_updates", None),
    ("get_drep_updates", (DREP,), {}, "get", f"drep_updates?_drep_id={DREP}", None),
    ("get_drep_history", (), {}, "get", "drep_history", None),
    ("get_drep_voting_power_history", (), {}, "get", "drep_voting_power_history", None),
    ("get_drep_votes", (DREP,), {}, "get", f"drep_votes?_drep_id={DREP}", None),
    ("get_drep_delegators", (DREP,), {}, "get", f"drep_delegators?_drep_id={DREP}", None),
    ("get_committee_info", (), {}, "get", "committee_info", None),
    ("get_committee_votes", (), {}, "get", "committee_votes", None),
    ("get_committee_votes", (CC_HOT,), {}, "get", f"committee_votes?_cc_hot_id={CC_HOT}", None),
    ("get_proposal_list", (), {}, "get", "proposal_list", None),
    ("get_voter_proposal_list", (), {}, "get", "voter_proposal_list", None),
    ("get_voter_proposal_list", (DREP,), {}, "get", f"voter_proposal_list?_voter_id={DREP}", None),
    ("get_proposal_voting_summary", (PROPOSAL,), {}, "get", f"proposal_voting_summary?_proposal_id={PROPOSAL}", None),
    ("get_proposal_votes", (PROPOSAL,), {}, "get", f"proposal_votes?_proposal_id={PROPOSAL}", None),
    ("get_vote_list", (), {}, "get", "vote_list", None),
    ("get_pool_voting_power_history", (), {}, "get", "pool_voting_power_history", None),
    ("get_pool_votes", (POOL,), {}, "get", f"pool_votes?_pool_bech32={POOL}", None),
]
IDS = [f"{c[0]}-{c[4].split('?')[-1][:24]}" for c in CASES]


def response(payload=b'[{"ok": true}]'):
    return mock.Mock(content=payload)


def call(kp, case, bearer=None):
    name, args, kwargs, verb, _url, _body = case
    kp.BEARER = bearer
    with mock.patch(f"koios_python.governance.requests.{verb}", return_value=response()) as sent:
        result = getattr(kp, name)(*args, **kwargs)
    return result, sent


@pytest.fixture
def kp():
    return URLs()


@pytest.mark.parametrize("case", CASES, ids=IDS)
def test_request_and_parsed_response(kp, case):
    result, sent = call(kp, case)

    assert result == [{"ok": True}]
    sent.assert_called_once()
    assert sent.call_args.args[0] == BASE + case[4]
    assert sent.call_args.kwargs.get("json") == case[5]
    assert "Authorization" not in sent.call_args.kwargs.get("headers", {})


@pytest.mark.parametrize("case", CASES, ids=IDS)
def test_bearer_token_is_sent(kp, case):
    _, sent = call(kp, case, bearer="secret")

    assert sent.call_args.kwargs["headers"]["Authorization"] == "Bearer secret"


@pytest.mark.parametrize(
    ("name", "args"),
    [
        ("get_drep_list", ()),
        ("get_drep_votes", (DREP,)),
        ("get_proposal_list", ()),
        ("get_vote_list", ()),
        ("get_pool_votes", (POOL,)),
    ],
)
def test_paginated_endpoints_send_the_range_header(kp, name, args):
    with mock.patch("koios_python.governance.requests.get", return_value=response()) as sent:
        getattr(kp, name)(*args, content_range="1000-1999")

    assert sent.call_args.kwargs["headers"]["Range"] == "1000-1999"


def test_default_range_is_the_first_page(kp):
    with mock.patch("koios_python.governance.requests.get", return_value=response()) as sent:
        kp.get_drep_list()

    assert sent.call_args.kwargs["headers"]["Range"] == "0-999"


def test_drep_info_accepts_several_ids(kp):
    other = "drep1ytnzpxevx4wwnv77uadwxj3t7w2yvedlp6yvcdr7fgr9s7c4gtcg6"
    with mock.patch("koios_python.governance.requests.post", return_value=response()) as sent:
        kp.get_drep_info(DREP, other)

    assert sent.call_args.kwargs["json"] == {"_drep_ids": [DREP, other]}


def test_history_filters_are_combined(kp):
    with mock.patch("koios_python.governance.requests.get", return_value=response()) as sent:
        kp.get_drep_history(drep_id=DREP, epoch_no=540)

    url = sent.call_args.args[0]
    assert url.startswith(BASE + "drep_history?")
    assert f"_drep_id={DREP}" in url
    assert "_epoch_no=540" in url


def test_pool_voting_power_history_filters_are_combined(kp):
    with mock.patch("koios_python.governance.requests.get", return_value=response()) as sent:
        kp.get_pool_voting_power_history(pool_bech32=POOL, epoch_no=540)

    url = sent.call_args.args[0]
    assert f"_pool_bech32={POOL}" in url
    assert "_epoch_no=540" in url
