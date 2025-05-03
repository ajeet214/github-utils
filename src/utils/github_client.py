import requests
from requests.exceptions import HTTPError
from src.config import logger as root_logger

logger = root_logger.getChild("github_client")


class GitHubAPIClient:
    def __init__(self, token: str, owner: str, repo: str):
        self.base_url = f'https://api.github.com/repos/{owner}/{repo}'
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github+json',
        }

    def _request(self, method: str, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        logger.debug(f"REQUEST {method} {url} params={kwargs.get('params')} json={kwargs.get('json')}")
        resp = requests.request(method, url, headers=self.headers, **kwargs)
        try:
            resp.raise_for_status()
        except HTTPError as e:
            logger.error(f"HTTP {resp.status_code} error: {resp.text}")
            raise
        logger.debug(f"RESPONSE {resp.status_code}")
        return resp.json() if resp.content else None

    def list_workflows(self):
        return self._request('GET', '/actions/workflows')['workflows']

    def list_workflow_runs(self, workflow_id=None, status=None, per_page=30):
        path = f'/actions/workflows/{workflow_id}/runs' if workflow_id else '/actions/runs'
        params = {'per_page': per_page}
        if status:
            params['status'] = status
        return self._request('GET', path, params=params)['workflow_runs']

    def delete_workflow_run(self, run_id: int):
        self._request('DELETE', f'/actions/runs/{run_id}')
        return True

    # Additional methods for branches, PRs, issues can be added here.
