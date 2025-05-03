from datetime import datetime, timedelta
from src.config import logger as root_logger
from src.actions.base_action import GitHubAction

logger = root_logger.getChild("issue_closer")


class StaleIssueAutoCloser(GitHubAction):
    def __init__(self, client, days_stale=30):
        super().__init__(client)
        self.days_stale = days_stale

    def clean(self):
        cutoff = datetime.utcnow() - timedelta(days=self.days_stale)
        issues = self.client._request('GET', '/issues', params={'state': 'open'})
        stale = [i for i in issues if datetime.strptime(i['updated_at'], "%Y-%m-%dT%H:%M:%SZ") < cutoff]
        logger.info(f"Found {len(stale)} stale issues.")
        for i in stale:
            num = i['number']
            try:
                self.client._request('PATCH', f"/issues/{num}", json={'state':'closed'})
                logger.info(f"Closed issue #{num}")
            except Exception:
                logger.warning(f"Failed to close issue #{num}", exc_info=True)
