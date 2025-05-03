import pytest
from unittest.mock import Mock
from datetime import datetime, timedelta
from src.actions.branch_cleaner import BranchCleaner

@pytest.fixture
def cleaner():
    client = Mock()
    return BranchCleaner(client, days_stale=1)


def test_clean_deletes_stale_branches(cleaner):
    old_date = (datetime.utcnow() - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    branches = [ {"name": "old", "commit": {"commit": {"author": {"date": old_date}}}},
                 {"name": "new", "commit": {"commit": {"author": {"date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}}}} ]
    cleaner.client._request.side_effect = [branches, None]

    cleaner.clean()

    # First call lists branches, second deletes
    cleaner.client._request.assert_any_call('DELETE', '/git/refs/heads/old')