import pytest
from unittest.mock import Mock
from src.actions.workflow_cleaner import WorkflowCleaner

@pytest.fixture
def cleaner():
    client = Mock()
    return WorkflowCleaner(client, workflow_filename='wf.yml', max_runs=2, status='completed')

def test_find_workflow_id(cleaner):
    cleaner.client.list_workflows.return_value = [
        {"id": 1, "path": ".github/workflows/wf.yml"},
    ]
    assert cleaner._find_workflow_id() == 1


def test_find_workflow_id_not_found(cleaner):
    cleaner.client.list_workflows.return_value = []
    with pytest.raises(ValueError):
        cleaner._find_workflow_id()


def test_clean_deletes_runs(cleaner):
    cleaner._find_workflow_id = Mock(return_value=1)
    cleaner.client.list_workflow_runs.return_value = [ {"id": 10}, {"id": 20} ]
    cleaner.client.delete_workflow_run = Mock()

    cleaner.clean()

    cleaner.client.delete_workflow_run.assert_any_call(10)
    cleaner.client.delete_workflow_run.assert_any_call(20)
