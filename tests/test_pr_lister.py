import pytest
from unittest.mock import Mock
from src.actions.pr_lister import PullRequestLister

@pytest.fixture
def lister():
    client = Mock()
    return PullRequestLister(client, state='open')


def test_list_logs_prs(caplog, lister):
    caplog.set_level(lister.client._request.__class__.__name__)
    prs = [{"number": 1, "title": "Test PR"}]
    lister.client._request.return_value = prs

    lister.list()

    # Check that PR info is in logs
    assert any("PR #1: Test PR" in rec.message for rec in caplog.records)
