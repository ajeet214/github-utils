import pytest
from unittest.mock import Mock
from datetime import datetime, timedelta
from src.actions.issue_closer import StaleIssueAutoCloser

@pytest.fixture
def closer():
    client = Mock()
    return StaleIssueAutoCloser(client, days_stale=1)


def test_clean_closes_stale_issues(closer):
    old_date = (datetime.utcnow() - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    issues = [{"number": 5, "updated_at": old_date}, {"number": 6, "updated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}]
    closer.client._request.side_effect = [issues, None]

    closer.clean()

    closer.client._request.assert_any_call('PATCH', '/issues/5', json={'state': 'closed'})
