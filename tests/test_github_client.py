import pytest
import requests
from unittest.mock import patch, Mock
from src.utils.github_client import GitHubAPIClient

@pytest.fixture
def client():
    return GitHubAPIClient(token='token', owner='owner', repo='repo')

@patch('requests.request')
def test_request_success(mock_req, client):
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.content = b'{"key": "value"}'
    mock_resp.json.return_value = {"key": "value"}
    mock_req.return_value = mock_resp

    result = client._request('GET', '/path')
    assert result == {"key": "value"}

@patch('requests.request')
def test_request_http_error(mock_req, client):
    mock_resp = Mock()
    mock_resp.status_code = 404
    mock_resp.content = b''
    mock_resp.raise_for_status.side_effect = requests.HTTPError(response=mock_resp)
    mock_req.return_value = mock_resp

    with pytest.raises(requests.HTTPError):
        client._request('GET', '/path')