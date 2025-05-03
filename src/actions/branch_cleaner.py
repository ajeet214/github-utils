from datetime import datetime, timedelta
from src.config import logger as root_logger
from src.actions.base_action import GitHubAction

logger = root_logger.getChild("branch_cleaner")


class BranchCleaner(GitHubAction):
    def __init__(self, client, days_stale=30):
        super().__init__(client)
        self.days_stale = days_stale

    def clean(self):
        cutoff = datetime.utcnow() - timedelta(days=self.days_stale)
        branches = self.client._request('GET', '/branches')
        stale = [b for b in branches if datetime.strptime(b['commit']['commit']['author']['date'],
                                                           "%Y-%m-%dT%H:%M:%SZ") < cutoff]
        logger.info(f"Found {len(stale)} stale branches.")
        for b in stale:
            name = b['name']
            try:
                self.client._request('DELETE', f"/git/refs/heads/{name}")
                logger.info(f"Deleted branch {name}")
            except Exception:
                logger.warning(f"Failed to delete branch {name}", exc_info=True)
